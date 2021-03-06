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

def sentenceinput():
    print ("Welcome to word, vowel, and consonant counter!")
    time.sleep (2)
    print ("Please enter your sentence for the program to count the amount of words, vowels, and consonants.")
    time.sleep (2)
    sentence = input("Enter sentence here: ")
    return sentence

def wordcounter (sentence):
    wordnum = sentence.split ()
    wordcount = len(wordnum)
    return wordcount
            
def countvowels (sentence):
    count = 0
    vowels = 'AEIOUaeiou'
    for s in sentence:
        for v in vowels:
            if s == v:
                count = count + 1
    return count

def countconsonants (sentence):
    count = 0
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstuvwxyz'
    for s in sentence:
        for c in consonants:
            if s == c:
                count = count + 1
    return count

def displayresult (wordcount_, vowelcount_, consonantcount_):
    print ('Here are the results based from the sentence that you entered:')
    time.sleep (2)
    if wordcount_ == 1:
        print (f"Based on the sentence that you entered, there's a total of {wordcount_} word.")
    else:
        print (f"Based on the sentence that you entered, there's a total of {wordcount_} words.")
    time.sleep (2)
    if vowelcount_ == 1:
        print (f"Based on the sentence that you entered, there's {vowelcount_} vowel counted.")
    else:
        print (f'Based on the sentence that you entered, there are {vowelcount_} vowels counted.')
    time.sleep (2)
    if consonantcount_ == 1:
        print (f"Based on the sentence that you entered, ther's {consonantcount_} consonant counted.")
    else:
        print (f'Based on the sentence that you entered, there are {consonantcount_} consonants counted.')

sentence = sentenceinput ()

wordcount = wordcounter (sentence)

vowelcount = countvowels (sentence)

consonantcount = countconsonants (sentence)

results = displayresult (wordcount, vowelcount, consonantcount)
