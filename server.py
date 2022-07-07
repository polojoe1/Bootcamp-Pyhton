import imp
from flask import Flask

app=Flask(__name__)

@app.route('/')

def hello():
    return 'hello world!'

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def name(name):
    return (f'hi {name}')

@app.route('/repeat/<int:nums>/<input>')

def repeat(nums, input):
    return (input + ' ') * nums

if __name__=='__main__':
    app.run(debug=True)