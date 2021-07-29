import os, sys

from datetime import datetime

from pathlib import Path

## FFMPEG ON PATH

from mutagen.mp3 import MP3
from mutagen import easyid3 as eid
from pydub import AudioSegment
from pydub.utils import mediainfo

# print(eid.EasyID3.valid_keys.keys())

# from string to datetime
def getTime(t):
    if str(t).upper() == 'END':
        return 'END'

    if '.' in t:
        mili = '.%f'
    else:
        mili = ''

    try:
        t = datetime.strptime(t, f'%H:%M:%S{mili}')
    except:
        try:
            t = datetime.strptime(t, f'%M:%S{mili}')
        except:
            t = datetime.strptime(t, f'%S{mili}')
    return t

# to milliseconds
def toMilli(t):
    if t == 'END':
        return totalt * 1000

    t_timedelta = t - datetime(1900, 1, 1)
    seconds = t_timedelta.total_seconds()
    return seconds * 1000

# clean up paths
def getPath(filename):
    if os.path.isabs(filename):
        pathfile = filename
        return pathfile
    else:
        if '.\\' in filename[0:2]:
            filename = filename[2:] 
        pathfile = os.path.join(os.getcwd(), filename)
        return pathfile

# create txt file for easier use
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

category = {}

def sliceMain():
    # cut track 
    cuttrack = file[mstart:mend]

    # exporting

    if track < 10:
        zero = '0'
    else:
        zero = ''

    trackname = f"{zero}{track}. {tname}.mp3"
    
    cuttrack.export(trackname, format='mp3', bitrate=tbitrate)

    # tagging 
    exported = eid.EasyID3(trackname)

    exported['tracknumber'] = str(track)
    exported['title'] = tname
    exported['artist'] = category['artist']
    exported['albumartist'] = category['artist']
    exported['album'] = category['album']
    exported['date'] = category['release']
    exported.save()

### Main Program Start

# Test for given filepath/name
try:
    filename = sys.argv[1]
except:
    print('Enter file: ')
    filename = input()

# get and filter path
pathfile = getPath(filename)

# getting input bitrate
tbitrate = mediainfo(pathfile)['bit_rate']
# opening file
file = AudioSegment.from_mp3(pathfile)
# get total length (unused still)
totalt = MP3(pathfile).info.length
print(totalt)

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
                    track = int(x[0])
                    y = x[1].split('--')
                    tname = y[0].strip()

                    tstart = getTime(y[1].strip())
                    mstart = toMilli(tstart)
                    tend = getTime(y[2].strip())
                    mend = toMilli(tend)

                    sliceMain()
                
                # Activates track condition above
                if 'VVV' in line:
                    isTrack = True
                
                #Split Tagname from Name
                if isTrack == False:
                    x = line.split(':', 1)
                    category[x[0].lower()] = x[1].replace('\n', '').strip()
else:
    print('AlbName: ')
    category['album'] = input()

    print('AlbArtist: ')
    category['artist'] = input()

    print('Date: ')
    category['release'] = input()

    print('How many trks: ')
    numberoftracks = int(input())

    track = 1

    # Getting times by input
    while track <= numberoftracks:
        print('Track: ')
        tname = input()

        # get times
        print('Start (h:m:s): ')
        tstart = getTime(input())
        mstart = toMilli(tstart)

        print('End (h:m:s): ')
        tend = getTime(input())
        mend = toMilli(tend)

        print(mstart, mend)

        sliceMain()

        track += 1

    

