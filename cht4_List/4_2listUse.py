import random
catNames = []
while True:
    print('Enter the name of cat'+ str(len(catNames)+1)+'(Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('The cat names are:')
for name in catNames:
    print(''+name)

#输入猫猫名字空后启动下面的程序
#列表用于循环
for i in range(4):
    print(i)

#for循环中使用range(len(somelist))
supplies =['pen','apple','milk']
for i in range(len(supplies)):
    print('Index '+str(i)+' in supplies is: '+supplies[i])
#enumerate()函数实现该段代码
for index, item in enumerate(supplies):
    print('Index '+str(index)+' in supplies is: '+item)


#判断值是否在列表中
a='pen' in supplies
print(a)
b='pen' not in supplies
print(b)

#多变量赋值
cat = ['fat','black','loud']
size, color, disposition = cat
print(size, color, disposition)

#列表随机选择、重新排序
print(cat)
print(random.choice(cat))
random.shuffle(cat)
print(cat)