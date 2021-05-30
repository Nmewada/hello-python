#1)Write a Python program to display a user-entered name followed by Good Afternoon using input() function.
name=input("Enter your name : \n")
print("Good Morning, "+name)




#2)Write a program to fill in a letter template given below with name and date.
# letter = ‘’’ Dear <|NAME|>,

#                         You are selected!

#                         <|DATE|>

letter='''Dear <|Name|>,
Greeting from Pixeldust
Congratulations your are selected
Have a great day ahead!
Thanks you
Date : <|Date|>
'''
name=input("Enter Your Name : \n")
date=input("Ënter Date : \n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)




#3)Write a program to detect double spaces in a string.
st = "This is a string with double  spaces"
doubleSpaces = st.find("  ")
print(doubleSpaces)


#4)Replace the double spaces from problem 3 with single spaces.
st = "This is a string with double  spaces  ok"
st = st.replace("  ", " ")
print(st)



#5)Write a program to format the following letter using escape sequence characters.
# letter = ""Dear Sandip,I am really enjoying python!! Thank you!”
letter = "Dear Sandip, I am really enjoying python!! Thanks man!"
print(letter)

formatted_letter = "Dear Sandip,\n\tI am really enjoying python!!\nThanks man!"
print(formatted_letter)