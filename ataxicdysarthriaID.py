import os
import shutil
import speech_recognition as sr

# Define the patterns to detect
patterns = [
    "irregular speech rate or rhythm",
    "slurring of words or syllables",
    "difficulty with articulation",
    "overshooting or undershooting of speech targets",
    "intonation abnormalities"
]

# Define the input and output directories
input_dir = "input"
output_dir = "output"

# Initialize the speech recognition engine
r = sr.Recognizer()

# Iterate over audio files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".wav") or filename.endswith(".mp3"):
        # Load the audio file for speech recognition
        with sr.AudioFile(os.path.join(input_dir, filename)) as source:
            audio = r.record(source)

        # Transcribe the audio using the speech recognition engine
        transcription = r.recognize_google(audio)

        # Check for each pattern in the transcription
        for pattern in patterns:
            if pattern in transcription.lower():
                # If the pattern is detected, save the audio file to the output directory
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                shutil.copy(os.path.join(input_dir, filename), os.path.join(output_dir, filename))
