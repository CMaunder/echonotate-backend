from flask import Flask, jsonify
import librosa

app = Flask(__name__)


@app.route('/')
def get_notes():
    filename = './c-major-scale.mp3'
    a, sr = librosa.load(filename)
    return jsonify({"lengthOfFile": len(a)})


if __name__ == "__main__":
    app.run()
