from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return '''
    <h1>Welcome to My Flask App</h1>
    <p>Navigate to <a href="/greet">/greet</a> to see something interesting!</p>
    '''

# Greeting route with dynamic user input
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name', 'Stranger')
        return render_template('greet.html', name=name)
    return '''
    <form method="POST" action="/greet">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Greet Me!</button>
    </form>
    '''

# Dynamic content template
@app.route('/about')
def about():
    return '''
    <h1>About This App</h1>
    <p>This is a simple Flask application demonstrating routes, templates, and user input.</p>
    <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
