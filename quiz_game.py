import random

from game_data import question_data


class Quiz:
    def __init__(self, question_list) -> None:
        self.score = 0
        self.question_num = 0
        self.question_list = question_list
        pass

    def next_q(self):
        first_q = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"{self.question_num}. {first_q.text}? (True/ False): ")
        if user_answer.lower() == first_q.answer.lower():
            self.score += 1
            print(f"Correct! Your score is:  {self.score}")
        else:
            print(f"Incorrect! Your score is: {self.score}")


    def another_q(self):
        if self.question_num < len(self.question_list):
            return True
        else:
            return False


