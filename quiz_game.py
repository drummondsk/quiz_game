from game_data import question_data


class Quiz:
    def __init__(self) -> None:
        score = 0

        pass


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
        print(question_data)

        # game = Quiz()


if __name__ == '__main__':
    main()