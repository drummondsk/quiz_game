def clear_console():
    """
    Helper function to clear the console to only display one question at a time
    :return: None
    """
    # for windows
    print("\n" * 50)


class Quiz:
    """
    The logic of the quiz game
    """

    def __init__(self, question_list) -> None:
        self.score = 0
        self.question_num = 0
        self.question_list = question_list
        self.max_ques_num = 10
        pass

    def get_next_ques(self):
        """
        Retrieves the questions from the list, asks the user the question then accepts the input
        :return: None
        """
        cur_ques = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"{self.question_num}. {cur_ques.text}? (True/ False): ")
        # Conditional to check that the user answer is equal to the answer value corresponding to the question text
        if user_answer.lower() == cur_ques.answer.lower():
            self.score += 1
            print(f"Correct! Your score is:  {self.score}")
            input("Press Enter to continue...")
            clear_console()
        else:
            print(f"Incorrect! Your score is: {self.score}")
            print(f"{cur_ques.explanation}")
            input("Press Enter to continue...")
            clear_console()

    def is_another_ques(self):
        """
        Checks if the number of questions given is within the maximum limit
        :return: True if another question can be asked
        :return: False if another question cannot be asked
        """
        if self.question_num < self.max_ques_num:
            return True
        else:
            return False
