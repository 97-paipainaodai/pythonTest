#strip() : remove spaces around the string
spam = '     Hello, world!  '
print(spam)
print(spam.strip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam)
print(spam.strip('ampS'))  #remove 'a' 'm' 'p' and 'S' around the string