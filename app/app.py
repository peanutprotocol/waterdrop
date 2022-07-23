from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    redirect,
    Response,
    make_response,
)

app = Flask(__name__, static_folder="dist", template_folder="dist")
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
    return render_template("home.html")

# get all addresses
@app.route("/leaderboard", methods=["GET"])
def get_data():
    return jsonify(leaderboard)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host="