#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

import time

print ("Welcome to word, vowel, and consonant counter!")
time.sleep (2)
print ("Please enter your sentence for the program to count the amount of words, vowels, and consonants.")
time.sleep (2)
sentence = input("Enter sentence here: ")

def countvowels (sentence):
    count = 0
    vowels = 'AEIOUaeiou'
    for s in sentence:
        for v in vowels:
            if s == v:
                count = count+1
    return count

vowelcount = countvowels (sentence)

print (f'Based on the sentence that you entered, here are {vowelcount} vowels counted.')