#upper() lower() isupper() islower()
spam = 'Hello, world!'
print(spam)
spam = spam.upper()   #spam.upper return a new string, make the origin string be the new string
print(spam)
spam = spam.lower()
print(spam)

print('HELLO is supper: '+str('HELLO'.isupper()))
print('HELLO is lower: '+str('HELLO'.islower()))
print('Hello'.upper().lower().upper().upper()) 