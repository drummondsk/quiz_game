from game_data import question_data
from question_model import Question
from quiz_game import Quiz
import random


def main():
    game_not_over = True
    while game_not_over:
        print("Welcome to my computer quiz game")
        playing = input("Do you want to play? (y/n): ").lower()
        while playing != 'y' and playing != 'n':
            print("Please enter a valid input")
            playing = input("Do you want to play? (y/n): ").lower()
        if playing == 'n':
            exit()
        else:
            print("Okay! Lets play!")
            input("Press Enter to continue...")
            item = 0
            question_bank = []
            question_list = []

            # Loop that will iterate until there all the question in the question_data list has been imported
            while question_data and item < len(question_data):
                # Question order is randomly selected
                rand_ques = random.choice(question_data)

                ques_text = rand_ques['text']
                ques_answer = rand_ques['answer']
                ques_exp = rand_ques['explanation']

                ques_obj = Question(ques_text, ques_answer, ques_exp)
                # Conditional that ensures that questions are not repeated in the question_list
                if ques_text not in question_list:
                    question_list.append(ques_text)
                    question_bank.append(ques_obj)
                    item += 1
                else:
                    continue
        # Creates an instance of the quiz game
        quiz_obj = Quiz(question_bank)
        # Calls the first question of the quiz game
        quiz_obj.get_next_ques()

        # While the user is eligible to receive another question, ask the user a question
        while quiz_obj.is_another_ques():
            quiz_obj.get_next_ques()

            # If the maximum number of questions have been reached then display the user's score in percentage
            if not quiz_obj.is_another_ques():
                percent_score = (quiz_obj.score / 10) * 100
                print(f"Congratulations! Your score is {percent_score}%")
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() == 'y':
                    main()
                else:
                    exit()


if __name__ == '__main__':
    main()
