#### Rock Paper Scissors
import random  
print("Hello. Welocome to Rock Paper Scissors!")
print("")
while True:
    generatedNum = random.randint(0,2)
# Rock = 0, Paper = 1, Scissors = 2
    while True:
        print("Please choose: Rock, Paper, or Scissors!")
        userInput = input("")
        userInput = userInput.lower()
        if userInput == "rock" and generatedNum == 2:
            print("You chose Rock!")
            print("And I chose...")
            print("Scissors! You win!")
            break
        elif userInput == "paper" and generatedNum == 0:
            print("You chose Paper!")
            print("And I chose...")
            print("Rock! You win!")
            break
        elif userInput == "scissors" and generatedNum == 1:
            print("You chose Scissors!")
            print("And I chose...")
            print("Paper! You win!")
            break
        elif userInput == "scissors" and generatedNum == 2:
            print("You chose Scissors!")
            print("And I chose...")
            print("Scissors! Hmm.. seems we've tied.")
            break
        elif userInput == "scissors" and generatedNum == 0:
            print("You chose Scissors!")
            print("And I chose...")
            print("Rock! I win! Take that!")
            break
        elif userInput == "paper" and generatedNum == 1:
            print("You chose Paper!")
            print("And I chose...")
            print("Paper! Hmm.. seems we've tied.")
            break
        elif userInput == "paper" and generatedNum == 2:
            print("You chose Paper!")
            print("And I chose...")
            print("Scissors! I win! Take that!")
            break
        elif userInput == "rock" and generatedNum == 0:
            print("You chose Rock!")
            print("And I chose...")
            print("Rock! Hmm.. seems we've tied.")
            break
        elif userInput == "rock" and generatedNum == 1:
            print("You chose Rock!")
            print("And I chose...")
            print("Paper! I win! Take that!")
            break
        else:
            continue
    print("")       
    print("Good game. Let's play again!")
    print("Hit enter to play again!") 
    input("")