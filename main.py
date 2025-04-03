from data import get_questions
from question_model import TF_Question, Mul_Question
from quiz_brain import QuizBrain

def play_quiz():
    while True:
        choice = input("Enter 'T&F' for True/False or 'Mul' for Multiple Choice (or 'quit' to exit): ").lower()
        
        if choice == 'quit':
            break
            
        if choice not in ['t&f', 'mul']:
            print("Invalid choice. Please enter 'T&F' or 'Mul'")
            continue
            
        question_data = get_questions(choice)
        if not question_data:
            continue
            
        question_bank = []
        
        for question in question_data:
            text = question["question"]
            answer = question["correct_answer"]
            if choice == 'mul':
                incorrect_answers = question["incorrect_answers"]
                question = Mul_Question(text, answer, incorrect_answers)
            else:
                question = TF_Question(text, answer)
            question_bank.append(question)

        quiz = QuizBrain(question_bank)

        while quiz.still_has_questions():
            quiz.ask_question()

        print(f"Thanks for playing the quiz. Final Score = {quiz.score}/{len(question_bank)}\n")
        
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_quiz()