import librosa

filename = './c-major-scale.mp3'
a, sr = librosa.load(filename)
print(len(a))
