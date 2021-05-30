# String Functions
story='once upon upon a time there was a Coder named Nitin who created python code'
print(len(story))
print(story.endswith("code"))
print(story.count("c")) 
print(story.count("upon"))
print(story.capitalize())  #first letter capital of string
print(story.find("upon"))  #find upon and return upon index position --> doesn't exist it will return  -1
print(story.replace("Nitin", "NMewada")) 



story1='           once upon upon a time there was a Coder named Nitin who created python code        '
print(story1)
print(story1.strip()) #remove white space from start and end