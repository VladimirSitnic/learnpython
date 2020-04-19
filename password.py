import getpass
p = getpass.getpass("Enter your passworld:")
if p == "12345":
    print("Good morning!")
else:
    print("Wrong password")