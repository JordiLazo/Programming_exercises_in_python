import re

string = "'I AM NOT YELLING', she said. Though we knew it to not be true."
print(string)

new_string = re.sub('[A-Z]','',string)
print(new_string)

new_string = re.sub('[a-z]','',string)
print(new_string)

new_string = re.sub('[.,\']','',string)
print(new_string)

new_string = re.sub('[.,\'a-z]','',string)
print(new_string)

new_string = re.sub('[.,\'a-zA-Z]','',string)
print(new_string)

new_string = re.sub('[.,\'A-Z]','',string)
print(new_string)

new_string = re.sub('[.,\'A-Z+" "]','',string)
print(new_string)

string = string + "6 298 - 345"
print(string)

new = re.sub('[0-9]', '', string)
print(new)

new = re.sub('[^0-9]', '', string)
print(new)