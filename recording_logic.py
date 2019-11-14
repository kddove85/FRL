import os
import vlc
import time
import pydub
import pyaudio
import wave
import threading
from datetime import datetime


class RecordingLogic:
    # TODO: Below is what the signature needs to become
    def __init__(self, station, start_time, end_time):
        self.file_name = 'output.wav'

        length_of_recording = self._get_length(start_time, end_time)

        now = datetime.now().strftime("%H:%M")
        while now != start_time.strftime("%H:%M"):
            now = datetime.now().strftime("%H:%M")
            print("Current Time =", now)
            time.sleep(1)

        t1 = threading.Thread(target=self._play, args=(station, end_time), name='t1')
        t2 = threading.Thread(target=self._record_audio, args=(length_of_recording, self.file_name), name='t2')

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print('Both things are done')

        self._convert_to_mp3(self.file_name)

    def _print_a(self, num):
        for x in range(0, num):
            print('a')

    def _print_b(self, num):
        for x in range(0, num):
            print('b')

    def _play(self, url, end_time):
        player = vlc.MediaPlayer(url)
        player.play()

        now = datetime.now().strftime("%H:%M")
        while now != end_time.strftime("%H:%M"):
            now = datetime.now().strftime("%H:%M")
            print("Current Time =", now)
            time.sleep(1)
        player.stop()

    def _record_audio(self, seconds, file_name):
        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 2
        fs = 44100  # Record at 44100 samples per second
        # seconds = 10
        filename = file_name

        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        time.sleep(5)

    def _convert_to_mp3(self, wave_file):
        sound = pydub.AudioSegment.from_wav(wave_file)  # 'myfile.wav'
        sound.export('myfile.mp3', format='mp3')
        os.remove(wave_file)

    def _get_length(self, start_time, end_time):
        diff = end_time - start_time
        return diff.seconds
