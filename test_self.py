import math
game_board = [
    [1,9,6,0,5,3,0,0,0],
    [7,0,0,2,1,0,3,0,0],
    [0,3,0,0,0,6,0,0,7],
    [0,7,0,0,0,2,4,1,0],
    [5,6,1,3,7,4,0,0,0],
    [4,0,0,0,6,0,7,0,0],
    [6,1,0,0,2,0,5,0,9],
    [2,0,0,6,0,0,8,3,0],
    [0,8,0,5,3,0,0,7,2]
]


def print_game_board(game_board):
	for i in range(len(game_board)):
		if i%3==0 and i!=0:
			print('- - - - - - - - - - - - - - - ')

		for j in range(len(game_board[0])):
			if j%3==0 and j!=0:
				print('|',end=' ')

			if j==8:
				print(game_board[i][j])
			else:
				print(str(game_board[i][j])+' ',end=' ')
#print_game_board(game_board)


def find_empty_space(game_board):
	for i in range(len(game_board)):
		for j in range(len(game_board[0])):
			if game_board[i][j]==0:
				return (i,j) #row x col
	return None

def check_legal_operation(game_board,num,pos):
	for i in range(len(game_board[0])):
		if game_board[pos[0]][i]==num and pos[1]!=i:
			return False

	for j in range(len(game_board)):
		if game_board[j][pos[1]]==num and pos[0]!=j:
			return False

	row_idx=math.floor(pos[0]/3)
	col_idx=math.floor(pos[1]/3)

	for i in range(row_idx*3,row_idx*4):
		for j in range(col_idx*3,col_idx*4):
			if game_board[i][j]==num and (i,j)!=pos:
				return False

	return True


def solve_sudoko(game_board):
	idx_finder=find_empty_space(game_board)
	if not idx_finder:
		return True
	else:
		row=idx_finder[0]
		col=idx_finder[1]
		for i in range(1,10):
			if check_legal_operation(game_board,i,idx_finder)== True:
				game_board[row][col]=i
				if solve_sudoko(game_board):
					return True
				game_board[row][col]=0
	return False

print("", '##### Original Sudoko #####')
print_game_board(game_board)
print('\n')
solve_sudoko(game_board)
print('  ##### Solved Sudoko #####')
print_game_board(game_board)





