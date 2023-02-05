#字符串为 不可变 数据，不能被修改，只能被复制
name = 'ermao a cat'
newName = name[0:6] + 'the' + name[7:11]  #复制到索引2的前一个字符
print(name)
print(newName)

#列表值是可变的
eggs = [1,2,3]
eggs = [4,5,6]  #列表值没有改变，而是用新列表覆写了老的列表
print(eggs)

#del、append可以就地修改原列表值
eggs = [1,2,3]
del eggs[2]
eggs.append(4)
print(eggs)

#用（）表示tuple元组，和字符串一样，不可变
spam = ('hello',42,0.5)
print(spam[0])
print(spam[1:3])

print(type(('hello',)))  #tuple类型
print(type(('hello')))   #str类型

#元组tuple和列表list换格式
a = ['cat','dog',5]   #list
b = ('cat','dog',5)   #tuple
print(tuple(a))
print(list(b))
print(list('hello'))  #str->list