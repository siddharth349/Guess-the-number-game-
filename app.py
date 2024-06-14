from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    if request.method == 'POST':
        guess = int(request.form['guess'])
        session['attempts'] += 1

        if guess < session['number']:
            message = "Too low!"
        elif guess > session['number']:
            message = "Too high!"
        else:
            message = f"Correct! The number was {session['number']}. Attempts: {session['attempts']}"
            session.pop('number', None)  # Reset the game

        return render_template('index.html', message=message)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
