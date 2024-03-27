# Email Slicer to get the username and domain

email = input("Enter your Email Id: ")
email = email.strip()

username = email[ : email.index('@')]
domain = email[(email.index('@') + 1) : ]

print("Your Username: ", username)
print("Domain: ", domain)