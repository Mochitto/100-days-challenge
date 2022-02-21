from question_model import Question
from data import question_data
from quiz_brain import Quiz
import random

# Creates the questions list and randomizes it
question_bank = []
for dictionary in question_data:
    question = dictionary["question"]
    answer = dictionary["answer"]
    question_bank.append(Question(question, answer))
random.shuffle(question_bank)

quiz = Quiz(question_bank)
# Main loop
for question_number in range(len(question_bank)):
    quiz.next_question()
print(f"Thank you for playing! Your final score is {quiz.score}")
