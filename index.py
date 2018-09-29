#Longest Even Word
#In this program the user type 5 words and
#the computer will display the longest even word

import sys
import os

def longestEvenWord(sentence):
    if len(sentence) == 0:
        return '00'

    words = sentence.split()
    word = ''
    longestWordLength = 0
    
    for w in words:
        if len(w) % 2 == 0 and len(w) > longestWordLength :
            word = w
            longestWordLength = len(w)
            
    if word != '':
        print('The longest even word is: ',word)
        print('The longest word length is: ', longestWordLength)
        return word
    else:
        return '00'


    

print("""

        #####################################################
        #                                                   #
        #     Welcome to the longest even word program!     #
        #                                                   #
        #####################################################
""")
sentence = input('\n\nPlease enter at lease 5 words: >')
longestEvenWord(sentence)

input('\nPlease Press Enter to Exit')
os.system("clear")
sys.exit()
