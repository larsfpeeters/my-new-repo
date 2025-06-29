from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Server is running'}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)