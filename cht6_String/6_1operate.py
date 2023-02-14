#spam = "That is Alice's cat."   which is wrong, ' can be seen the end of string
#There are several methods to solve it
spam = "That is Alice's cat."
print(spam)
spam = 'That is Alice\'s cat.'
print(spam)
print(r'That is Alice\'s cat.')   #r stands for the original string
print('''Dear Alice,

Eve's cat has been arrested for capnapping.

Sincerely;
Bob''')   #'''  '''can reserve the  the original string
print('Dear Alice,\n\nEve\'s cat has been arrested for capnapping.\n\nSincerely;\nBob') 

#""":Multi-line comments
"""This is a test Python program.
Written by Simy
"""
bacon = 'Hello, world!'
print(bacon[7:-1])
