import random
import question_model


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number in range(len(self.question_list))

    def ask_question(self):
        print("")
        question = self.question_list[self.question_number]
        self.question_number += 1

        if isinstance(question, question_model.Mul_Question):
            # Handle multiple choice questions
            options = question.incorrect_answers
            options.append(question.answer)
            random.shuffle(options)

            print(f"Q.{self.question_number}: {question.text} (1, 2, 3, 4): ")

            for i, option in enumerate(options, 1):
                print(f"Option {i}: {option}")

            while True:
                try:
                    user_answer = int(input("Choose your answer(1, 2, 3, 4): "))
                    if 1 <= user_answer <= 4:
                        break
                    print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number between 1 and 4.")

            correct_ans = None
            for i, option in enumerate(options, 1):
                if option == question.answer:
                    correct_ans = i
                    break

        else:
            # Handle True/False questions
            print(f"Q.{self.question_number}: {question.text}")

            while True:
                user_input = input("Enter True/T or False/F: ").lower()
                if user_input in ["true", "t", "f", "false"]:
                    user_answer = user_input
                    break
                print("Please enter either True or False.")

            if question.answer == "True":
                correct_ans: str = ["true", "t"]
            else:
                correct_ans: str = ["false", "f"]

        self.check_answer(user_answer, correct_ans, question)

    def check_answer(self, user_answer, correct_ans, question):

        if isinstance(question, question_model.Mul_Question):
            is_correct = user_answer == correct_ans
        else:
            is_correct = user_answer in correct_ans

        if is_correct:
            print("You got it right ✅")
            self.score += 1
        else:
            print("You got it wrong ❌")

        print(f"The correct answer was: {question.answer}")
        print(f"Current Score: {self.score}/{self.question_number}\n")
