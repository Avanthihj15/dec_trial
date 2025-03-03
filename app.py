from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello')
def hello():
    name = request.args.get('name', 'World')
    return f'<h1>Hello, {name}!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This is a simple Flask application.</p>'

# Run the application
if __name__ == '__main__':
    app.run(Debug=True,port=10000)
