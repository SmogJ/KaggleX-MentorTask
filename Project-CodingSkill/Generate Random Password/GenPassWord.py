# Import libraries
import random

# Character set for generating password
characters= [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!" "@", "#", 
    "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", 
    "{", "}", "|", ";", ":", "'"
]

# Define the main, this function request an integer input and outputs a set of strings for the password
def main():
    password= int(input('How long do you want your password?, Enter a Number: ' ))
    str(generate_password(password))
 
# This function is used to generate the password from the character set   
def generate_password(lenght):
    password=''
    for i in random.choices(characters, k=lenght):
        password+=i    
           
    print(password)

    
main()