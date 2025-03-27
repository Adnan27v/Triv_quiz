# Quiz Game

A Python-based quiz game that fetches questions from the OpenTDB API and presents them to the user in a console-based interface.

## Features

- Fetches questions from OpenTDB API
- True/False questions
- Score tracking
- Progress tracking
- HTML entity decoding for proper text display

## Requirements

- Python 3.x
- requests library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/quiz-game.git
cd quiz-game
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the game using:
```bash
python main.py
```

## Project Structure

- `main.py`: Main game loop and user interface
- `data.py`: Handles API data fetching and processing
- `question_model.py`: Question class definition
- `quiz_brain.py`: Game logic and scoring

## License

This project is open source and available under the MIT License. 