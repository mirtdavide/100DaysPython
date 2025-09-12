dictionary_example = {
    "Key1" : "Value for key 1",
    "Key2" : "Value for key 2",
    "Key3" : "Value for key 3"
}

print(dictionary_example["Key1"])

dictionary_example["Key4"] = "Value for key 4"
dictionary_example["Key3"] = "New Value for key 3"
print(dictionary_example["Key4"])
print(dictionary_example["Key3"])

empty_dictionary = {}

#looping dictionary
for key in dictionary_example:
    print(key)
    print(dictionary_example[key])


capitals = {

    "France" : "Paris",
    "Germainy" : "Berlin"
}

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : []
}



print(travel_log["France"][0])


example_nested = {
    "Key1" : ["value1",["value2","value3"]]
}


print(example_nested["Key1"][1][0])

travel_log2 = {
    "France" : {"Cities": ["Paris"]},
    "Germany" : []
}

print(travel_log2["France"]["Cities"][0])

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

for key in dict:
    dict[key] += 1
    print(dict[key])

#dict[1] = 5

dict["c"] = [1,2,3,4]