from flask import Flask, jsonify
import librosa
from pydub import AudioSegment

app = Flask(__name__)


@app.route('/')
def get_notes():
    # assign files
    input_file = "./c-major-scale.mp3"
    output_file = "./c-major-scale.wav"

    # convert mp3 file to wav file
    sound = AudioSegment.from_mp3(input_file)
    sound.export(output_file, format="wav")
    a, sr = librosa.load(output_file)
    return jsonify({"lengthOfFile 2.wav": len(a)})


if __name__ == "__main__":
    app.run()
