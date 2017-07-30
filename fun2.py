def draw_2d(n, m, fill):
    for i in range(1, (n * m) + 1):
        if i % m != 0:
            print(fill, end="")
        else:
            print(fill)

def specialDraw2d(n, m, border, fill):
    numRow = 0
    numColumn = 0
    var = 1
    for i in range(1, (n * m) + 1):
        ## print new line whenever needed
        if i == (m * var) + 1:
            print()

        ## draw borders whenever needed
        if numRow == 0 or numRow == (m - 1) or i == (m * var) + 1 or i == (m  * var):
            print(border, end="")
        ## draw fill wheever needed
        elif i % m != 0:
            print(fill, end="")
        ## draw
        else:
            print(fill)
            
        if i == (m * var) + 1:
            numRow = numRow + 1
            var = var + 1
            
    
            
draw_2d(3, 23, '*')
specialDraw2d(16, 16, '&', 'x')
