from game_data import question_data
from question_model import Question
import random

for item in range(len(question_data)):
    rand_ques = random.choice(question_data)
    ques_item = question_data[item]
    ques_text = rand_ques['text']
    ques_answer = rand_ques['answer']
    print(ques_text, ques_answer)
    test_q = Question(ques_text, ques_answer)
