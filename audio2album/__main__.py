import os, sys

from .Editor import Cut
from .PathTool import getPath

## FFMPEG ON PATH

### Setup Functions
help = '''
Audio2Album

Usage:
    python Audio2Album.py [optional arg1] [optional arg2]

Args:
    ->  h or help: Prints this screen
        
    ->  mktxt: Makes text file for easier use
            |-> arg2: Name of output txt file
        
    ->  path/to/track: Path to mp3 that is gonna be cut
            |-> arg2: path to txt file that contains the parameters

If no arg is given then the program asks for the info as it is needed

* (CTRL + C) to close
'''

# print help
try:
    if sys.argv[1] == 'h' or sys.argv[1] == 'help': 
        print(help)
        exit()    
except IndexError:
    pass

# create txt file for easier use
try:
    if sys.argv[1] == 'mktxt':
        try:
            name = getPath(sys.argv[2]) + '.txt'
            w = open(name, 'w')
        except:
            w = open(getPath('ToAlbumStamps.txt'), 'w')

        lines = [
            'Album:\n', 
            'Artist:\n', 
            'Release:\n',  
            'VVV Tracks Below VVV\n',
            '1.Track--Start--End\n',
            '2.\n'
            ]
        for line in lines:
            w.write(line)
        exit()
except:
    pass


category = {}

### Main Program Start
def main():
    # Test for given filepath/name
    try:
        filename = sys.argv[1]
    except:
        print('Enter file: ')
        filename = input()

    # get and filter path
    pathfile = getPath(filename)

    

    ### IF TXT FILE PATH GIVEN
    if len(sys.argv) == 3:
        txtpath = getPath(sys.argv[2])
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

        print('How many trks: ')
        numberoftracks = int(input())

        category['track'] = 1

        # Getting times by input
        while category['track'] <= numberoftracks:
            print('Track: ')
            category['title'] = input()

            # get times
            print('Start (h:m:s): ')
            start = input()

            print('End (h:m:s): ')
            end = input()

            Cut(pathfile, start, end, category)

            category['track'] += 1

if __name__ == '__main__':
    main()   

