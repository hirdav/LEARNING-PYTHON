#Chapter 2 assignment
#1: Personal Message: Store a person’s name in a variable, and print a message to that person . Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

buddy_name="dav"
sondes = f"Hello {buddy_name.title()},would you like to learn some Python today?"
print(sondes)

#2 : Store a person’s name in a variable, and then print that per
#son’s name in lowercase, uppercase, and titlecase 

buddy_name= "dav"
print(buddy_name.title())
print(buddy_name.lower())
print(buddy_name.upper())

#3.2-5. Famous Quote: Find a quote from a famous person you admire . Print the 
#quote and the name of its author . Your output should look something like the 
#following, including the quotation marks:
#Albert Einstein once said, “A person who never made a 
#mistake never tried anything new.”

quote = 'Price is what you pay, value is what you get.'
famous_person= 'warren buffet'
print(f"{famous_person.title()} once said, \"{quote}\"")


#2.7
her_name = "  miranda   "
print(her_name.rstrip())
print(her_name.lstrip())
print(her_name.strip())

#2.8
file_name= "pyhton notes.txt"
print(file_name.removesuffix('.txt'))



