from flask import Flask

www = Flask(__name__)

@www.route('/', methods=['GET'])

def home():
    return "Hello World!"

if __name__ == '__main__':
    www.run()
