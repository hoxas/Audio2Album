audio2album
===============

cut mp3 into albums with metadata tagging and youtube-dl

Description
-----------

**audio2album** is a CLI to cut mp3s and tags them, it also accepts an youtube URL as the mp3 path. audio2album also features a .txt parser which reads the inputs rather than manually entering then in the command line.

**Python 3.9**

Installation
------------

From PyPI
~~~~~~~~~

``pip3 install audio2album``

OR w/ pipx (recommended)

``pipx install audio2album``

From Source
~~~~~~~~~~~

1. Clone the project or `download and extract the zip <https://github.com/hoxas/Audio2Album/archive/master.zip>`_
2. ``cd`` to the project directory containing the ``setup.py``
3. ``python setup.py install`` or ``pipx install .``

Details
-------

::

    Usage:
        audio2album [options | URL] [TXTPATH] [--keepfile]

    Arguments:
        URL         path/to/mp3 or youtube.com/url
        TXTPATH     path/to/txtfile -> parse or output

Options
-------

::

    Options:
        -h --help                       Show this screen
        -v --version                    Show version
        -d --debug                      Verbose logging
        --mktxt                         Makes txt file for easier use
        --keepfile                      Keeps downloaded uncut file

TXTFILE
-------

With --mktxt you can output a txt file (TXTPATH) that can be used to feed the information to the app.

The basic structure required in the txt file is as follows:

::

    Album:
    Artist: 
    Release:  
    VVV
    1.TrackName--Start--End
    2.Justatrack--0--2:40"

The first three parameters **Album**, **Artist** and **Release** (Release year) can be placed in any order as long as the keys are the same.

The **"VVV"** indicates that below is the tracklist with the times.

**Track Template:**
(TrackNumber).(TrackName)--(StartTime)--(EndTime)

**Time Template:** [H]:[M]:S.[ms] ([] = optional)

Time Shortcuts
--------------

Instead of times following the given **Time Template** audio2album also accepts:

- "0" - as second 0
- "END" - end of the mp3 file (case-insensitive)

Example:

::
    
    1.WholeMP3--0--END

