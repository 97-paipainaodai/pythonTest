#函数实现：将列表值作为参数，返回一个字符串，包含所有表项，以逗号和空格分隔，并在最后一个表项前插入and
def change(spam):
    newStr = ''
    for i in range(len(spam)):
        if i < len(spam)-1:
            newStr += spam[i] + ', '
        else:
            newStr += 'and '+spam[i]
    return newStr

spam = ['apples','bananas','tofu','cats','ermao']
changedSpam = change(spam)
print(changedSpam)

        