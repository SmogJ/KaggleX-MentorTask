import random

words= [
    "apple", "banana", "cat", #"dog", "elephant", "fish",
    ]

def main():
    word= word_gen()
    hangman(word)
    
def word_gen():
    """function that generates random words """
    word= random.choice(words)
    return word

def user_input(word):
    """The Function gets user_input input and compares it to the generated word"""
    guess= str(input(f"The word is a {len(word)} letter word: {'_ '*len(word)} \nGive your best user_input? \n\n")).lower()
    return guess

def validate(word):
    """This is where the comparision takes place"""
    user_word= user_input(word)
    if user_word == word:
        return True
    else:
        return False

     
def hangman(word):
    """here the function handles the number of attempts"""
    vald= validate(word)
    
    attempt_count = 0
    max_attempt = 3
    stick = "||\n"
    
    while True: 
        attempt_count += 1
    
        if vald == False and attempt_count < max_attempt:
            print("GUESSED WRONG, TRY AGAIN ! \n", stick * attempt_count, sep="")
            guess= user_input(word)
        elif vald == False and attempt_count == max_attempt:
            print("GUESSED WRONG, MAX ATTEMPT REACH, TRY AGAIN LATER !\n", stick * max_attempt, sep="")
            break
        else:
            print("GUESSED RIGHT !!! 🏆")
            break
            
                  
main()