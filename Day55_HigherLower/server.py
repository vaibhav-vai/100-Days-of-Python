from flask import Flask
import random

random_number = random.randint(0,9)
print(random_number)
app = Flask(__name__)

@app.route("/")
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:number>")
def guess_number(number):
    if number > random_number:
        return ('<h1 style="color: purple">Too High, Try Again!</h1>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXBlMHRmbWpjaWtrNmRiNnU0dzN0cHdxb2dpYmM5Z2N4YjJldHJoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J3AoXNNJPXBRu/giphy.gif"/>')
    elif number < random_number:
        return ('<h1 style="color: red">Too Low, Try Again!</h1>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGlmN3ZmbWN6cDFxOTEyOGducTliYm05NWtjNTdiajQxZDlqbDZqOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKJkUIgrWrJdOWA/giphy.gif"/>')
    else:
        return ('<h1 style="color: green">You Found Me!</h1>'
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXFqeDlzYXgzMWJ4MW5waXhzamZrbTFwcXFzZG41MTI3d211ajR3dyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYB0aJJ0hQ230WI/giphy.gif"/>')

if __name__ == "__main__":
    app.run()