
def find_highest(dict):
    max = 0
    bidder = ""
    for key in dict:
        bid_amount = dict[key]
        if bid_amount > max:
            max = dict[key]
            bidder = key
    return bidder
print("Welcome to the secret auction")

bidders = {}
answer = "yes"
while answer == "yes":

    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    bidders[name] = bid

    answer  = input("Are there any other bidders? 'yes' or 'no' ")
    print('\n' * 100)
print(f"The winner is : {find_highest(bidders)} ")