# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:00:37 2021

@author: JENI
"""

def madlib():
    print("************Welcome to Jane's Madlib!************")
    print("You are expected to enter words that best fit into the blank spaces.")
    print("NB: These words can be parts of speech!")
    verb_1 = input('Verb: \n')
    pronoun_1 = input('pronoun: \n')
    pronoun_2 = input('pronoun: \n')
    verb_2 = input('verb: \n')
    noun_1 = input('noun: \n')
    adj_1 = input('Adjective: \n')
    verb_3 = input('verb: \n')
    noun_2 = input('noun: \n')
    verb_4 = input('verb: \n')
    colour = input('colour \n')
    verb_5 = input('verb: \n')
    con_1 = input('conjuction: \n')
    

    story = f"It was the 7th of may, 2021, Jennifer {verb_1} up at exactly 7:45 am and was staring at the ceiling. {pronoun_1} just started {pronoun_2} codinng journey few weeks back and it hasn't been a smooth one. \n From {verb_2} the web, to networking, to {noun_1} of information on the web, it has been {adj_1}.\n{pronoun_1} decided to {verb_3} a break today, at least for her mental health. So, {pronoun_1} decided to write a to-do {noun_2}.\n {pronoun_1} would have her bath, {verb_4} breakfast of {colour} vegetables. After which {pronoun_1} would {verb_5} a movie {con_1} then take a nap, make lunch and then take a stroll to the mall."
    
    return story
             
print(madlib())