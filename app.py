from flask import Flask, jsonify, request
import librosa
import os
from os import path
from pydub import AudioSegment
import boto3
from decouple import config
import jwt
app = Flask(__name__)


@app.route('/predicted-notes')
def get_notes():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return 'Missing Token', 403
    auth_token = auth_header.split()[1]
    try:
        payload = jwt.decode(auth_token, config(
            'AUTH_JWT_SECRET_KEY'), algorithms=["HS256"])
        print(payload)
    except jwt.ExpiredSignatureError:
        return 'Signature expired.', 403
    except jwt.InvalidTokenError:
        return 'Invalid token.', 403

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
    return jsonify({f"lengthOfFile": len(a)})


if __name__ == "__main__":
    app.run(debug=True)
