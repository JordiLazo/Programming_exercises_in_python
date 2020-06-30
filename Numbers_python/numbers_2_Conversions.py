#NUMBERS - CONVERSIONS
#int(value)
#float(value)
#str(value)

# 1 - Convert the following to int: 23.7, 2.0, "92.7", "92"
print(int(23.7))
print(int(2.0))
print(int("92"))
#print(int("92.7")) you can not double convert
print(int(float("92.7")))

# 2 - Convert the following to float: 2, "92.7", "92"
print(float(2))
print(float("92.7"))
print(float("92"))
# 3 - Convert the followiwng to string: 23.7, 2
print(str(23.7))
# 4 - Print the type of the following: (2+2.7), (2+2.0), (97-2.0)
# 5 - Print the type of the following: (2+int(2.7)), (str(97) - 2.0)
print(2+int(2.7))
#print(str(97) - 2.0)
print(int(str(97))-2.0)