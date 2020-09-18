from string import digits
start = "_________"
line = "---------"
mat = [list(start[:3]), list(start[3:6]), list(start[6:])]

def print_mat(field):
    print(line)
    print("|", mat[0][0], mat[0][1], mat[0][2], "|")
    print("|", mat[1][0], mat[1][1], mat[1][2], "|")
    print("|", mat[2][0], mat[2][1], mat[2][2], "|")
    print(line)

print_mat(mat)

win_x = 0
win_o = 0
def win_state():
    global win_x
    global win_o
    if (mat[0][0] == mat[0][1] == mat[0][2] == "X" or
       mat[1][0] == mat[1][1] == mat[1][2] == "X" or
       mat[2][0] == mat[2][1] == mat[2][2] == "X" or
       mat[0][0] == mat[1][0] == mat[2][0] == "X" or
       mat[0][1] == mat[1][1] == mat[2][1] == "X" or
       mat[0][2] == mat[1][2] == mat[2][2] == "X" or
       mat[0][0] == mat[1][1] == mat[2][2] == "X" or
       mat[2][0] == mat[1][1] == mat[0][2] == "X"):
       win_x = 1
    if (mat[0][0] == mat[0][1] == mat[0][2] == "O" or
       mat[1][0] == mat[1][1] == mat[1][2] == "O" or
       mat[2][0] == mat[2][1] == mat[2][2] == "O" or
       mat[0][0] == mat[1][0] == mat[2][0] == "O" or
       mat[0][1] == mat[1][1] == mat[2][1] == "O" or
       mat[0][2] == mat[1][2] == mat[2][2] == "O" or
       mat[0][0] == mat[1][1] == mat[2][2] == "O" or
       mat[2][0] == mat[1][1] == mat[0][2] == "O"):
       win_o = 2
    return win_o + win_x

win = win_state()

def check_coord(coord):
    global coord_list
    global j
    global i
    if len(coord) != 3 or coord[1] != " ":
        return "You should enter numbers!"
    coord_list_string = coord.split()
    if coord_list_string[0] not in digits or coord_list_string[1] not in digits:
        return "You should enter numbers!"
    coord_list = [int(x) for x in coord_list_string]
    j = 3 - coord_list[1]
    i = coord_list[0] - 1
    if coord_list[0] > 3 or coord_list[1] > 3:
        return "Coordinates should be from 1 to 3!"
    if mat[j][i] in ["X", "O"]:
        return "This cell is occupied! Choose another one!"     

def game_state():
    if win == 1:
        return "X wins"
    elif win == 2:
        return "O wins"
    elif any("_" in part for part in mat):
        return "Game not finished"
    else:
        return "Draw"

state = game_state()
x_turn = 1

while True:
    win = win_state()
    state = game_state()
    if state == "Game not finished":
        x_move = input("Enter the coordinates: ")
        while True:
            check = check_coord(x_move)
            if check:
                print(check_coord(x_move))
                x_move = input("Enter the coordinates: ")
            elif x_turn == 1:
                mat[j][i] = "X"
                print_mat(mat)
                x_turn = 0
                break
            else:
                mat[j][i] = "O"
                print_mat(mat)
                x_turn = 1
                break
    else:
        break
print(state)
