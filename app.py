from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store messages in memory
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    if name and message:
        messages.append({'name': name, 'message': message})
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)