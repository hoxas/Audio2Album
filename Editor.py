import os, sys

from datetime import datetime
from pydub import AudioSegment
from mutagen.mp3 import MP3

class Cut():
    def __init__(self, track, start, end):
        self.start = start
        self.end = end
        self.total = MP3(track).info.length

    # from string to datetime
    def getTime(self):
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

 
    





def sliceMain():
    # cut track 
    cuttrack = file[mstart:mend]

    # exporting

    if track < 10:
        zero = '0'
    else:
        zero = ''

    trackname = f"{zero}{track}. {category['title']}.mp3"
    
    cuttrack.export(trackname, format='mp3', bitrate=tbitrate)