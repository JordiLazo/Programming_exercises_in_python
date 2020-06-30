#Print the index where the word "esther" start(index/find)
print("hola lazo jordi".find("esther"))

#Check if the string "to" is in the given string, print the result
print("no" in "me llamo jordi")

#Replace "lottery" with "board", print the result
print("Yesterday I won the lottery in the lottery".replace("lottery","boat"))

#Replace the caracter "i" with "1" only once, prin the result
print("willy want to win the lottery again".replace("i","1"))
print("willy want to win win the lottery".replace("i","1",3))

#.strip() - Remove spaces from begin and end
print("      this is a cool string    ")
print("      this is a cool string    ".strip())

#"separator".join() - from list to string
print(" ".join ("willy   want to,     win the lottery ".split()))
print("".join ("willy   want to,     win the lottery ".split()))
print(" willy   wants to,   win the lottery  ".split())

#String - Slicing
#"this is a cool string"[start:stop:step]
print("this is a cool string"[3])
print("this is a cool string"[0:10])
print("this is a cool string"[0:10:3].strip())
print("this is a cool string"[7:])

#Exercice
print("I am willy wanka! And I like chocolate!"[5:17].title())

