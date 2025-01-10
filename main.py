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
    # Dictionary of valid users and their passwords
    users = {
        'admin': 'password',
        'user1': 'pass123',
        'user2': 'secret'
    }
    
    # Check if username exists and password matches
    if username in users and users[username] == password:
        return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
