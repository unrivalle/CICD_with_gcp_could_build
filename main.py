import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    someVarFromEnv = os.environ.get('someVar')
    return 'I have changed the text here for testing: {}!\n second line'.format(someVarFromEnv)

if __name__ == "__main__":
    app.debug = True
    app.host='0.0.0.0'
    app.port=int(os.environ.get('PORT', 808'0))
    app.run()
