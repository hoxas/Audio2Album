import youtube_dl

def download(URL: str):


    def my_hook(d):
        if d['status'] == 'finished':
            print('Done downloading, now converting ...')


    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'progress_hooks': [my_hook]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading...')
        ''' ydl.download([URL]) '''
        info = ydl.extract_info(URL)

        video_title = info.get('title', None)
        video_title = video_title.replace(':', ' -')
        video_id = info.get("id", None)
        pathfile = f'{video_title}-{video_id}'
        return pathfile

        