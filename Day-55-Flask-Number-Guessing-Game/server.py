from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
    "<img src='https://images.squarespace-cdn.com/content/v1/55b3b4afe4b0a813f74ebbd8/1548601200418-B4WV6BACDMPF2W67BBP5/ALL_4.gif?format=1500w'>"

random_int = random.randint(0, 9)

@app.route('/<int:guess>')
def guessed_num(guess):
    if guess>random_int:
        return "<h1 style='color:purple'>Too high,try again!</h1>" \
        "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTJybzNyOHVvcWF4cXEwaDZnYXZndzg2ZGxmcGNhb2RpcWg1OHVpdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/61374X6M1XFHJmWYJG/giphy.gif'>"
    elif guess<random_int:
        return "<h1 style='color:red'>Too low,try again!</h1>" \
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXBobHJlMXZuaXR1eWNoNHFlemR4bTh2dGpzMGUxcG5ra3l3ZzNldiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/WQ2IwyAgYlmU0/giphy.gif'>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXBobHJlMXZuaXR1eWNoNHFlemR4bTh2dGpzMGUxcG5ra3l3ZzNldiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wtqEhmpTMmjRK/giphy.gif'>"

if __name__=="__main__":
    app.run(debug=True)