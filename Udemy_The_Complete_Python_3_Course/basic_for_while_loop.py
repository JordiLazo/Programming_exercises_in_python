numbers = [1,2,3,4,5]
number2 = ["Nick", "Someone","Another Person"]

for item in numbers:
    print(item)

for item in number2:
    print(item)

for item in number2:
    print("This person name is", item)

run = True
current = 1

while run:
    if current == 100:
        run = False
    if not current == 100:
        print(current)
        current += 1

while run:
    if current == 100:
        run = True
    else:
        print(current)
        current += 1