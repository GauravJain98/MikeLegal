from flask import Flask, render_template, redirect, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from convert import htmlTokentize
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a02f6b6f061fb082059c'
socketio = SocketIO(app)

# Socket messages

@socketio.on('joined', namespace='/chat')
def joined(message):
    room = "Public Room"
    join_room(room)
    emit('status', {'msg': "someone" + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = "Public Room"
    if "tokenize" == message['msg'].split(" ")[0]:
        message['msg'] = htmlTokentize(" ".join(message['msg'].split(" ")[1:]))
    emit('message', {'msg':  session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = "Public Room"
    leave_room(room)
    emit('status', {'msg': "someone" + ' has left the room.'}, room=room)

# Routes 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def indexPost():
    session['name'] = request.form['name']
    return redirect("/chat")

@app.route('/chat', methods=['GET'])
def chat():
    name = session.get('name')
    room = "Public Room"
    return render_template('chat.html', name=name, room=room)

if __name__ == '__main__':
    socketio.run(app)
    # app.run()