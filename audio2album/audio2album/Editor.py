import os
from mutagen.mp3 import MP3
from mutagen import easyid3 as eid
from pydub import AudioSegment
from pydub.utils import mediainfo
from datetime import datetime
from pathlib import Path


# print(eid.EasyID3.valid_keys.keys())

class Cut:
    """Slice audio clips & Export (pathfile, start, end, category)

    Arguments:
    str(pathfile): Path to mp3
    str(start): Start of cut
    str(end): End of cut
    list(category): Tagging parameters 
    """

    def getTime(self, t):
        '''From string(t) to datetime object'''

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

    def toMilli(self, t):
        '''From datetime(t) to int(milliseconds)'''

        t_timedelta = t - datetime(1900, 1, 1)
        seconds = t_timedelta.total_seconds()
        return seconds * 1000

    def slice(self):
        # cut track 
        cuttrack = self.file[self.mstart:self.mend]

        # exporting
        if int(self.category['track']) < 10:
            zero = '0'
        else:
            zero = ''

        self.trackname = f"{zero}{self.category['track']}. {self.category['title']}.mp3"
        
        cuttrack.export(f"{self.outpath}\{self.trackname}", format='mp3', bitrate=self.tbitrate)
    
    def tag(self):
        # tagging 
        exported = eid.EasyID3(f'{self.outpath}\{self.trackname}')

        exported['tracknumber'] = self.category['track']
        exported['title'] = self.category['title']
        exported['artist'] = self.category['artist']
        exported['albumartist'] = self.category['artist']
        exported['album'] = self.category['album']
        exported['date'] = self.category['release']
        exported.save()


    def __init__(self, pathfile, start, end, category):
        # opening file
        self.file = AudioSegment.from_mp3(pathfile)

        # get total length 
        self.totalt = MP3(pathfile).info.length
        self.mtotalt = self.totalt * 1000

        self.category = category

        # getting input bitrate
        self.tbitrate = mediainfo(pathfile)['bit_rate']

        # parsing cut times and converting to millisecs
        self.start = self.getTime(start)
        self.mstart = self.toMilli(self.start)
        
        if end.upper() == 'END':
            self.mend = self.mtotalt
        else:
            self.end = self.getTime(end)
            self.mend = self.toMilli(self.end)
            #check if end higher than total track time
            if self.mend > self.mtotalt:
                self.mend = self.mtotalt
        
        self.folder = f"{self.category['artist']} - {self.category['album']}"
        self.outpath = os.path.join(os.getcwd(), self.folder)
            
        Path(self.outpath).mkdir(parents=True, exist_ok=True)
        self.slice()
        self.tag()

        


        
        
        
        

    
