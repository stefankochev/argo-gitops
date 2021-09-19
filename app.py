import flask


app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def endpoint():
    return "Test Service Update"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
