#setdefult():  to set a default value for a key
spam = {'color': 'red', 'age': 42}
print(spam)

if 'name' not in spam:
    spam['name'] = 'Pooka'
print(spam)

bacon = {'color': 'red', 'age': 42}
bacon.setdefault('name', 'Pooka')
print(bacon)
bacon.setdefault('name', 'Simy')  #can not be changed twice
print(bacon)

message = 'It was a blight cold day in April.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
