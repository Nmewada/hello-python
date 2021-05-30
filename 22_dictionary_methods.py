myDict = {
    "fast": "In a Quick Manner",
    "nitin": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'nitin': 'Player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.values()) # Prints the values of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "sandip": "Best Friend",
    "priya": "Best Friend",
    "vimal": "Friend",
    "nitin": "Rockstar"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("nitin")) # Prints value associated with key "nitin"
print(myDict["nitin"]) # Prints value associated with key "nitin"

# The difference between .get and [] sytax in Dictionaries?
print(myDict.get("nitin1")) # Returns None as nitin1 is not present in the dictionary
print(myDict["nitin1"]) # throws an error as nitin1 is not present in the dictionary