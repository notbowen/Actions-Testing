from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    username = request.form['username']
    password = request.form['password']

    if login_helper(username, password):
        return 'Login successful!'
    else:
        return 'Login failed!'

def login_helper(username: str, password: str):
    user_pairs = {
        'admin': 'password',
        'user1': 'password1',
    }

    if username in user_pairs and user_pairs[username] == password:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run(debug=True)
