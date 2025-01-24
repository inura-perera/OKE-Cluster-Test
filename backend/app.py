from flask import Flask

app = Flask(__name__)

@app.route('/api')
def api():
    return "Hello from the Backend!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)