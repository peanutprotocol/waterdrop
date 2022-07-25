from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    Response,
    make_response,
)
import pandas as pd

addresses = pd.read_csv("data/addresses.csv")

DEBUG = True
if DEBUG:
    static_folder = "src"
    template_folder = "src"
else:
    static_folder = "dist"
    template_folder = "dist"
app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)
leaderboard = []

# before request redirect to https
@app.before_request
def before_request():
    if request.url.startswith("http://") and not "127.0." in request.url:
        return redirect(request.url.replace("http://", "https://", 301))


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


# home
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", addresses=addresses.to_dict(orient="records"))


@app.route('/konrad', methods=['GET'])
def konrad():
    return 'Hello world!'


# get all addresses
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(addresses.to_dict(orient="records"))


if __name__ == "__main__":
    # change app static folder to "src"

    app.run(debug=DEBUG)
    # app.run(host="
