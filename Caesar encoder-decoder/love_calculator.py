def calculate_love_score(lover1, lover2):
    counter1 = 0
    counter2 = 0
    for letter in lover1:
        counter1 = counter1 + "TRUE".count(letter.upper())

    for letter in lover2:
        counter1 = counter1 + "TRUE".count(letter.upper())

    for letter in lover1:
        counter2 = counter2 + "LOVE".count(letter.upper())

    for letter in lover2:
        counter2 = counter2 + "LOVE".count(letter.upper())
    print("Love score: "+str(counter1)+str(counter2))


calculate_love_score(lover1="Anna", lover2="Gianni")