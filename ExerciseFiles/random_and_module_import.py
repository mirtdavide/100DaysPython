#random module and module import
import random
import my_module


print(my_module.my_favourite_number)
random_integer = random.randint(1,10)
print(random_integer)

random_number_0_to_1 = random.random() * 10

print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

random_ht = random.randint(0,1)

if(random_ht):
    print("Heads")
else:
    print("Tails")