from flask import Flask,render_template
from flask_socketio import SocketIO
app = Flask(__name__)

socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('modify')
def modify_file(msg):
    with open('file.txt','w+') as f:
        f.write(msg.get('data'))
        socketio.emit('server_response',{'data':msg.get('data')})
        f.close()

@socketio.on('connect')
def init_msg():
    with open('file.txt','r') as f:
        socketio.emit('server_response',{'data':f.read()})
        print('初始化~~~~~')
        f.close()

if __name__ == '__main__':
    socketio.run(app,port=5000,debug=True)
