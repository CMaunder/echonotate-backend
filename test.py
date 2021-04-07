import librosa

filename = './2.wav'
a, sr = librosa.load(filename)
print(len(a))
