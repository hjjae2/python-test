from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "secret"

socket_io = SocketIO(app)


@app.route('/')
def index():
    return "Index"


@app.route('/chat')
def chatting():
    return render_template('chat.html')


@app.route('/chat2')
def chatting2():
    return render_template('chat2.html')


@socket_io.on("message")
def request(message):
    print("message : " + message)
    to = dict()
    if message == 'new_connect':
        to['message'] = "새로운 유저가 난입하였다!!"
        to['type'] = 'connect'
    else:
        to['message'] = message
        to['type'] = 'normal'
        send(to, broadcast=True)


if __name__ == '__main__':
    socket_io.run(app, debug=True, host='0.0.0.0', port=8000)
