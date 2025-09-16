from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 10)


@app.route('/')
def hello_world():
    return ('<h1 style=text-align:center>"Guess a number between 0 and 9"</h1> '
            '<img src = https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>')


@app.route('/<int:guess>')
def guessed_number(guess):
    if guess == number:
        return ('<b>"you found me"</b>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    elif guess > number:
        return ('<b>"to high"</b>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<b>"to low"</b>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')


def dec(func):
    def wrapper(*args, **kwargs):
        if args and args[0] > 0:
            return '<b>"sup"<b>'
        else:
            return '<b>"nothing much"<b>'
    return wrapper


@app.route('/temp/<int:a>')
@dec
def temper(a):
    return a


if __name__ == "__main__":
    app.run(debug=True)
