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
print_something_3(27)
print_something_3(age = 27)
print_something_3(age = 27, name = "Nick")

def print_people(*people):
    for person in people:
        print("This person is", person)

print_people("Nick","Dan","Jack","King","Smiley")

def do_math(num1,num2):
    return num1 + num2

math1 = do_math(9,2)
math2 = do_math(11,34)
print("First sum is", math1, "and the second sum is", math2)