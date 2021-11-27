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


passwordintro ()