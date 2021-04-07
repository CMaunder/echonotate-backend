from flask import Flask, jsonify
import librosa

app = Flask(__name__)


@app.route('/')
def get_notes():
    filename = './2.wav'
    a, sr = librosa.load(filename)
    return jsonify({"lengthOfFile 2.wav": len(a)})


if __name__ == "__main__":
    app.run()
