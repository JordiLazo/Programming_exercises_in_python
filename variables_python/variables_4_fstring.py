# VARIABLES - fstring, python 3.6 and above
# combine variables in a string

# Get number from user, multiply by 2 and print MEANINGFUL output
num = int(input("Write a number: "))
num = num * 2
num2 = 21
#print("your number got multuplied by 2, the result is:", num, "I am", num2, "old")
#msg = "your number got multuplied by 2, the result "+ str(num)
msg = f"your number got multuplied by 2, the result is: {num + 1}"
print(msg)