from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
app = Flask(__name__) 
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

users = {
    'users_list' :
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job' : 'Janitor',
        },
        {
            'id' : 'abc123',
            'name' : 'Mac',
            'job' : 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name' : 'Mac',
            'job' : 'Professor',
        },
        {
            'id' : 'yat999',
            'name' : 'Dee',
            'job' : 'Aspiring actress',
        },
        {
            'id' : 'zap555',
            'name' : 'Dennis',
            'job' : 'Bartender',
        }
    ]
}

def randGenID():
    string = ""
    
    for x in range(3):
        string += str(random.choice("abcdefghijklmnopqrstuvwxyz"))

    for y in range(3):
        string += str(random.randint(0, 9))
        
    return string

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name') #accessing the value of parameter 'name'
        search_job = request.args.get('job')
        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = randGenID()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd),201
        #resp.status_code = 200 #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                if request.method == 'GET':
                    return user
                elif request.method == 'DELETE':
                    users['users_list'].remove(user)
                    resp = jsonify(success=True),204
                    return resp
        return jsonify('resource not found'), 404
    return users