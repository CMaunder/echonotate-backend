import librosa
from os import path
from pydub import AudioSegment


# assign files
input_file = "./c-major-scale.mp3"
output_file = "./c-major-scale.wav"

# convert mp3 file to wav file
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")
a, sr = librosa.load(output_file)
print(len(a))
