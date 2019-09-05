from flask import Flask
import logging


app = Flask(__name__)

@app.route('/test/')
def test():
    return 'rest'

@app.route('/honeypot/')
def test1():
    1/0
    return 'lol'

if __name__ == '__main__':
    app.run()
