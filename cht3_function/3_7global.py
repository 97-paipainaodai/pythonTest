# def spam():
#     global eggs   #用global标注eggs是全局变量
#     eggs = 'spam' #在函数中修改全局变量

# eggs = 'global'
# spam()
# print(eggs)

#区分全局变量和局部变量
def spam():
    global eggs
    eggs = 'spam' #全局变量：有global定义

def bacon():
    eggs = 'bacon' #局部变量：赋值

def ham():
    print(eggs)  #全局变量:无赋值语句

eggs =  42 #全局变量
spam()
print(eggs)
