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

while not game_over :
    correct_letters = []
    input_letter = (input("Give me a letter: ")).lower()

    if input_letter in correct_letters:
        print("You already said that letter!")
    else:
        if input_letter in word:
            for letter in word:
                if letter == input_letter:
                    placeholder[word.index(letter)] = input_letter
                    correct_letters.append(letter)
        else:
            lives = lives -1
    print(placeholder)
    if lives == 0 or "_" not in placeholder:
        game_over = True
        print("Game over!")



