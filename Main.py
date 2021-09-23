# Tic-Tac-Toe game in Python with simple AI


board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return (board[pos] == ' ')


def printBoard(board=board):
    # print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    # print('   |   |')
    print('-----------')
    # print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    # print('   |   |')


def isWinner(bo, le):
    horizontal_win = ( ( (bo[1] == le) and (bo[2] == le) and (bo[3] == le) ) or
                       ( (bo[4] == le) and (bo[5] == le) and (bo[6] == le) ) or
                       ( (bo[7] == le) and (bo[8] == le) and (bo[9] == le) ) )

    vertical_win = ( ( (bo[1] == le) and (bo[4] == le) and (bo[7] == le) ) or
                     ( (bo[2] == le) and (bo[5] == le) and (bo[8] == le) ) or
                     ( (bo[3] == le) and (bo[6] == le) and (bo[9] == le) ) )

    diagonal_win = ( ( (bo[1] == le) and (bo[5] == le) and (bo[9] == le) ) or
                     ( (bo[3] == le) and (bo[5] == le) and (bo[7] == le) ) )

    return (horizontal_win or vertical_win or diagonal_win)


def playerMove():
    run = True
    while run:
        move = input(f"Please select a position to place an (X) (1-9): ")
        try:
            move = int(move)
            if ( (move > 0) and (move < 10) ):
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is occupied")
            else:
                print("Please type a number within the range (1-9)")

        except:
            print("what you wrote isn't a number between 1 and 9. Please try again ")


def compMove():
    possible_moves = [x for x, letter in enumerate(board) if (letter == ' ' and x != 0)]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if isWinner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = selectRandom(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    corners_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = selectRandom(corners_open)
    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    return not(board.count(' ') > 1)


def main():
    print ("Welcome to Tic-Tac-Toe")
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print("Sorry, the bot won this time!")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print("Tie Game!")
            else:
                insertLetter('O', move)
                print (f"Computer places an (O) in position {move}")
                printBoard()
        else:
            print("You won this time!, Well Done!")
            break

    if isBoardFull(board):
        print("Tie Game!")

run_game = True
while run_game:
    answer = input("Do you want to play Tic-Tac-Toe?[yes/no] ")
    if answer == "yes":
        main()
    else:
        print("I hope you had fun ^^")
        run_game = False

