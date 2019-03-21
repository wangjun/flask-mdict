
import os.path

from flask import Flask, redirect, url_for


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "jfdsafn219jdf924j.dfsu12jf294"

    # mdict directory
    app.config["MDICT_DIR"] = 'content'
    # css/png/jpg file are cached in memory
    app.config["MDICT_CACHE"] = False

    # fix blueprint directory
    import sys
    sys.path.append(os.path.dirname(os.path.abspath('')))

    import mdict
    mdict.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return redirect(url_for('mdict.query_word2'))


@app.route('/favicon.ico')
def favicon_ico():
    return redirect(url_for('static', filename='logo.png'))
