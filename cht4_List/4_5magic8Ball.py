import random

message = ['Certain',
     'Yes',
     'Doutful',
     'So good',
     'Try again']

print(message)
print('My answer is: ',message[random.randint(0,len(message)-1)])
