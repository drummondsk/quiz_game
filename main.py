from game_data import question_data
from question_model import Question
from quiz_game import Quiz
import random



def main():
    print("Welcome to my computer quiz game")
    playing = input("Do you want to play? (y/n) ").lower()
    while playing != 'y' and playing != 'n':
        print("Please enter a valid input")
        playing = input("Do you want to play? (y/n) ").lower()
    if playing == 'n':
        exit()
    else:
        print("Okay! Lets play!")
        item = 0
        question_bank = []
        while question_data and item < len(question_data):
            # rand_ques = random.choice(question_data)
            ques_item = question_data[item]

            ques_text = ques_item['text']
            ques_answer = ques_item['answer']

            test_q = Question(ques_text, ques_answer)
            question_bank.append(test_q)

            item += 1

        q_can = Quiz(question_bank)
        q_can.next_q()

        while q_can.another_q():
            q_can.next_q()


if __name__ == '__main__':
    main()

