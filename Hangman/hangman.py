import random

#Open File
words_file = open("words.txt", "r")
data = words_file.read()
#Split the string based on newline occurence and create a list
words_list = data.split("\n")
#Close File
words_file.close()

#Choose a random word from the list
word = random.choice(words_list)
print(word)
placeholder = ""
for position in range(len(word)):
    placeholder += "_"
print(placeholder)

placeholder = list(placeholder)
game_over = False

lives = 6
print(placeholder)
correct_letters = []
while not game_over :

    input_letter = (input("Give me a letter: ")).lower()
    if len(input_letter) > 1:
        if input_letter == word:
            game_over = True
            print("Correct, you won!")
        else:
            lives -= 1
            print("Bad Guess, remaining lives " + str(lives) + "/6")

    else:
        if input_letter in correct_letters:
            print("You already said that letter!")
        else:
            found = False
            for i in range(len(word)):
                if word[i] == input_letter:
                    found = True
                    placeholder[i]= input_letter
            if found:
                print("Correct Guess")
                correct_letters.append(input_letter)
            else:

                lives-=1
            print("Bad Guess, remaining lives " + str(lives) + "/6")

        print(placeholder)
        if lives == 0 or "_" not in placeholder:
            game_over = True
            print("Game over!")



