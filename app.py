from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():

    return '@Team_TDM'

if __name__ == "__newfeatures__":

    app.run()
