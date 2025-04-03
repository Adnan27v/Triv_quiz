# Quiz Game

A Python-based quiz game that fetches questions from the OpenTDB API and presents them to the user in a console-based interface. The game supports both True/False and Multiple Choice questions.

## Features

- Fetches questions from OpenTDB API
- Two quiz modes:
  - True/False questions
  - Multiple Choice questions
- Score tracking
- Progress tracking
- HTML entity decoding for proper text display
- Option to replay the quiz
- Dynamic question bank based on selected mode

## Requirements

- Python 3.x
- requests library (for API calls)

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

1. Run the game using:
```bash
python main.py
```

2. Choose your preferred quiz mode:
   - Enter 'T&F' for True/False questions
   - Enter 'Mul' for Multiple Choice questions
   - Enter 'quit' to exit the game

3. Answer the questions and track your score

4. After completing the quiz, you can choose to play again with a different mode

## Project Structure

- `main.py`: Main game loop and user interface
- `data.py`: Handles API data fetching and processing
- `question_model.py`: Question class definitions (TF_Question and Mul_Question)
- `quiz_brain.py`: Game logic, scoring, and question handling

## How It Works

1. The game fetches questions from the OpenTDB API based on the selected mode
2. Questions are processed and stored in a question bank
3. The quiz brain handles the game flow, scoring, and question presentation
4. Users can switch between True/False and Multiple Choice modes
5. Final scores are displayed after each round

## License

This project is open source and available under the MIT License. 