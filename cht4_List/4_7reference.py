import copy
#原列表值改变，id不变
spam = [0,1,2,3,4,5]  #spam引用了该表
cheese = spam   #cheese复制了spam引用的表的值，而不是列表值本身，spam和cheese指向同一个list
cheese[1] = 'hello'  #同时修改了指向的列表值（即spam引用的，所以spam同步修改了）
print(spam, 'id=',id(spam))
print(cheese, 'id=',id(cheese))

#字符串不可变，若做“更改”，则会创建新字符串对象
bacon = 'Hello'
print(bacon, 'id=',id(bacon))
bacon +=' world!'
print(bacon, 'id=',id(bacon))

#传递引用,会改变运来的值
def eggs(someParameter):
    someParameter.append('Hello')

spam1 = [1,2,3]
print(spam1,'id=',id(spam1))
eggs(spam1)
print(spam1,'id=',id(spam1))

#copy() deepcopy() 复制可变值，而不是复制引用
spam2 = copy.copy(spam1)
print(spam2,'id=',id(spam2))