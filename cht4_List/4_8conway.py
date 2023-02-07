import random, time, copy
WIDTH = 10
HEIGHT = 6

nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') #增加一个活方块
        else:
            column.append('.') #增加一个死方块
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')   #分隔每一行
    currentCells = copy.deepcopy(nextCells)
   #打出当前cell
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  #打印'#'或空格
        print()  #打印新一行

    #计算下一个cell
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0

            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1   #左上是活的
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1   #上是活的
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1   #右上是活的
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1   #左是活的
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1   #右是活的
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1   #左下是活的
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1   #下是活的
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1   #右下是活的

            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #大于3的也要变成死的
                nextCells[x][y] = '#'
            elif currentCells[x][y] == '.' and numNeighbors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = '.'
            print(x,y,numNeighbors)

        time.sleep(1)