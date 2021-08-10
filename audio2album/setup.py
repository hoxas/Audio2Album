from setuptools import setup
from os import path

appversion = '0.0.0'

here = path.abspath(path.dirname(__file__))

with open(here + 'audio2album/__init__.py') as initpy:
    initpy.write(f'__version__  = {appversion}')

setup(
    name = 'audio2album',
    version = appversion,
    description = 'audio2album slices mp3 files and tags them with metadata',
    long_description = open('README.md').read(),
    url = 'http://github.com/hoxas/Audio2Album',
    author = 'hoxas',
    author_email = 'hoxas@live.com',
    license = 'unlicense',
    classifiers = [
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: Public Domain',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.9'
    ],
    keywords = ['audio', 'album', 'music', 'cli', 'albums', 'cut', 'slice', 'id3'],
    python_requires = '>=3.6',
    install_requires = [
        'mutagen==1.45.1',
        'pydub==0.25.1'
    ],
    packages = ['audio2album'],
    entry_points = {
        'console_scripts': [
            'audio2album = audio2album.__main__:main'
        ]
    }
)