from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    Response,
    make_response,
    send_file,
)
import pandas as pd
import os

addresses = pd.read_csv("data/addresses.csv")

DEBUG = True  # should load this from a config file, ideally
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
    return render_template(
        "home.html", addresses=addresses[:20].to_dict(orient="records")
    )


@app.route("/konrad", methods=["GET"])
def konrad():
    return "Why are you here? Are you missing me? Typing my name into the URL void, hoping I will appear? Honestly, just tag me on discord and I'll be here for you."


@app.route("/test", methods=["GET"])
def test():
    return render_template("test.html")


# get all addresses
@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(addresses.to_dict(orient="records"))


# get image
@app.route("/i/<string:name>", methods=["GET"])
def get_image(name):
    data_url = f"data/images/{name}.png"
    return send_file(data_url, mimetype="image/png")


@app.route("/gallery", methods=["GET"])
def gallery():
    # get all image names in /data/images
    images = [f.split(".")[0] for f in os.listdir("data/images")][: 8 * 8]
    # m
    return render_template("gallery.html", images=images)


if __name__ == "__main__":
    app.run(debug=DEBUG)
