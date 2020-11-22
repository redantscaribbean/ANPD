from flask import Flask, request, render_template
from flask_socketio import SocketIO, send

# in this file we will publish the results to all the necessary frontend interfaces.

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
app.config['SECRET_KEY'] = 'secret!'


@app.route('/PublishResults', methods=['POST'])
def publishResults():
    input_json = request.get_json(force=True)
    print(input_json)
    socketio.send(input_json, broadcast=True)
    return "ok"

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000)