# FRL
Frequency Recording Library

## Requirements

You will need to manually get the library for pyaudio!
You can find multiple versions here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
Look for the .whl file specific to your version of Python and OS

You will also need to download VLC(https://www.videolan.org/vlc/index.html) and ffmpeg(https://www.ffmpeg.org/)

In addition, you will also need a virtual input/output device like VoiceMeter Banana. You need to use this device so 
that you can record playback. Note that VoiceMeter is a Windows Only product. You can find more information on 
installing VoiceMeter here: https://youtu.be/XD9sWOjITYU

Once these are downloaded and installed, you will have to update your Path Environment Variable for the locations of
these two items. For instance:

C:\Program Files\VideoLAN\VLC

C:\Program Files\ffmpeg\bin

Once all of this has been complete, you should be able to run the application.

If you receive an error such as having an improper input device, reference your program's output. Note this part of the 
logs:
```commandline
Input Device id  0  -  Microsoft Sound Mapper - Input
Input Device id  1  -  Microphone (Blue Snowball )
Input Device id  2  -  Stereo Mix (Realtek(R) Audio)
Input Device id  3  -  VoiceMeeter Output (VB-Audio Vo
Input Device id  4  -  CABLE Output (VB-Audio Virtual 
Input Device id  5  -  VoiceMeeter Aux Output (VB-Audi
Input Device id  6  -  Microphone (HD Pro Webcam C920)
Output Device id  7  -  Microsoft Sound Mapper - Output
Output Device id  8  -  VoiceMeeter Input (VB-Audio Voi
Output Device id  9  -  CABLE Input (VB-Audio Virtual C
Output Device id  10  -  VoiceMeeter Aux Input (VB-Audio
Output Device id  11  -  VG259QM (NVIDIA High Definition
Output Device id  12  -  NS-24D510NA17 (NVIDIA High Defi
```

The application has been written so that all the input and output devices are printed for your convenience. To record
desktop playback, select the option that corresponds to VoiceMeeter Output (VB-Audio Vo). In this case, it would be 
Device ID 3.

## Purpose

Let's say you want to listen to a podcast BUT the program you want to listen to either does not put their programs in 
podcast form OR they are behind a pay wall BUT the program is played on FREE internet radio. This is the solution! What 
FRL does is, you set a start time and an end time for your podcast as well as an internet radio station using the UI. 
Then, once your system reaches that start time, it will start to record a wave file of the program. Once completed it 
will output the wave file AND convert it to mp3 to save space. Presto! You now have a podcast of a program.

## Future Ideas

1. Delete the wave file when finished converting
2. Make the output location optional
3. Use the GUI to add other radio stations
