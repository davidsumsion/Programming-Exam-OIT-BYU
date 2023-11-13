import random

class Game:
    def __init__(self) -> None:
        self.word_list = ['Roman Empire', 'Barbenheimer', 'Ken', 'rudolph', 'ski season is back', 'Christmas', 'gifts', 'Macedonia', 'Go Cougs', 'Go Utes']
        self.word = random.choice(self.word_list)
        self.num_guesses = 0
        self.num_incorrect = 0
        self.printable_man = ''
        self.num_correct = 0
        #number of body parts
        self.num_parts = 8
        self.guessed_letters = []
        self.answered_list = []
        for i in range(len(self.word)):
            self.answered_list.append("_")
        pass
    

    def run(self) -> None:
        while True:
            print(f"\nHello!! \n Welcome to Hangman \n Play at your own risk!\n")
            print(f"length of word: {len(self.word)} characters (including spaces)")
            ##NEED A FEW MORE GUESSES
            while not self.finished():
                #print information for user
                print(f'Correct Letters: {self.list_to_string(self.answered_list)}')
                print(f'Guessed Letters: {self.list_to_string(self.guessed_letters)}')
                print(f'Number of Guesses: {self.num_guesses}')
                print(f'Number of Correct Guesses: {self.num_correct}')
                print(f'Number of Incorrect Guesses: {self.num_incorrect}')

                #get user input
                user_input = None
                while self.valid_input(user_input) == False:
                    print()
                    user_input = input("Guess a Letter: ")
                self.num_guesses += 1
            
                # check input
                correct_letter, index = self.check_input(user_input)
                
                #interpret input
                self.interpret_input(correct_letter, index, user_input)

                #print man 
                print(self.man_to_string())

                #guessed complete word
                if self.finished():
                    break
            
            #play again?
            if input("Try Again?[y] or Quit[any key]: ").lower() != 'y':
                print("Thanks for playing! Have a good day!")
                break

            #Reinitialize function
            indicator: bool = self.reinitialize()
            if indicator == False:
                break
    

    def interpret_input(self, correct_letter: bool, index: int, user_input: str)-> None:
            if correct_letter == True:
                self.update_list(index)
            else:
                self.update_man(user_input)

        
    def reinitialize(self):
        word = self.word
        self.__init__()
        self.word_list.remove(word)
        if self.word_list == []:
            print("Used 10 words from word bank!")
            return False
        self.word = random.choice(self.word_list)
        self.answered_list = []
        for i in range(len(self.word)):
            self.answered_list.append("_")
        return  True
        


    def finished(self) -> bool:
        if '_' in self.answered_list:
            return False
        print('You guessed the entire word')
        if self.num_incorrect >= 8:
            print('YOU LOST')
        else:
            print('YOU WON')
        print(f"You used {self.num_guesses} Gueses")
        return True

      
    def update_man(self, input)-> None:
        print('INCORRECT!')
        self.guessed_letters.append(input)
        self.num_incorrect += 1
        

    def check_input(self, input: str):
        for i, char in enumerate((self.word)):
            if input.lower() == char.lower():
                return True, i
        return False, 0


    def valid_input(self, input):
        if input == None:
            return False
        if input in self.answered_list or input in self.guessed_letters:
            print("  Already Guessed!")
            return False
        if input.isalpha() or input == ' ':
            if len(input) == 1:
                return True
            else:
                print('  Invalid Length!')
                return False
        else:
            print('  Not an Alpha Character!')
            return False 
                   
            
    def update_list(self, index) -> None:
        for i in range(len(self.word)):
            if self.word[i].lower() == self.word[index].lower():
                self.answered_list[i] = self.word[i]
        print("CORRECT!")
        self.num_correct += 1


    def list_to_string(self, lister: list) -> str:
        return_str = ""
        for item in lister:
            return_str += item + " "
        return return_str


        #   ________________            
        #   |              |
        #   |             ...
        #   |             ...
        #   |             /|\
        #   |            / | \
        #   |           /  |  \
        #   |             / \
        #   |            /   \
        #   |         __/     \__
        #   |
        #   |
        # __|_________________________  
    def man_to_string(self)-> str:
        return_str = ""
        #Gallows 
        if self.num_incorrect == 0:
            return_str = f"  ________________\n  |              |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n__|_________________________"
        #head
        elif self.num_incorrect == 1:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n  |\n__|_________________________"
        #torso
        elif self.num_incorrect == 2:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |              |\n  |              |\n  |              |\n  |\n  |\n  |\n  |\n  |\n  |\n__|_________________________"
        #left arm
        elif self.num_incorrect == 3:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\n  |            / |\n  |           /  |\n  |\n  |\n  |\n  |\n  |\n  |\n__|_________________________"
        #right arm
        elif self.num_incorrect == 4:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\ \n  |            / | \ \n  |           /  |  \ \n  |\n  |\n  |\n  |\n  |\n  |\n__|_________________________"
        #left leg
        elif self.num_incorrect == 5:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\ \n  |            / | \ \n  |           /  |  \ \n  |             /\n  |            /\n  |           /\n  |\n  |\n  |\n__|_________________________"
        #right leg
        elif self.num_incorrect == 6:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\ \n  |            / | \ \n  |           /  |  \ \n  |             / \ \n  |            /   \ \n  |           /     \ \n  |\n  |\n  |\n__|_________________________"
        #left foot
        elif self.num_incorrect == 7:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\ \n  |            / | \ \n  |           /  |  \ \n  |             / \ \n  |            /   \ \n  |         __/     \ \n  |\n  |\n  |\n__|_________________________"
        #right foot
        elif self.num_incorrect == 8:
            return_str = f"  ________________\n  |              |\n  |             ...\n  |             ...\n  |             /|\ \n  |            / | \ \n  |           /  |  \ \n  |             / \ \n  |            /   \ \n  |         __/     \__ \n  |\n  |\n  |\n__|_________________________"
        return return_str