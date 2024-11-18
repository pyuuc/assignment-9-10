import math, random
from pprint import pprint
import copy


class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''

    def __init__(self, row_length, removed_cells):
        random.seed(10)
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length= int(math.sqrt(self.row_length))
        self.board = [] # this is the 2d list that has all values
        self.game = [] # this is the 2d list that has some value removed
        temp=[0]*self.row_length
        for i in range(self.row_length):
            self.board.append(temp.copy())
        #print("test constructor run succesfully")
        #print(self.board)

    '''
	Returns a 2D python list of numbers which represents the board

	Parameters: None
	Return: list[list]
    '''

    def get_board(self):
        return self.board


    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''

    def print_board(self):
        print(self.board)

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row

	Return: boolean
    '''

    def valid_in_row(self, row, num):
        temp_row=self.board[row]
        if num in temp_row:
            return False
        else:
            return True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column

	Return: boolean
    '''

    def valid_in_col(self, col, num):
        for row in self.board:
            if row[col]==num:
                return False
        else:
            return True

    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        for i in range(col_start * 3, col_start*3+3):
            for j in range(row_start * 3, row_start*3+3):
                if self.board[i][j]==num:
                    return False
        return True


    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''

    def is_valid(self, row, col, num):
        if self.valid_in_col(col, num) and self.valid_in_row(row, num):
            return True
        else:
            return False

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        temp =[1, 2, 3, 4, 5, 6, 7, 8, 9]
        temp =random.sample(temp, 9)
        for i in range(col_start * 3, col_start*3+3):
            for j in range(row_start * 3, row_start*3+3):
                self.board[i][j]= temp.pop()

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(1, 1)
        self.fill_box(2, 2)

    
    '''
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):

        #print(row, col)
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            # print("=====", row, col, num)
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
	Parameters: None
	Return: None
    '''

    def fill_values(self):
        #print("in fill values", self.box_length)
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(self):
        self.game = copy.deepcopy(self.board)
        remove  = list(range(self.row_length))
        answer = {}
        count = 0
        while True:
            row, col = random.choices(remove, k=2)
            print(f"{row=}{col=}")
            if self.game[row][col] != "None":
                answer[(row,col)] = self.game[row][col]
                self.game[row][col] = "None"
                count += 1
            if count >= self.removed_cells:
                break
        return self.game, answer


'''
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

def generate_partial_sudoku(size, removed):
    
    while True:
        print("Menu:")
        print("1. check the initial sudoku board")
        print("2. fill left upper coner.")
        print("3. fill the core middle.")
        print("4. fill right bottem coner.")
        print("5. fill a diagonal.")
        print("6. fill all")
        print("7. quit")
        key = input("Please select a number to check the sudoku board 1 2 3 4...etc: ")
        sudoku = SudokuGenerator(size, removed)
        if key == "1":
            sudoku = SudokuGenerator(size, removed)
            pprint(sudoku.board)
        elif key == '2':
            sudoku.fill_box(0, 0)
            pprint(sudoku.board)
        elif key == '3':
            sudoku.fill_box(1, 1)
            pprint(sudoku.board)
        elif key == '4':
            sudoku.fill_box(2, 2)
            pprint(sudoku.board)
        elif key == '5':
            sudoku.fill_diagonal()
            pprint(sudoku.board)
        elif key == '6':
            sudoku.fill_diagonal()
            sudoku.fill_remaining(0, 3)
            pprint(sudoku.board)

        elif key == "7":
            print("Thank you")
            break
        else:
            
            print("Invalid input, please try again")




#test=generate_sudoku(9, 30)
#print(test)
#temp = SudokuGenerator(9, 30)
#temp.print_board()
#temp_list=temp.get_board()
#pprint(temp_list)
#print(temp.valid_in_row(0,0))
#print(temp.valid_in_col(0,9))
#temp.fill_box(0,0)
#temp.fill_box(2,2)
#temp.print_board()
#temp.fill_diagonal()

# generate_partial_sudoku(9, 30)
#temp.fill_values()
#temp_list=temp.get_board()
#pprint(temp_list)

test = SudokuGenerator(9, 1)
test.fill_values()
pprint(test.get_board())
x,y = test.remove_cells()
pprint(x)
print(y)
y_new = sorted(y)
print(x == test.get_board())
for a,b in y_new:
    x[a][b] = y[(a,b)]
print(x == test.get_board())
print(x)