import requests
import json
import html

def get_questions(choice):
    if choice.lower() == "t&f":
        response = requests.get('https://opentdb.com/api.php?amount=15&difficulty=easy&type=boolean')
    else:
        response = requests.get('https://opentdb.com/api.php?amount=10&type=multiple')

    if response.status_code == 200:
        data = json.loads(response.text)
        question_data = data["results"]
        
        # Decode HTML entities in questions
        for question in question_data:
            question_text = question["question"]
            decoded_text = html.unescape(question_text)
            question["question"] = decoded_text
            
            # Also decode the correct answer
            correct_answer = question["correct_answer"]
            question["correct_answer"] = html.unescape(correct_answer)
            
            # If it's multiple choice, decode incorrect answers too
            if "incorrect_answers" in question:
                question["incorrect_answers"] = [html.unescape(ans) for ans in question["incorrect_answers"]]
        
        return question_data
    else:
        print("Something Wrong with the API")
        return None
