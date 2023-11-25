# modules to use
"""flask (http://flask.pocoo.org/)
twython (https://twython.readthedocs.io/en/latest/)
pytz (https://pypi.python.org/pypi/pytz)
django (https://www.djangoproject.com/)
django-rest-hooks (https://github.com/zapier/django-rest-hooks)
"""
# Designing your own REST APIs
# from flask import Flask, jsonify, make_response, request, abort

# app = Flask(__name__)

# users = [
"""
    {
        'id': 1,
        'username': u'cjgiridhar',
        'email': u'abc@xyz.com',
        'active': True




    },


    {
        'id': 2,
        'username': u'python',
        'email': u'py@py.org',
        'active': False



    }

]


@app.route('/')
def index():
    return 'Hello, python'


@app.route('/v1/users/<int:id>', methods=['GET'])
def get_users(id):
    for user in users:
        if users.get('id') == id:
            return jsonify({'users': user})
        abort(404)


@app.route('/v1/users/', methods=['POST'])
def create_user():
    if not request.json or not 'email' in request.json:
        abort(404)
    user_id = users[-1].get('id')+1
    username = request.json.get('username')
    email = request.json.get('email')
    status = False
    user = {
        'id': user_id,
        'email': email,
        'username': username,
        'active': status

    }
    users.append(user)
    return jsonify({'user': user}), 201


@app.route('/v1/users/<int:id>/', methods=['PUT'])
def update_user(id):
    user = [user for user in users if user['id'] == id]
    user[0]['username'] = request.json.get(
        'username', user[0]['username'])
    user[0]['email'] = request.json.get(
        'email', user[0]['email'])
    user[0]['active'] = request.json.get(
        'active', user[0]['active'])
    return jsonify({'users': user[0]})

@app.route('/v1/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user=[for user in users if user['id']==id]
    users.remove(user[0])
    return jsonify({}), 204
    
    
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)

"""

#