from flask import session, redirect, url_for, render_template, request
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
    name = "someone"
    room = "public room"
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)
