import os
import random
FRUITS_FILE='fruits.txt'

def get_a_sentence():
    file_path = os.path.abspath(__file__)
    directory = os.path.dirname(file_path)
    fruits_file_path = os.path.join(directory , FRUITS_FILE)

    with open(fruits_file_path) as f:
       return random.choice(f.readlines()).rstrip()


def guesser(guess_word,word,mistake_value):
    
    if mistake_value in range(1,6):
        if '_' in guess_word:
            print(f'Guess the word.{mistake_value} mistakes left',guess_word) 
            letter=input("Guess a letter: ")

            if letter not in word:
                guesser(mistake_value-1,guess_word,word)

            else:
                def letter_count(word): # այս ֆունկցիան հաշվում է թե քանի հատ կա այդ տառից բառի մեջ ու տեղադրում է դրանք '_'-երի փոխարեն
                    count=word.count(letter)
                    if count>0:
                        index=word.index(letter) 
                        guess_word_1=list(guess_word) 
                        guess_word_1[index]=letter
                        guess_word_1=''.join(guess_word_1)
                        count-=1
                        letter_count(word[index:])

                    guesser(mistake_value,guess_word_1,word)
                letter_count(word)
                

        else: 
            print('You won the game') 
            
    else:
        print("you lose the game")

def main(): # ստեղ խնդիրներ առաջացան , բայց չեմ կարողացել լուծել դրանք
    word = get_a_sentence() # ուզում էի random ընտրած բառը(word) փոխանցել guesser ֆունկցիային
    guess_word=len(word)*'_'
    guesser(5,guess_word,word)

if __name__ == '__main__':
    main()   