s = input(" enter a text: ")
reverse = s[:: -1]

if (s==reverse):
    print("yes it's palindrome")
else:
    print("no, it's not a palindrome")