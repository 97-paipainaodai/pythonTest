spam = ['cat','dog','moose','rat']
print(len(spam))
print('Hello,'+spam[0])  #列表第1个参数
print('Hello,'+spam[1])  #列表第2个参数
print('Hello,'+spam[-1])  #列表倒数第1个参数

print(spam[0:3])   #列表第1~3个参数  切片不包括第二个索引值
print(spam[:3])   #列表第1~3个参数
print(spam[2:4])   #列表第3~4个参数
print(spam[2:])   #列表第3~最后1个参数
print(spam[1:-1])   #列表第2~倒数第2个参数

#利用索引改变值
spam[1] = 'elephant'  
print(spam) 

#列表连接和复制
alist = [1,2,3]
blist = ['A','B','C']
print(alist + blist) 

#del列表值删除
del spam[2]
print(spam)
del spam[2]
print(spam)