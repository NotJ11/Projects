t = [['-','-','-'], ['-','-','-'], ['-','-','-']]


# ---------------- BOARD ------------------
def board():
    for l in range(3):
        for c in range(3):
            print(f'{t[l][c]:^3}', end='')
        print()



# ---------------- Checking Win and Draw ----------------
def check_win():
# Checking rows
    for l in range(3):
        if t[l][0] == t[l][1] == t[l][2] == 'X':
            print('X wins')
            return True
        elif t[l][0] == t[l][1] == t[l][2] == 'O':
            print('O wins')
            return True

# Checking col
    for c in range(3):
        if t[0][c] == t[1][c] == t[2][c] == 'O':
            print('O wins')
            return True
        elif t[0][c] == t[1][c] == t[2][c] == 'X':
            print('X wins')
            return True

# Checking diagonals
    if t[0][0] == t[1][1] == t[2][2] == 'O' or t[0][2] == t[1][1] == t[2][0] == 'O':
        print('O wins')
        return True
    elif t[0][0] == t[1][1] == t[2][2] == 'X' or t[0][2] == t[1][1] == t[2][0] == 'X':
        print('X wins')
        return True

# Checking Draw
    for l in t:
        for n in l:
            if n == '-':
                return False
    print("Draw")
    return True
    



# ---------------- Player's Turn ----------------
def O_turn():
    print("  O's Turn: ")
    row = int(input('Row: '))
    col = int(input('Column: '))
    t[row][col] = 'O'

def X_turn():
    print("  X's Turn: ")
    row = int(input('Row: '))
    col = int(input('Column: '))
    t[row][col] = 'X'



# ---------------- Game ----------------
end = False
board()
print()

while end != True:
    X_turn()
    board()
    print()
    end = check_win()
    if end == True:
        break

    O_turn()
    board()
    print()
    end = check_win()


