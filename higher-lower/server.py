import random
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Generate a random number at the start of the server
random_number = random.randint(0, 9)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = int(request.form["number"])
        if user_input == random_number:
            return redirect(url_for('you_are_right'))
        elif user_input < random_number:
            return redirect(url_for('too_low'))
        else:
            return redirect(url_for('too_high'))

    return '''
     <h1 style='text-align:center; color:red;'>Guess a number between 0 and 9</h1>
     <form method="POST" style='text-align:center;'>
         <input type="number" name="number" min="0" max="9">
         <button type="submit">Guess</button>
     </form>
     <div style='text-align:center;'>
         <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
     </div>
    '''


@app.route("/too_low")
def too_low():
    return '''
        <h1 style='text-align:center; color:blue;'>It is too low</h1>
        <div style='text-align:center;'>
            <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" style="height:500px;">
        </div>
        <form action="/" method="get" style='text-align:center;'>
            <button type="submit">Try Again</button>
        </form>
    '''


@app.route("/too_high")
def too_high():
    return '''
        <h1 style='text-align:center; color:purple;'>It is too high!</h1>
        <div style='text-align:center;'>
            <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
        </div>
        <form action="/" method="get" style='text-align:center;'>
            <button type="submit">Try Again</button>
        </form>
    '''


@app.route("/you_are_right")
def you_are_right():
    return '''
        <h1 style='text-align:center; color:green;'>You found me!</h1>
        <div style='text-align:center;'>
            <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
        </div>
    '''


if __name__ == "__main__":
    app.run(debug=True)
