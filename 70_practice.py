# A file contains the word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file.
with open("badword.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("badword.txt", "w") as f:
    f.write(content)