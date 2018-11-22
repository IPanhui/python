def mutiple_table():

    row = 1
    while row < 10:
        col = 1
        while col <= row:
            print ("%d*%d = %d\t"%(col,row,row*col),end=" ")
            col += 1
        print ("")
        row += 1
