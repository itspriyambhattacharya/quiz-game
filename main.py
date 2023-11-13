from question_model import *
from data import *
from quiz_brain import *

question_bank = []  # A list which will store the objects of the Question class

for i in question_data:
    text = i['question']
    answer = i['correct_answer']
    question = Question(text, answer)  # Creating an object of the question class
    question_bank.append(question)  # Creating a list containing objects of the Question class

quiz = QuizBrain(question_bank)  # An object of QuizBrain class

while quiz.still_has_next_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
