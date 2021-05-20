from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/artem', methods=['GET', 'POST'])
def send():
    message = request.data.decode()
    answer = ''
    if message == 'hi':
        answer = 'hello, im bot'

    elif message == 'bye':
        answer = 'bye, im bot'


if __name__ == "__main__":
    app.run()
