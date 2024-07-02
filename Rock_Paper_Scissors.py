import random


def game():
    r1 = "Rock"
    p1 = "Paper"
    s1 = "Scissor"
    user_pick = str(input("Enter Rock/Paper/Scissor: ").strip().capitalize())
    words = ("Rock", "Paper", "Scissor")
    comp_pick = random.choices(words)
    if user_pick == r1:
        print("User Picked : ", user_pick)
        print("Computer Picked: ", str(comp_pick)) 
        if comp_pick == [r1]:
            print("Tie")
        elif comp_pick == [p1]:
            print("Paper Wins")
        elif comp_pick == [s1]:
            print("Rock Wins")
        else:
            print("Incorrect Input")
    # r1 = "Rock", p1 = "Paper", s1 = "Scissor"
    if user_pick == p1:
        print("User Picked : ", user_pick)
        print("Computer Picked: ", str(comp_pick))
        if comp_pick == [p1]:
            print("Tie")
        elif comp_pick == [r1]:
            print("Paper Wins")
        elif comp_pick == [s1]:
            print("Scissor Wins")
        else:
            print("Incorrect Input")
    # r1 = "Rock", p1 = "Paper", s1 = "Scissor"
    if user_pick == s1:
        print("User Picked : ", user_pick)
        print("Computer Picked: ", str(comp_pick))
        if comp_pick == [s1]:
            print("Tie")
        elif comp_pick == [r1]:
            print("Rock Wins")
        elif comp_pick == [p1]:
            print("Scissor Wins")
        else:
            print("Incorrect Input")

while True:
        response = input("Do you want to play more? (yes/no): ").strip().lower()
        if response == 'yes':
            game()
        elif response == 'no':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
