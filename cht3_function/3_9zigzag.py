#20230204yss修改：通过输入可输出固定次数的图案

import time, sys

while True:
    indent = 0
    indentIncreasing = True
    n = 0
    while True:
        print('请输入你想看到几次闪电（1~10）或退出（0)：', end='')
        num = input()
        num = int(num)
        if num == 0:
            sys.exit()
        else:
            break

    if num > 0:
        while n/3 < num:
            print(' ' * indent, end='')  #确定缩进量
            print('********')
            time.sleep(0.1) #暂停1/10秒
            if indentIncreasing:
                indent = indent + 1
                if indent == 20:
                    indentIncreasing = False  #变方向
                    n = n + 1
            else:
                indent = indent - 1
                if indent == 0:
                    indentIncreasing = True
                    n = n + 1
    elif num < 0:
        print('请输入正确的数字！')


# #以下为原程序
# import time, sys
# indent = 0
# indentIncreasing = True

# try:
#     while True:
#         print(' ' * indent, end='')  #确定缩进量
#         print('********')
#         time.sleep(0.1) #暂停1/10秒

#         if indentIncreasing:
#             indent = indent + 1
#             if indent == 20:
#                 indentIncreasing = False  #变方向
#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indentIncreasing = True
# except KeyboardInterrupt:  #键盘ctrl+c 退出
#     sys.exit()