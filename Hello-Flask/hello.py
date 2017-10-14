# Import Flask class from flask module
from flask import Flask

# Create instance of Flask class
app = Flask(__name__)

# Use @app.route() decoratir for creating routes
@app.route('/')

# Function that is executed when index route is requested
def index():
    return '''<h1>Hello World</h1>
<h2>The world is full of mysteries</h2>'''

# Make hello.py run-able
if __name__ == '__main__':
    app.run(debug = True)