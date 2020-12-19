sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in range(9):
    if i%3==0:
        print('- '*11,end='\n')


    for j in range(9):  
       
        if j==2:
             print((sudoku[i][j]),end=' | ')
        elif j==5:
            print((sudoku[i][j]),end=' | ')
        elif j==8:    
            print((sudoku[i][j]),end='\n')
        else:
            print((sudoku[i][j]),end=' ')
        