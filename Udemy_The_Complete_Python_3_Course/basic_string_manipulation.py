string_1 = "Hello, " + "Nick"
print(string_1)

string_2 = "H"+ "e" + "l" + "l" + "o"
print(string_2)

string_3 = "This cost " + str(6) + " buck"
print(string_3)

string_4 = "This cost " + str(6+5) + " dollars"
print(string_4)

string_5 = "Hello:Nick:World"
print(string_5.split(":"))

string_6 = "My name is: " + "Hello:Nick:World".split(":")[1]
print(string_6)