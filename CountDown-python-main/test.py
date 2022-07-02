import re
from itertools import permutations as perm


# converting txt file of english words to set
with open('words.txt', 'r') as cdwords:
    cdwords = cdwords.read()# get all the words 
    wordregex = re.compile('\w+')
    cdwords = wordregex.findall(cdwords)# all the words seprated by , in array
    cdwords = set(cdwords)# all the words sent to set() to eliminate repatition 

    #                  123456789
characters = list('sdbrakcee'.lower())# turn the random letter to array / list 
length = len(characters)
words = set()
alphabet = set('abcdefghijklmnopqrstuvwxyz')
not_alpha = alphabet.difference(set(characters))# got the letters that are not in selcted letter with difference()

possible = set()




# Ruling out words which contain letters not in 'characters'
for word in cdwords:
    for letter in not_alpha:
        
        if letter in word:
            break
    else:
        possible.add(word)
       


# Finding every permutation of 'characters' for each length from 1 to how many letters there are
for l in range(1, length + 1):
    for subset in perm(characters, l):
        word = ''.join(subset)
        words.add(word)
