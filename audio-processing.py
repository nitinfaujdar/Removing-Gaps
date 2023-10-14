from pydub import AudioSegment
from pydub.silence import split_on_silence

# Load the audio file
audio = AudioSegment.from_file("Desktop/Raagbilaaval5.wav")

# Define the minimum silence length and silence threshold in milliseconds
min_silence_length = 100  # 1 second
silence_threshold = -30  # Adjust this value based on your audio file

# Split the audio into segments where silence is detected
segments = split_on_silence(audio, min_silence_len=min_silence_length, silence_thresh=silence_threshold)

# Concatenate the non-silent segments to create the output audio
output_audio = AudioSegment.empty()
for segment in segments:
    output_audio += segment

# Export the output audio to a file
output_audio.export("Desktop/output1.wav", format="wav")
