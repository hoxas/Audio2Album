import os, subprocess

def getPath(filename):
    """
    Clean up/format path string(filename)

    :rtype: str
    :return: path string
    """

    if os.path.isabs(filename):
        pathfile = filename
        return pathfile
    else:
        filename = filename.lstrip('/\.')
        filename = filename.replace('/', '\\')
        pathfile = os.path.join(os.getcwd(), filename)
        return pathfile

def checkFFMPEG():
        """
        Check for ffmpeg

        :rtype: str/bool
        :return: true if present, false otherwise
        """
        try:
            subprocess.run('ffmpeg -version', stdout=subprocess.DEVNULL)
            return True
        except FileNotFoundError as e:
            return False

