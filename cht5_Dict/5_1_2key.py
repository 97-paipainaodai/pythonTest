#keys()  values()  items()
#The returns are not LIST, can not be modified.
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

print(spam.keys())
print(list(spam.keys()))   #make a list

for k,v in spam.items():
    print('Key:' + k + ' Value: ' + str(v))