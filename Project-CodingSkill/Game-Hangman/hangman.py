import random

# list of word
words= [
    "apple", "banana", "cat",
    ]
# main function calls the other function
def main():
    word= word_gen()
    attempt(word)
    
def word_gen():
    """function that generates random words """
    word= random.choice(words) # generates random words
    return word


def user_input(word):
    """The Function gets user_input input and compares it to the generated word"""
    guess= str(input(f"The word is a {len(word)} letter word: {'_ '*len(word)} \nGive your best guess? \n\n")).lower() # get input from users
    return guess

def attempt(word):
    """This is where the comparision takes place and handles the number of attempts"""
    guess= user_input(word) # calls and stores the user_input as variable
    
    stick = "||\n" # stick
    
    # Number and count of attempts by users
    limit= 3
    count= 0  
    
    # Makes the comparison of guessed word and random word, and checks the number od attempts
    while count < limit: 
        count +=1
        
        if guess != word and count < limit:
            print("GUESSED WRONG !\n", stick*count, sep="")
            guess = user_input(word)
        elif guess != word and count == limit:
            print(f"CORRECT WORD IS: {word}\nGUESSED WRONG AGAIN, MAX ATTEMPT REACHED, TRY AGAIN LATER !\n", stick*limit, sep="")
            break
        else:
            print("GUESSED RIGHT !!! 🏆")
            break
            
               
main()             