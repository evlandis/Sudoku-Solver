sudokuBoard=[
    [3, 0, 6, 5, 0, 8, 4, 0, 0], 
    [5, 2, 0, 0, 0, 0, 0, 0, 0], 
    [0, 8, 7, 0, 0, 0, 0, 3, 1], 
    [0, 0, 3, 0, 1, 0, 0, 8, 0], 
    [9, 0, 0, 8, 6, 3, 0, 0, 5], 
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 7, 4], 
    [0, 0, 5, 2, 0, 6, 3, 0, 0]]

widthOfBoard=len(sudokuBoard[0])
heightOfBoard=len(sudokuBoard)
#prints the starting sudoku board to the console
def printBoardLines(sudokuBoard):
    horizLines=23*"-"
    #"i" goes through the y axis and distributes lines after every 3 units
    #then changes the y axis for the 2nd for loop so "j" can read the next row down

    #creates the horizontal lines
    for i in range(heightOfBoard):
        if i!=0 and i%3==0:
            print(horizLines)
        #"j" goes through the x axis and distributes a vertical line after every 3 units

        #creates the vertical lines
        for j in range(widthOfBoard):
            if j!=0 and j%3==0:
                print(" | ",end="")
            if j==8:
                #
                print(sudokuBoard[i][j]) #y and x axis
            else:
                print(str(sudokuBoard[i][j])+" ",end="")
printBoardLines(sudokuBoard)

def findZeros(sudokuBoard):
    for i in range(widthOfBoard):
        for j in range(heightOfBoard):
            if sudokuBoard[i][j]==0:
                return i,j
    return None, None
#findZeros(sudokuBoard)

def isGuessValid(board,guess,row,column): #row is y axis | column is x axis
    currentlyValid=True
    #checks to see if the guess is equal to any number in the row
    numbersInRow=board[row]
    for num in numbersInRow:
        if guess == num:
            #print(numbersInRow)
            #print("in row")
            currentlyValid=False  
    
    #checks to see if the guess is equal to any number in the column
    numbersInColumn=[]
    for i in range(9):
        numbersInColumn.append(board[i][column])
    if guess in numbersInColumn:
        #print(numbersInColumn)
        #print("in column")
        currentlyValid=False

    #checks to see if there is another number in its box equal to the guess
    rowBoxStart = (row//3) * 3#shows where set of 3 rows the y axis starts
    rowBoxEnd = rowBoxStart + 3
    columnBoxStart = (column//3) * 3#shows where set of 3 columns the x axis starts
    columnBoxEnd = columnBoxStart + 3
    for j in range(rowBoxStart,rowBoxEnd):
        for k in range(columnBoxStart,columnBoxEnd):
            if board[j][k]==guess:
                #print("in box")
                currentlyValid=False


    if currentlyValid==False:
        return False
    if currentlyValid==True:
        
        return True
#print(isGuessValid(sudokuBoard,3,1,4))#starts from (0,0) y,x

def main(board):
    #first finds the missing numbers all across the board
    row, column = findZeros(board)
    #if there are no missing numbers, that means the board is solved
    if row == None:
        return True
    #goes through the values 1-9 and checks to see if it is a valid guess on the board
    for guess in range(1,10):
        #if the guessed value works, it is inputted as new value for that previously empty slot
        if isGuessValid(board,guess,row,column)==True:
            board[row][column]=guess
            #now use recursion to go through and solve each empty slot
            #call the main function in itself which keeps being called until the board is completely solved
            if main(board)==True:
                
                return True

            #if the solution is not found, the value must be reset to zero to find another value that works
            board[row][column]=0
    
    return False

main(sudokuBoard)
if main(sudokuBoard)==True:
    print("\nThis Sudoku is solvable.\nSolved Sudoku: ")
    printBoardLines(sudokuBoard)
else:
    print("This Sudoku is not solvable.")
