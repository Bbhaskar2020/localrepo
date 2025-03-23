def check_vowels(text):
    count = 0
    for i in text:
        if (i in 'aAeEiIoOuU'):
            count += 1
    return count
text=input("Enter the text..")
count=check_vowels(text)
print("Here is the number", count)