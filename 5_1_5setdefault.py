#setdefult():  to set a default value for a key
spam = {'color': 'red', 'age': 42}
print(spam)
if 'color' not in spam:
    spam['color'] = 'black'
# print(spam)
bacon = {'color': 'red', 'age': 42}
bacon.setdefault('color', 'black')
print(bacon)