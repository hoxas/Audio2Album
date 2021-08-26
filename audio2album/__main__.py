'''
audio2album

Usage:
    audio2album [options | URL] [TXTPATH] [--keepfile]

Options:
    -h --help                       Show this screen
    -v --version                    Show version
    -d --debug                      Verbose logging
    --mktxt                         Makes txt file for easier use (Accepts txt output path)
    --keepfile                      Keeps downloaded uncut file
                                    

URL = path/to/mp3

TXTPATH = path to text file/output OR youtube URL

If no arg is given the program asks for the info as it is needed

* (CTRL + C) to close
'''

import os, sys, pkg_resources

from docopt import docopt

from .Editor import Cut
from .PathTool import getPath
from .YtMP3Downloader import download

## FFMPEG ON PATH

### Setup

__version__ = pkg_resources.require('audio2album')[0].version

arguments = docopt(__doc__, version=f'audio2album {__version__}')
print(arguments)

if arguments['--mktxt']:
    """Create txt file for easy use"""
    lines = [
            'Album:\n', 
            'Artist:\n', 
            'Release:\n',  
            'VVV Tracks Below VVV\n',
            '1.Track--Start--End\n',
            '2.\n'
            ]

    def writer(filepath):
        w = open(filepath, 'w')
        for line in lines:
            w.write(line)
        exit()
    
    if arguments['TXTPATH']:
        filepath = getPath(arguments['TXTPATH']) + '.txt'
    else:
        filepath = getPath('ToAlbumStamps.txt')
    
    print(f'Writing file:\n    {filepath}')
    writer(filepath)

    

    
    


category = {}

### Main Program Start
def main():
    # Test for given filepath/name
    
    if arguments['URL']:
        filename = arguments['URL']
    else:
        print('Enter file path/ytURL: ')
        filename = input()

    # get and filter path
    if 'youtube.com/' in filename:
        youtube = True
        print('Youtube: ' + filename)
        pathfile = getPath(download(filename) + '.mp3')
    else:
        youtube = False
        print('Path: ' + filename)
        pathfile = getPath(filename)

    

    ### IF TXT FILE PATH GIVEN
    if arguments['TXTPATH']:
        txtpath = arguments['TXTPATH']
        # check if txt is there
        if os.path.isfile(txtpath):
            with open(txtpath, 'r') as r:
                content = r.readlines()
                isTrack = False;
                for line in content:
                    # Getting tracktime and cutting
                    if isTrack == True:
                        x = line.split('.')
                        category['track'] = x[0]
                        y = x[1].split('--')
                        category['title'] = y[0].strip()
                        
                        start = y[1].strip()
                        end = y[2].strip()

                        Cut(pathfile, start, end, category)
                        
                        print(f'Track {category["track"]} - {category["title"]} -> Exported')

                    
                    # Activates track condition above
                    if 'VVV' in line:
                        isTrack = True
                    
                    #Split Tagname from Name
                    if isTrack == False:
                        x = line.split(':', 1)
                        category[x[0].lower()] = x[1].replace('\n', '').strip()

    ### IF NO TXT FILE IS GIVEN
    else:
        print('AlbName: ')
        category['album'] = input()

        print('AlbArtist: ')
        category['artist'] = input()

        print('Date: ')
        category['release'] = input()

        print('How many tracks: ')
        numberoftracks = int(input())

        category['track'] = 1

        # Getting times by input
        while category['track'] <= numberoftracks:
            print('Trackname: ')
            category['title'] = input()

            # get times
            print('Start (h:m:s): ')
            start = input()

            print('End (h:m:s): ')
            end = input();

            Cut(pathfile, start, end, category)

            category['track'] += 1

    if youtube == True:
        if arguments['--keepfile']:
            print(f'Keeping file: {pathfile}')
        else:
            print(f'Deleting: {pathfile}')
            os.remove(pathfile)

if __name__ == '__main__':
    main()   

