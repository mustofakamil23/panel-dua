import panel as pn
# from flask import Flask, render_template
#
# flask_app = Flask(__name__)


# @flask_app.route('/app')
# def hello_world():
#     return render_template("index.html")
#

def panel_app():
    return pn.Column('Hello Panel')  # This Panel app runs alongside flask, access the flask app at [here](./flask/app)"


def user():
    return pn.Column('Ini Halaman Untuk User')


# pn.serve({'/flask': flask_app, '/': panel_app}, port=8080)
pn.serve({"/": panel_app, "user": user})

