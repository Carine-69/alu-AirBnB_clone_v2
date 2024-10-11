# web application listening on 0.0.0.0. and port 5000
# !/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    app.url_map.strict_slashes = False
