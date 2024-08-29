from datetime import date
today = date.today()
print(today)
this_month = today.month
print(this_month)
#this_month = today.strftime('%B')

#Part 1
#Ask for user name
name = input('What is your name? ')

#Ask for user's birthday month
birthday_month = input('Which month were you born in? ')

#Welcoming user
print(f'Greetings and welcome, {name}!')

#This will give you the number of characters in your name
print('Your name has', len(name), 'letters')

#If your birthday month is in August, it will let you know!
if birthday_month.lower() == 'August':
    print('Happy Birthday month!')
else:
    print('Your birthday is not in August!')



# from datetime import date
# now = date.today()
# current_month = now.month

#Part 2
# Write a program that asks for the names of all of the classes you are taking this semester
# Save these class names in a list.
# Print all the items in the list, one per line.

list_of_classes = [] # this will ask for the names of all your classes
while True:
    class_name = input('Enter class name or press enter to stop: ')
    if class_name == '':
        break #this will end the looop
    else:
        list_of_classes.append(class_name) # append means stick it to the end of the list

print(list_of_classes) #this will print out the classes

for class_name in list_of_classes:
    print(class_name) # This will print out the list of classes one by one