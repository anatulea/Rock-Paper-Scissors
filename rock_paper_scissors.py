import random

def load_results():
    text_file = open("history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) +", "+ str(t) +", "+ str(l) )
    text_file.close()

results = load_results()

wins = int(results[0])
losses = int(results[1])
ties = int(results[2])

print("Welcome to the Rock, Paper, scissors Game!")
print('Wins: %s, Ties: %s, Losses: %s' %(wins, ties, losses))

# Initializing computer and user choices
computer =random.randint(1,3)
user = int(input('[1] Rock  [2] Paper  [3] Scissors  [9] Quit\n '))

print(computer)
print (user)

#  GAME PLAY LOOP
while not user == 9:
    if user == 1:
        if computer == 1:
            print("Computer chose Rock ... It's a TIE!")
            ties += 1

        elif computer == 2:
            print("Computer chose Paper ... Computer Wins!")
            losses += 1

        else:
            print("Computer chose Scissors ... You WIN!")
            wins += 1


    elif user == 2:
        if computer == 1:
            print("Computer chose Rock ... You WIN!")
            wins += 1

        elif computer == 2:
            print("Computer chose Paper ... It's a TIE!")
            ties += 1

        else:
            print("Computer chose Scissors ... Computer Wins!")
            losses += 1


    elif user == 3:
        if computer == 1:
            print("Computer chose Rock ... Computer Wins! ")
            losses += 1

        elif computer == 2:
            print("Computer chose Paper ... You WIN!")
            wins += 1

        else:
            print("Computer chose Scissors ... It's a TIE!")
            ties += 1
    else:
        print("Please enter a valid number!")     
        
    print('Wins: %s, Ties: %s, Losses: %s' %(wins, ties, losses))
    print("please chose to continue ...")

    computer =random.randint(1,3)
    user = int(input('[1] Rock  [2] Paper  [3] Scissors  [9] Quit\n '))

save_results(wins, ties, losses)
