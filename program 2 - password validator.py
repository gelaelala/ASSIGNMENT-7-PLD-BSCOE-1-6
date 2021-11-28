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
    count = 0
    capitalletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for p in password_:
        for c in capitalletter:
            if p == c:
                    count = count + 1
    return count

def numbers (password_):
    count = 0
    numbers = "0123456789"
    for p in password_:
        for n in numbers:
            if p == n:
                    count = count + 1
    return count

def specialcharacters (password_):
    count = 0
    specialchar = "!@#$%^&*()_+-=/\'?:;,{[]}`.~"
    for p in password_:
        for s in specialchar:
            if p == s:
                count = count + 1
    return count

def lettercounter (password_):
    count = 0
    for p in password_:
            letter = len(p)
            count = count + letter
    return count

def results (letters_, capitalletter_, numberdetector_, specialcharac):
    print ('After checking the password that you entered:')
    time.sleep (2)
    if letters_ > 15:
        print ("The number of letters in your password is greater than 15 letters.")
    else:
        print ("The number of letters in your password is less than or equal to 15.")
    time.sleep(1)
    print (f"There's {capitalletter_} capital letter/s detected in your password.")
    time.sleep (1)
    print (f"There's {numberdetector_} number/s detected in your password.")
    time.sleep (1)
    print (f"There's {specialcharac} special character/s detected in your password.")

passwordintro ()

password = getpassword ()

capitalletterdetector = capitalletter (password)

numberdetector = numbers (password)

specialchardetector = specialcharacters (password)

letters = lettercounter (password)

results (letters, capitalletterdetector, numberdetector, specialchardetector)