#Program that calculates restaurant bill
#takes in the total bill, the number of persons at the table and the tip percentage and gives as output how much each
#person should pay; 

print("Welcome to the tip calculator.")
total_bill=float(input("What was the total bill? $"))
people_number=int(input("How many people to split the bill? "))

tip_percentage=int(input("What percentage tip would you like to give? 10, 12 or 15? "))
while(tip_percentage not in [10,12,15]):
    tip_percentage = int(input("Wrong input,chose a percentage that is 10,12 or 15 "))

total_plus_tip=total_bill + total_bill*(tip_percentage/100)
total_per_person=round(total_plus_tip/people_number,2)
print("Each person should pay: $"+ str(total_per_person))


