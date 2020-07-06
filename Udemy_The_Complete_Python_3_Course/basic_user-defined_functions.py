def my_function():
    print("This is my function!")
    print("A second string.")

my_function()

def arguments(str1, str2):
    print(str1)
    print(str2)

arguments("This is argument 1", "This is the second argument which is also a string")
arguments("Stringy", "Hello World ")

def print_something(name, age):
    print("My name is" + name + " and my age is " + str(age) )

print_something("Nick", 27)

def print_something_2(name, age):
    print("My name is",name,"and my age is",age )

print_something_2("Nick", 27)

def print_something_3(name = "Someone", age = "Unknown"):
    print("My name is",name,"and my age is",age )

print_something_3("Nick")