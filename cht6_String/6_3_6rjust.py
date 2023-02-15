#rjust() ljust() center()
print('Hello'.rjust(10))
print('Hello, world'.rjust(20))
print('Hello, world'.ljust(20))

print('Hello'.rjust(10,'*'))
print('Hello, world'.rjust(20,'='))
print('Hello, world'.ljust(20,'-'))

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 800}
printPicnic(picnicItems, 12, 6)
printPicnic(picnicItems, 20, 4)