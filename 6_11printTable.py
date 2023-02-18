tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)

    #return each col's length
    def lenMax(col):
        lenReturn = len(col[0])
        for i in range(len(col)-1):
            if len(col[i+1]) > len(col[i]):
                lenReturn = len(col[i+1])
        return lenReturn

    for i in range(len(tableData)):
        colWidths[i] = lenMax(tableData[i])

    for y in range(len(tableData[0])):   #length of every string list 
        printCol = tableData[0][y].rjust(colWidths[0])
        for x in range(1, len(tableData)):   #length of the list table
            printCol += ' ' + tableData[x][y].ljust(colWidths[x]) 
        print(printCol)
    
    # print(colWidths)

printTable(tableData)
