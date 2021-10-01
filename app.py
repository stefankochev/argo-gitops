import flask
from flask import jsonify


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def endpoint():
    return jsonify({"message": "Test Service Update", "version": "v3"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
