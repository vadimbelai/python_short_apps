game = []
for i in range(3):
    game.append(['.'] * 3)

'''for i in range(3):
    print(*game[i])'''

def print_game(x): #вывод игрового поля
    for i in range(len(x)):
        print(*x[i])

def enter_x(x):
    print('Ходят крестики')
    n = int(input())
    return n

def enter_0(x):
    print('Ходят нолики')
    n = int(input())
    return n

def winner(x): #статус игры
    flag = False
    for i in range(3):
        for j in range(3):
            if x[i][0] == x[i][1] == x[i][2] or x[0][j] == x[1][j] == x[2][j] or x[0][0] == x[1][1] == x[2][2] or x[2][0] == x[1][1] == x[0][2]:
                flag = True
    return flag

def x0_status(x): #определение, чей ход
    flag = True
    sum_x = 0
    sum_0 = 0
    for i in range(3):
        sum_x += x[i].count('X')
        sum_0 += x[i].count('0')
    if sum_0 > sum_x:
        flag = False

def logic_og_game(x): #логика игры
    while not winner(x):
        if x0_status(x):
            n = enter_x(x)
            for i in range(3):
                for j in range(3):
                    if x[i][j] == n:
                        x[i][j] = 'X'
        else:
            n = enter_0(x)
            for i in range(3):
                for j in range(3):
                    if x[i][j] == n:
                        x[i][j] = '0'
        print_game(x)
    print('Игра окончена')

def start_game(x): #начало новой игры
    k = 9
    for i in range(3):
        for j in range(3):
            x[i][2 - j] = k
            k -= 1
    print_game(x)
    logic_og_game(x)

start_game(game)

