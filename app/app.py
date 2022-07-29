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
import random

################################################################################
addresses = pd.read_csv("data/addresses.csv")
addresses_list = addresses.iloc[:, 0].tolist()
contractAddress = "0x8d1a17A3A4504aEB17515645BA8098f1D75237f7"
################################################################################


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
        "home.html",
        addresses=addresses[:40].to_dict(orient="records"),
        addresses_list=addresses_list,
        contractAddress=contractAddress,
    )


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

    images = [f.split(".")[0] for f in os.listdir("data/images")]
    # get 64 random images
    images = random.sample(images, 64)
    # m
    return render_template(
        "gallery.html",
        images=images,
        addresses_list=addresses_list,
        contractAddress=contractAddress,
    )


@app.route("/mint", methods=["GET"])
def mint():
    return render_template(
        "mint.html", addresses_list=addresses_list, contractAddress=contractAddress
    )


if __name__ == "__main__":
    app.run(debug=DEBUG)
    # app.run(debug=False)
