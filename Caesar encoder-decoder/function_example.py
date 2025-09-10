def greet():
    print("Hello!")
    print("How do you do?")
    print("Isn't the weather nice?")



def greet_name(name, location):
    print("Hello " + str(name)+"!")
    print("How do you do " + str(name)+"?")
    print(str(name) + " isn't the weather nice here in " + str(location)+"?")
greet()
greet_name("Berlusconi","Milano")
greet_name(name="Berlusconi",location="Milano")

