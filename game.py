import random

class Game:
    def __init__(self) -> None:
        ### ADD 10 words , 'Ken', 'lovely', 'Chewsday', 'Volkl', 'Utah Utes', 'Skiing', 'BYU'
        self.word_list = ['Roman Empire']
        self.word = random.choice(self.word_list)
        self.num_guesses = 0 
        pass

    def run(self) -> None:
        print(f"Hello!! \n Welcome to Hangman \n Play at your own risk!")
        while self.num_guesses < len(self.word):
            print('ok')
            


