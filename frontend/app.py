from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Call the backend API
    backend_response = requests.get('http://backend-service/api')
    return render_template('index.html', backend_data=backend_response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
