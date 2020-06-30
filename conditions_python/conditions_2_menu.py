# CONDITIONS - MENU
# Ask user to insert age
# Print the following options menu to the user:
# (1) How many years do I have until retirement? (67 minus user_age)
# (2) Can I drink alcohol? (older than 18)
# (3) Am I having a middle crisis? (between 40 and 45)
# Ask user to select an option
# Print the result according to user selection

user_age = float(input("Please insert your age: "))
print("""(1) How many years do I have until retirement?
(2) Can I drink alcohol?
(3) Am I having a middle crisis?
""")
user_selection = int(input("Please select an option: "))
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