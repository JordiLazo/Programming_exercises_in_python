# CONDITIONS - Exceptions
# try / except

try:
    user_age = float(input("Please insert your age: "))
except:
    print("Error, write your name")
    exit()


print("""(1) How many years do I have until retirement?
(2) Can I drink alcohol?
(3) Am I having a middle crisis?
""")
try:
    user_selection = int(input("Please select an option: "))
except:
    print("Error, choose options")
    exit()

if user_selection == 1:
    print(f"You have {67 - int(user_age)} until retirement")
elif user_selection == 2:
    if user_age >= 18:
        print("Yes you can")
    else:
        print("Sorry you can't")
elif user_selection == 3:
    #if user_age >= 40 and user_age <= 45:
    if 40 <= user_age <= 45:
        print("Yes you are in a midlife crisis")
    else:
        print("All is good with you")
else:
    print("Please choose a number between 1 and 3")