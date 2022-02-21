import random


class Quiz:

    def __init__(self, questions_list: list):
        self.list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        number = self.question_number
        questions_list = self.list
        user_answer = input(f"Q.{number + 1} : {questions_list[number].question} (True/False)?: ").capitalize()
        if user_answer == questions_list[number].answer:
            self.score += 1
            print(f"You got it right! Your score is {self.score}/{self.question_number + 1}.\n")
        else:
            print(f"Awh, you got it wrong. Your score is {self.score}/{self.question_number + 1}.\n")
        self.question_number += 1


