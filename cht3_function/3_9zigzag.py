import time, sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')  #确定缩进量
        print('********')
        time.sleep(0.1) #暂停1/10秒

        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False  #变方向
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:  #键盘ctrl+c 退出
    sys.exit()
