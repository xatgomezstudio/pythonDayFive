# ----------------------------- BUILD A TRANSLATOR -------------------
print("-------------------------Translator example-------------------------")
# this exercise translates words into a made up 'Giraffe Language'
# all the vowels will get turned into G's
# THIS IS A COMBINATION OF FOR LOOPS AND IF STATEMENTS

def translate(phrase):
    # here we are naming the function 'translate',
    # and identified the variable as 'phrase'
    translation = ""
    # we set the storage spot that will add what's collected from the for loop
    # and made the final collection a string ""
    for letter in phrase:
        # we set 'letter' as the name of what we're sorting
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
                # using .lower and .isupper we can search by case and replace accordingly
            else:
                # here python lets us compare and check if our item matches anything in the "" string we provided
                translation = translation + "g"
                # here we tell it to replace matching items with a G in the final storage
        else:
            translation = translation + letter
            # if not then just store the original item
    return translation

# print(translate(input("Enter phrase: ")))


# ----------------------------- COMMENTS -------------------
# python has specific comment operators

'''
anything written in this space will be commented
useful to turn off code without adding individual comments
called 'commenting out' when trouble shooting
'''

# ----------------------------- CATCHING ERRORS -------------------
print("----------------------Catching errors example-------------------------")
# TRY EXCEPT BLOCKS field possible errors or user issues
# err is common python jargon
# best practice is to name err specifically

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")


# ----------------------------- READING FILES ----------------------------------
print("-----------------------Reading files Example 1-------------------------")
# # READING FROM EXTERNAL FILES IN PYTHON

# this variable allows us to store the info from the file we opened
employee_file = open("employee.txt", "r")
                        # ^file path     ^ here the MODE is a python command for the file
                        # here we can pass in the files name, a relative path, or an absolute path

# you could also use python specific commands it to modify the file
# "r" for READ
# "w" for WRITE,
# "a" for APPEND to add info, or
# "r+" to READ AND WRITE,

# it's best practice, to check that a file is readable
print(employee_file.readable())
# this will return a boolean value, should come back TRUE if the "r" command is used
print(employee_file.read())
# ^^ this action will print the entire file into the counsel
employee_file.close()

print("-----------------------Reading files Example 2-------------------------")
# reading files line by line

employee_file = open("employee.txt", "r")
print(employee_file.readable())

print(employee_file.readline())
# this action will read the first line, then if the action is called again it'll read the next line
# so this would read the first 3 lines
print(employee_file.readline())
print(employee_file.readline())


# YOU ALWAYS WANT TO CLOSE THE FILE AFTER THE ACTION IS COMPLETED
employee_file.close()


print("-----------------------Reading files Example 3-------------------------")
#reading specific lines in a file

employee_file = open("employee.txt", "r")
print(employee_file.readable())

print(employee_file.readlines()[6])
#                               ^ this picks the index from the array we want to engage with
employee_file.close()

print("-----------------------Reading files Example 3-------------------------")
#reading files with a for loop

employee_file = open("employee.txt", "r")
print(employee_file.readable())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()