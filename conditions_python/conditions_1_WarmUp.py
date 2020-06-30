# CONDITIONS - Warm Up

"""exp1 = True
exp2 = True
if exp1 and exp2:
    print("Both exp are correct")
else:
    print("Not all expressions are True")
"""
full_name = input("Enter your name: ")
if "willy" in full_name.lower():
    print("Its ok")
elif "umpa" in full_name.lower() or "oompa" in full_name.lower():
    print("Umpa or oompa is in this sentence")
else:
    print("Wrong name")