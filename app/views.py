__author__ = 'm12sl'

from app import app
from flask import render_template, jsonify, send_from_directory

# just single page application:
@app.route('/')
def index():
    return render_template('index.html')


# api methods
@app.route('/api/<cmd>', methods=['POST'])
def command(cmd=None):
    # todo: add commands if needed
    if cmd in ['right', 'left', 'up', 'down']:
        # todo: add reactions, add some useful response
        return jsonify(status='ok'), 200

    # todo: check error status, add reaction for wrong cmd
    return jsonify(error='unknown command'), 400


# ad hoc, just for fast bower-components addition
# use as {{ url_for('bc_static', filename='xxx') }}" in templates
@app.route('/bc/<path:filename>')
def bc_static(filename):
    return send_from_directory(app.root_path + '/bower_components/', filename)
