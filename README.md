# FRL
Frequency Recording Library

## Requirements

You will need to manually get the library for pyaudio!
You can find multiple versions here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
Look for the .whl file specific to your version of Python and OS

You will also need to download VLC(https://www.videolan.org/vlc/index.html) and ffmpeg(https://www.ffmpeg.org/)

Once these are downloaded and installed, you will have to update your Path Environment Variable for the locations of
these two items. For instance:

C:\Program Files\VideoLAN\VLC

C:\Program Files\ffmpeg\bin

Once all of this has been complete, you should be able to run the application.

## Purpose

Let's say you want to listen to a podcast BUT the program you want to listen to either doesn't put their programs in podcast form OR they are behind a pay wall BUT the program is played on FREE internet radio. This is the solution! What FRL does is, you set a start time and an end time for your podcast as well as an internet radio station using the UI. Then, once your system reaches that start time, it will start to record a wave file of the program. Once completed it will output the wave file AND convert it to mp3 to save space. Voila. You now have a podcast of a program.

## Future Ideas

1. Delete the wave file when finished converting
2. Make the output location optional
3. Use the GUI to add other radio stations
