import sys

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
first_choice=input('You are at a cross road. Where do you want to go?  Type  [left] or [right]\n')
if first_choice == "left" :
    second_choice = input("As you're walking down, you come across a lake. Do you [swim] or [wait]\n")
else:
    print("You get attacked by a bear. Game Over!")
    sys.exit()

if second_choice == "swim":
    print("You got eaten by a shark. Game over!")
    sys.exit()
else:
    third_choice=input(
        "You find a giant wall with 3 doors in different colours. What door do you choose going forward?"
        " [red] [yellow] [blue]\n")

if third_choice == "red":
    print("You open the red door and an anvil falls on you. Game over!")
    sys.exit()
elif third_choice == "blue":
    print(
        "You open the blue door and you find another door behind that door, and another one, and another one... Game over!"
    )
    sys.exit()
elif third_choice == "yellow":
    print("You open the yellow door and you find the golden treasure! You win!")

