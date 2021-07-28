import os, sys

from datetime import datetime
import time

from mutagen.mp3 import MP3
from mutagen import easyid3 as eid
from pydub import AudioSegment

print(eid.EasyID3.valid_keys.keys())

try:
    filename = sys.argv[1]
except:
    print('Enter file: ')
    filename = input()

if os.path.isabs(filename):
    print('True')
    pathfile = filename
else:
    print('False')
    pathfile = os.path.join(os.getcwd(), filename)

print(filename)

file = AudioSegment.from_mp3(pathfile)

totalt = MP3(pathfile).info.length

print(totalt)

print('AlbName: ')
album = input()

print('AlbArtist: ')
artist = input()

print('Date: ')
release = input()

print('How many trks: ')
tracksnumber = int(input())

def getTime(t):
    if t.upper() == 'END':
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

def toMilli(t):
    if t == 'END':
        return totalt * 1000

    t_timedelta = t - datetime(1900, 1, 1)
    seconds = t_timedelta.total_seconds()
    return seconds * 1000

track = 1

while track <= tracksnumber:
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

    # cut track 
    cuttrack = file[mstart:mend]

    # exporting

    if track < 10:
        zero = '0'
    else:
        zero = ''

    trackname = f"{zero}{track}. {tname}.mp3"
    
    cuttrack.export(trackname, format='mp3')

    # tagging 
    exported = eid.EasyID3(trackname)

    exported['tracknumber'] = str(track)
    exported['title'] = tname
    exported['artist'] = artist
    exported['albumartist'] = artist
    exported['album'] = album
    exported['date'] = release
    exported.save()

    track += 1

    

