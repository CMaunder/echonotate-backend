from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def get_notes():
    return jsonify({"about": "notes go here"})


if __name__ == "__main__":
    app.run()
