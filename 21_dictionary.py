# Important: This syntax will create an empty dictionary
a = {}
print(type(a))


myDict = {
    "Firstname": "Nitin",
    "Lastname": "Mewada",
    "Habit": "Coding",
    "Marks": [1, 2, 5],
    "anotherdict": {'nitin': 'Player'}
}

print(myDict['Firstname'])
print(myDict['Lastname'])
print(myDict['Habit'])
myDict['Marks'] = [50, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['nitin'])