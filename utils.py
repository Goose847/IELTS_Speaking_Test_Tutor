import sounddevice as sd
import numpy as np
import wave
from openai import OpenAI
from scipy.io import wavfile
from pynput import keyboard
import os
import termios
import sys

API_KEY = 'INSERT API KEY HERE'

################## AUDIO ##################
RATE = 44100
CHANNELS = 1
DURATION = 15


recording = False
audio_frames = []

def on_press(key):
    global recording
    if key == keyboard.Key.space:
        recording = not recording

def record_audio_with_spacebar():
    global recording, audio_frames
    print("Press SPACE to start/stop recording.")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    audio_frames = []
    recording_started = False
    stream = sd.InputStream(samplerate=RATE, channels=CHANNELS, dtype='int16')

    with stream:
        while listener.running:
            if recording:
                recording_started = True
                print("Recording...", end="\r")
                audio_data, _ = stream.read(1024)
                audio_frames.append(audio_data)
            elif recording_started:
                # Ensures the loop exits only if recording has started.
                print("Recording stopped.")
                break

    listener.stop()
    return np.concatenate(audio_frames) if audio_frames else None


def save_audio(data, filename):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)
        wf.setframerate(RATE)
        wf.writeframes(data)


def answer_question(Q_number):
    print("-------------------------------------------------------------------")
    global audio_frames
    audio_data = record_audio_with_spacebar()
    filename = "question_" + str(Q_number) + ".wav"
    save_audio(audio_data, filename)
    print("Recording saved.")
    print("-------------------------------------------------------------------")

    client = OpenAI(api_key=API_KEY)
    audio_file = open(filename, "rb")
    transcription = client.audio.transcriptions.create(
    model='whisper-1',
    file=audio_file
    )
    return(transcription.text)


# Function to play a wav file
def play_wav_file(filename):
    # Read the WAV file
    rate, data = wavfile.read(filename)
    
    # Play the audio
    print(f"Playing {filename}...")
    sd.play(data, samplerate=rate)
    sd.wait()  # Wait until the audio finishes playing

###########################################

def clean_directory():
    """Deletes all .wav files in the current directory.
    This is to prevent the directory from getting cluttered with .wav files."""
    current_directory = os.getcwd()
    for file in os.listdir(current_directory):
        if file.endswith(".wav"):
            os.remove(file)
            
def flush_input():
    '''Flushes the input buffer.
        This fixes an issue in which the program would pass the input
        to the terminal instead of the program.'''
    termios.tcflush(sys.stdin, termios.TCIOFLUSH)