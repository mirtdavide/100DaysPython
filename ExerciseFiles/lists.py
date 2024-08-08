import random
#list tests
#pyhton starts arrays with 0 index
states = ["Delaware","Pennsylvania"]

print(states[0])

#you can also use minus index, it starts with -1 and gets the last item of the list
print(states[-1])

#changing an item inside the list

states[0] = "Software"
print(states[0])


#adding an item
states.append("Hardware")
print(states[-1])

#some other useful methods would be remove(i) insert(i,item) pop() pop([i]) clear() count(item) reverse() copy() sort() extend(list)

#code challenge: who will pay the bill?

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
unlucky_wallet = random.randint(0,4)
print("The friend who will pay for everyone is: ",friends[unlucky_wallet])

#Another solution

print("The friend who will pay for everyone is: ",random.choice(friends))


#length of a list

print(len(friends))

#nestesd lists

fruits = ["watermelon","mango","banana","kiwi"]
veggies = ["broccoli","peppers","zucchini"]

fruits_and_veggies = [fruits,veggies]
print(fruits_and_veggies)
#[0] Selects which list and [2] selects the item of that list, so [0][2] will select the first list and the third item
print(fruits_and_veggies[0][2])
