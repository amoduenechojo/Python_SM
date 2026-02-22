text = input("Enter a word: ")

new_text = ""

for letter in text:
    new_text = new_text + letter.lower()

print("Lowercase word:", new_text)
