from flask import Flask
from flask import send_file
from flask_cors import CORS

#python app.py --disable-host-check --host=0.0.0.0

app = Flask(__name__)
CORS(app)

@app.route('/prova')
def prova():
    return send_file('prova.json')

if __name__ == "__main__":
    app.run()