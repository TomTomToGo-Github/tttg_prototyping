"""https://www.youtube.com/watch?v=7LNl2JlZKHA"""
from flask import Flask, request, jsonify

app = Flask(__name__)

## Attention: As long as this global dictionary is not overwritten all functions can retrieve
# and add data and have the same copy of the dictionary -> better solution is to use a database
MEMBERS_DICT = {"list_of_members": ["Member1", "Member2", "Member3"]}

@app.route("/get_members")
def get_members():
    print("\n\nReturning current members:", MEMBERS_DICT)
    return MEMBERS_DICT

@app.route("/reset_members", methods=['GET'])
def reset_members():
    MEMBERS_DICT["list_of_members"] = ["Member1", "Member2", "Member3"]
    print("\n\nResetting and returning members:", MEMBERS_DICT)
    return MEMBERS_DICT

@app.route('/add_member', methods=['POST'])
def add_member():
    # Retrieve the data from the request
    new_member = request.json.get('new_element')
    print("\n\nCurrent members:", MEMBERS_DICT)
    print("Adding new member", new_member)
    MEMBERS_DICT['list_of_members'].append(new_member)
    return MEMBERS_DICT # jsonify(message='Member added successfully')


if __name__ == "__main__":
    app.run(debug=True)