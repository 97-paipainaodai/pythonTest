#join()  make list to a string
#split()  make string to a list
alist = ['cats', 'rats', 'bats']
astring = ', '.join(alist)
print(alist)
print(astring)
astring = ' '.join(alist)
print(astring)


blist = astring.split(' ')
print(blist)
blist = astring.split('a')
print(blist)

spam = '''Dear Alice,

Eve's cat has been arrested for capnapping.

Sincerely;
Bob'''
bacon = spam.split('\n')
print(bacon)