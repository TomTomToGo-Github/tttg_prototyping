# prototyping
random codes for test furposes



appium info;
https://www.youtube.com/watch?v=x-hBpgM5je8&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=3

install node

npm install -g appium


start server -> appium



appium driver install --source=npm appium-windows-driver

appium driver list --installed

## full stack  commandline
mkdir full_stack
mkdir full_stack\flask_server
touch full_stack\flask_server\server.py
npx create-react-app client
py -m venv .venv
.venv\Scripts\activate

pip install flask

write into python file:
from flask import Flask

app = Flask(__name__)

@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)


cd full_stack
py flask_server\server.py

open browser in localhost:5000/members


go to frontnd delete app-test, index.css and logo
then in package.json add 
  "proxy": "http://localhost:5000",