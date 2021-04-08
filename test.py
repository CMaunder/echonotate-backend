import librosa
import os
from os import path
from pydub import AudioSegment
import boto3
from decouple import config
import jwt

# BUCKET_NAME_STRING='tabscribe-audio-store'
# FILE_NAME_STRING='d-flat-ionian-mode-on-treble-clef.mp3'
# auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja0luZm8iOnsia2V5IjoiY21haiIsInVzZXIiOiJHdWVzdCJ9LCJpYXQiOjE2MTc4NzI5MDAsImV4cCI6MTYxNzg3MzQwMH0.u-OPa2hKQyD2G3jn3YWsI5qxp9WFl5bfgLx2vprQmpA'

# try:
#   payload = jwt.decode(auth_token, 'charliesSecretKey', algorithms=["HS256"])
#   print(payload)
# except jwt.ExpiredSignatureError:
#   print('Signature expired. Please log in again.')
# except jwt.InvalidTokenError:
#   print('Invalid token. Please log in again.')


# tempfilename = './tempfilename.mp3'

# s3_client = boto3.client('s3', aws_access_key_id=config('AWS_ACCESS_KEY_ID_TS'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY_TS'))
# s3_client.download_file(BUCKET_NAME_STRING, FILE_NAME_STRING, tempfilename)

# # assign files
# output_file = "./c-major-scale.wav"

# # convert mp3 file to wav file
# sound = AudioSegment.from_mp3(tempfilename)
# sound.export(output_file, format="wav")
# a, sr = librosa.load(output_file)
# print(len(a))


auth_header = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFja0luZm8iOnsia2V5IjoiYy1tYWpvci1zY2FsZS5tcDMiLCJ1c2VyIjoiR3Vlc3QifSwiaWF0IjoxNjE3OTA1MzY2LCJleHAiOjE2MjMwODkzNjZ9.HKvssp2_owYondAalYAUml5w1EluKspx3kVVlf5eD2E'
if not auth_header:
    print('Missing Token', 403)
auth_token = auth_header.split()[1]
try:
    payload = jwt.decode(auth_token, config(
        'AUTH_JWT_SECRET_KEY'), algorithms=["HS256"])
    print(payload)
except jwt.ExpiredSignatureError:
    print('Signature expired.', 403)
except jwt.InvalidTokenError:
    print('Invalid token.', 403)

# json_payload = json.loads(str(payload))
filename = payload['trackInfo']['key']

BUCKET_NAME_STRING = 'tabscribe-audio-store'
# TODO handle wav, m4a
tempfilename = './tempSoundFiles/tempfilename.mp3'

s3_client = boto3.client('s3', aws_access_key_id=config(
    'AWS_ACCESS_KEY_ID_TS'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY_TS'))
s3_client.download_file(BUCKET_NAME_STRING, filename, tempfilename)

# assign files
output_file = "./tempSoundFiles/tempfilename.wav"

# convert mp3 file to wav file
sound = AudioSegment.from_mp3(tempfilename)
sound.export(output_file, format="wav")
a, sr = librosa.load(output_file)
print(len(a))
