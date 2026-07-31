# Flask Number Guessing Game

A simple Flask web application where users guess a random number between **0** and **9** by entering it in the URL. The app responds with hints and animated GIFs until the correct number is guessed.

## Features

- Built with Flask
- Dynamic URL routing
- Random number generation
- Color-coded responses
- Animated GIF feedback
- Simple and interactive web game

## Technologies

- Python
- Flask

## Setup

1. Clone the repository.

2. Install the required dependency:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python server.py
```

4. Open your browser and visit:

```
http://127.0.0.1:5000/
```

5. Guess a number by adding it to the URL. For example:

```
http://127.0.0.1:5000/5
```

## Project Structure

```
.
├── server.py
├── requirements.txt
└── README.md
```

## How It Works

- When the server starts, it randomly selects a number between **0** and **9**.
- Visit the home page to see the game instructions.
- Enter your guess in the URL.
- The app tells you whether your guess is:
  - Too high
  - Too low
  - Correct
- A matching GIF is displayed for each response.

## Requirements

- Python 3.14
- Flask