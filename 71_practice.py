# Repeat program 70_practice for a list of such words to be censored.
words = ["donkey", "kaddu", "mote"]
with open("badword.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("badword.txt", "w") as f:
        f.write(content)