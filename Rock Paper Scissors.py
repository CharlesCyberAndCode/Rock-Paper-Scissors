#### Rock Paper Scissors
import random  
wins = 0
losses = 0
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
            print("You chose Rock! " "And I chose... " "Scissors! You win!")
            wins = wins + 1
            break
        elif userInput == "paper" and generatedNum == 0:
            print("You chose Paper! " "And I chose... " "Rock! You win!")
            wins = wins + 1
            break
        elif userInput == "scissors" and generatedNum == 1:
            print("You chose Scissors! " "And I chose... " "Paper! You win!")
            wins = wins + 1
            break
        elif userInput == "scissors" and generatedNum == 2:
            print("You chose Scissors! " "And I chose... " "Scissors! Hmm.. seems we've tied.")
            break
        elif userInput == "scissors" and generatedNum == 0:
            print("You chose Scissors! " "And I chose... " "Rock! I win! Take that!")
            losses = losses + 1
            break
        elif userInput == "paper" and generatedNum == 1:
            print("You chose Paper! " "And I chose... " "Paper! Hmm.. seems we've tied.")
            break
        elif userInput == "paper" and generatedNum == 2:
            print("You chose Paper! " "And I chose... " "Scissors! I win! Take that!")
            losses = losses + 1
            break
        elif userInput == "rock" and generatedNum == 0:
            print("You chose Rock! " "And I chose... " "Rock! Hmm.. seems we've tied.")
            break
        elif userInput == "rock" and generatedNum == 1:
            print("You chose Rock! " "And I chose... " "Paper! I win! Take that!")
            losses = losses + 1
            break
        else:
            continue
    print("Good game!")
    print("")
    print("Would you like to see how many times you've won and lost against me?")
    print("Type yes to see history. Hit enter to skip and play again.")
    history = input("")
    history = history.lower()
    if history == "yes":
        print(f"You have won against me {wins} times.")
        print(f"You have lost against me {losses} times.") 
        print("")
    