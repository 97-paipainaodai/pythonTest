#index()方法
spam = ['hello','hi','Heyas','hello']
print(spam.index('hello'))
print(spam.index('Heyas'))

#append()、insert()，只能在列表上调用，不能用于字符串和整形
spam.append('cat')  #不能用spam = spam.append('cat') ,方法返回值是None
print(spam)
spam.insert(1,'dog')
print(spam)

#remove(),删除列表中的值
spam.remove('hello')
print(spam)   #只删除第一次出现的值

#sort()排序，默认正向
#不能对既有数字又有字符串的列表排序
app = ['a','z','A','Z','b']
app.sort()
print(app)   #首字母ASCII字符排序，大写字母在小写字母之前
#若要按a-z排序，不区分大小写
app.sort(key=str.lower)
print(app)

bacon = [2,5,3.3,7,1]
bacon.sort()
print(bacon)   #数字从小到大排序
bacon.sort(reverse=True)   #逆序排序
print(bacon)

#reverse()反转列表中的值
print(spam)
spam.reverse()
print(spam)

