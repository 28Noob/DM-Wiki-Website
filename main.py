from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    header_py = "home"
    return render_template("index.html", header=header_py)


@app.route("/memento_mori")
def memento_mori():
    header_py = "memento_mori"
    return render_template("memento_mori.html", header=header_py)


@app.route("/violator")
def violator():
    header_py = "violator"
    return render_template("violator.html", header=header_py)


@app.route("/black_celebration")
def black_celebration():
    header_py = "black_celebration"
    return render_template("black_celebration.html", header=header_py)


@app.route("/music_for_the_masses")
def music_for_the_masses():
    header_py = "music_for_the_masses"
    return render_template("music_for_the_masses.html", header=header_py)


@app.route("/some_great_reward")
def some_great_reward():
    header_py = "some_great_reward"
    return render_template("some_great_reward.html", header=header_py)


if __name__ == "__main__":
    app.run(debug=True)
