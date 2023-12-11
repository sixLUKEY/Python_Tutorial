import random

# User asked for their name
name = input("what is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

#function will choose a random word from list
word = random.choice(words)

print("Guess the characters")

guesses = ''

#Number of turns allowed
turns = 10

while turns > 0:
    #Count the number of times a user has failed
    failed = 0
    
    #All characters from input word, one at a time
    for char in word:
        #Comparing charcater with character in guess
        if char in guesses:
            print(char, end=" ")
            
        else:
            print("_")
            #For every failed attempt, failed gets incremented
            failed += 1
            
    if failed == 0:
        #User will win the game if failure is 0 and 'You Win' will be given as a output
        print("You Win")
        
        #Print correct word
        print("The word is: ", word)
        break

#If user has input the wrong character then it will ask user to input a different character
    print()
    guess = input("guess a character:")
    
    #Every input character will be stored in guesses
    guesses += guess
    
    #Check input with the character in word
    if guess not in word:
        #remove a turn
        turns -= 1
        
        #If character does not match with word then 'wrong' is outputted
        print("Wrong!") 
        
        #Print number of turns left for user
        print("You have", + turns, 'more guesses')       
        
        if turns == 0:
            print("You Lose!")