#partition() :Text before and after the delimited string
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('o'))  #only the first 'o'

before, sep, after = 'Hello, world!'.partition(' ')
print(before, after)