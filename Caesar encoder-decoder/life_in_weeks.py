def life_in_weeks(your_age):
    remaining_years = 90 - int(your_age)
    remaining_weeks = 52*remaining_years
    print("Hey, you will approximately live "+str(remaining_weeks)+" more weeks, enjoy!")



input_age = input("How old are you?: ")
life_in_weeks(input_age)