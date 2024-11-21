from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Enter Your Name</h1>
    <form method="POST" action="/print_name">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/print_name', methods=['POST'])
def print_name():
    name = request.form.get('name', 'Anonymous')
    return f'''
    <h1>Hello, {name}!</h1>
    <a href="/">Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)

