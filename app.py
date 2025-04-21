# Save as flask_app.py
from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session management

@app.route('/', methods=['GET', 'POST'])
def guess_game():
    # Initialize session variables
    if 'target' not in session:
        session['target'] = random.randint(1, 10)
        session['attempts'] = 0

    message = ""
    game_over = False

    if request.method == 'POST':
        try:
            session['attempts'] += 1
            user_guess = int(request.form['guess'])
            target = session['target']

            if user_guess == target:
                message = f"""
                🎉🎉 Correct! You guessed {user_guess} in {session['attempts']} tries!
                The number was {target}. 
                New game started!
                """
                # Reset game
                session['target'] = random.randint(1, 10)
                session['attempts'] = 0
                game_over = True
            else:
                message = f"❌ {user_guess} is wrong! Try again!, The correct Anwser is ({session['target']})"

        except ValueError:
            message = "⚠️ Please enter a valid number between 1-10!"

    return render_template('index.html', 
                         message=message,
                         game_over=game_over)

if __name__ == '__main__':
    app.run(debug=True)