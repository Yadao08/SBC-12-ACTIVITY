text  = input("Enter your song lyrics: ")
split_text = []
word = ""

for char in text.title():
    if char != " ":
        word += char
    else:
        split_text.append(word)
        word = ""
if word:
    split_text.append(word)

print(split_text)