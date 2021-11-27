#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special char (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid

import time

def passwordintro ():
    print ('Hello and welcome to Password Validator!')
    time.sleep (1)
    print ("Please enter the password that you want to validate and we'll check if it's valid or not.")
    time.sleep (1)
    print ('For your password to be valid, here are some guidelines:')
    time.sleep (1)
    print ('1. Your password must be greater than 15 letters.')
    time.sleep (1)
    print ('2. Your password must have at least one capital letter.')
    time.sleep (1)
    print ('3. Your password must have at least one number (0-9).')
    time.sleep (1)
    print ('4. Your password must have atleast one special character (@,#,!,%,^,&,*, etc.).')
    time.sleep (1)
    print ("That's all for the instructions, you can now enter your password.")

def getpassword ():
    userpassword = input("Please enter password here: ")
    return userpassword

def capitalletter (password_):
    capitalletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for p in password_:
        for c in capitalletter:
            if p == c:
                print ("There is at least one capital letter detected in your input.")
            else:
                print ("No capital letter was detected in your input.")

def numbers (password_):
    numbers = "0123456789"
    for p in password_:
        for n in numbers:
            if p == n:
                print ("There is at least one number detected in your input.")
            else:
                print ("There is no number detected in your input.")

def specialcharacters (password_):
    specialchar = "!@#$%^&*()_+-=/\'?:;,{[]}`.~"
    for p in password_:
        for s in specialchar:
            if p == s: 
                print ("There is at least one special character detected in your input.")
            else:
                print ("There are no special characters detected in your input.")

def lettercounter (password_):
    count = 0
    for p in password_:
        for co in count:
            count = count + 1
    if count > 15:
        print ("There are more than 15 letters detected in your input.")
    else:
        print ("The amount of letters detected in your input is less than 15.")

passwordintro ()

password = getpassword ()

capitalletterdetector = capitalletter (password)

numberdetector = numbers (password)

specialchardetector = specialcharacters (password)

letters = lettercounter (password)