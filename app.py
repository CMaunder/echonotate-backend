from flask import Flask, jsonify
import librosa
import os
from os import path
from pydub import AudioSegment
import boto3
from decouple import config

app = Flask(__name__)


@app.route('/predicted-notes/<filename>')
def get_notes(filename):
    BUCKET_NAME_STRING='tabscribe-audio-store'
    #TODO handle wav, m4a
    tempfilename = './tempSoundFiles/tempfilename.mp3'

    s3_client = boto3.client('s3', aws_access_key_id=config('AWS_ACCESS_KEY_ID_TS'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY_TS'))
    s3_client.download_file(BUCKET_NAME_STRING, filename, tempfilename)

    # assign files
    output_file = "./tempSoundFiles/tempfilename.wav"

    # convert mp3 file to wav file
    sound = AudioSegment.from_mp3(tempfilename)
    sound.export(output_file, format="wav")
    a, sr = librosa.load(output_file)
    return jsonify({f"lengthOfFile {filename}": len(a)})


if __name__ == "__main__":
    app.run()
