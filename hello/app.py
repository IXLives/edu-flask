from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Success, You've reached the homepage"


@app.route('/<my_name>')
def greetings(my_name):
    return 'Welcome, ' + my_name + '!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
