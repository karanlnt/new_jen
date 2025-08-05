from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message=" Hello 12 rom Flask on Docker123434444 !")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
