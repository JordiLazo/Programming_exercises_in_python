# VARIABLES - Email
# Ask user to inster email address, print the domain of the email
# for example: gmail.com
# willy.wanka@gmail.com

email_address = input("Write your email address: ")
index_of_at = email_address.find("@")
domain = email_address[index_of_at+1:]
print(domain)