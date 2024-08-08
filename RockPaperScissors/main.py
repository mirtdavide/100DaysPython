import random
# Rock
rock =("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
choices = [rock, paper, scissors]
user_choice = -1

while(user_choice < 0 or user_choice > 2):
    user_choice = int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors "))


print("You choose: ",choices[user_choice])
computer_choice = random.randint(0,2)

print("Computer choose: ",choices[computer_choice])
print

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice ==2:
    print("You Lose!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw!")
