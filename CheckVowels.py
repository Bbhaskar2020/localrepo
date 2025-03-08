def vowels(text):
    count = 0
    for character in text:
        if character in ("aAeEiIoOuU"):
            count += 1
    return count
text = input("Text is: ")
count = vowels(text)
print("This is the vowels count: ", count)