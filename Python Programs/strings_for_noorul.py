"""
Rock, Paper, Scissors
April 3rd, 2020
"""

#Safe variables
player_points = 0
computer_points = 0
play_again = "yes"

import random

print("Welcome to rock, paper, scissors!\n")

#Instructions
while True:
    answer=input("Do you know how to play? (yes/no): ")
    if answer=="no":
        print ("hi")#instructions
        break
    elif answer!="no" and answer!="yes":
        print("Invalid answer")
    else:
        break

while play_again=="yes":
    #nb. of rounds
    while True:
        try:
            rounds=int(input("How many rounds would you like to play? (1-10): "))
        except ValueError:
            print("Invalid answer")
        else:
            if rounds>10 or rounds<1:
                print("Invalid answer")
            else:
                break

    #Match
    for i in range(rounds):
        while True:
            print("\nRound",(i+1))
            choice=input("Rock, paper or scissors? ")
            one=input("1..")
            two=input("2..")
            three=input("3!")
            choices = ["rock", "paper", "scissors"]
            reply=random.choice(choices)
            print("You: "+choice+"\nComputer: "+reply)
            if reply==choice:
                print("Tie! Nobody gets points...\nPlayer:",player_points,"Computer",computer_points)
                break
            elif (choice=="rock" and reply=="scissors") or (choice=="scissors" and reply=="paper") or (choice=="paper" and reply=="rock"):
                player_points = player_points + 1
                print("You won!\nPlayer:",player_points,"Computer:",computer_points)
                break
            elif (choice=="rock" and reply=="paper") or (choice=="scissors" and reply=="rock") or (choice=="paper" and reply=="scissors"):
                computer_points = computer_points + 1
                print("You lost this one..\nPlayer:",player_points,"Computer:",computer_points)
                break
            else:
                print("Spelling mistake? Here, try again: ")
                continue

    #Total points
    print("\nTotal points: \n\nPlayer:",player_points,"Computer:",computer_points)
    if player_points>computer_points:
        print("\nCongratulations, You won the game!")
    elif computer_points>player_points:
        print("Aww you lost the game...")
    elif player_points==computer_points:
        print("It's a tie for this game!")

    #Play again?
    while True:
        play_again=input("Play again? (yes/no): ")
        if play_again=="yes" or play_again=="no":
            break
        else:
            print("Invalid answer")

print("\nThank you for playing!")
