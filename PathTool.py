import os

def getPath(filename):
    '''Clean up path string(filename)'''

    if os.path.isabs(filename):
        pathfile = filename
        return pathfile
    else:
        filename = filename.lstrip('/\.')
        filename = filename.replace('/', '\\')
        pathfile = os.path.join(os.getcwd(), filename)
        return pathfile