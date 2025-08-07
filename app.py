from flask import (
    Flask, 
    render_template,
    redirect,
    url_for,
    jsonify, 
    request,
    flash
)
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def entrar_chat():
    if request.method == 'POST':
        nomeChat = request.form.get('nome')
        
        if not nomeChat or nomeChat == None:
            return redirect(url_for('index'))
        
        return redirect(url_for('chat', nome=nomeChat))
    

@app.route('/chat', methods=["GET"])
def chat():
    nomeUser = request.args.get('nome')
    return render_template('chat.html')


# Eventos do WebSocket
@socketio.on('connect')
def connect():
    pass

@socketio.on('disconnect')
def disconnect():
    pass




if __name__ == "__main__":
    socketio.run(app, debug=True)
