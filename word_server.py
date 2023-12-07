
# pip install pyopenssl -> for adhoc to run
from flask import Flask, request

app = Flask(__name__)

@app.route('/taskpane.html', methods=['POST'])
def taskpane():
    data = request.get_json()
    print(data)
    return 'Hello from taskpane.html!'

if __name__ == '__main__':
    app.run(ssl_context='adhoc', host='localhost', port=3000)
