__author__ = 'm12sl'

from app import app
from flask import render_template, jsonify

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/<cmd>', methods=['POST'])
def command(cmd=None):
    if cmd in ['right', 'left', 'up', 'down']:
        return jsonify(status='ok'), 200

    return jsonify(error='unknown command'), 400
