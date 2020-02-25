#!/usr/bin/env python

import os
from flask import Flask, render_template
from daab import DAAB

app = Flask(__name__)
daab = DAAB(os.getenv('DO_TOKEN'), 'waifu.church')

@app.route('/')
def index():
    # Return a list of waifus
    waifus = daab.scan('*')
    return render_template('index.html', waifus=waifus)

@app.route('/<waifu>')
def show_waifu(waifu):
    # Return an image of the waifu
    waifu = daab.get(waifu)
    return render_template('waifu.html', waifu=waifu)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 3:
        waifu = sys.argv[1]
        link = sys.argv[2]

        daab.set(waifu, link)
    else:
        app.run()
