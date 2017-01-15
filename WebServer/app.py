from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('I got a request')
    return 'Hello world'

@app.route('/cakes')
def cakesi():
    return 'YUMMY!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
