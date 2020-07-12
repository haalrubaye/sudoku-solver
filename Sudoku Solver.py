import math
import copy
import time

# Original basic terminal solver

board = [['5', '3', ' ',
          '6', ' ', ' ',
          ' ', '9', '8'], [' ', '7', ' ',
                           '1', '9', '5',
                           ' ', ' ', ' '], [' ', ' ', ' ',
                                            ' ', ' ', ' ',
                                            ' ', '6', ' '],
         ['8', ' ', ' ',
          '4', ' ', ' ',
          '7', ' ', ' '], [' ', '6', ' ',
                           '8', ' ', '3',
                           ' ', '2', ' '], [' ', ' ', '3',
                                            ' ', ' ', '1',
                                            ' ', ' ', '6'],
         [' ', '6', ' ',
          ' ', ' ', ' ',
          ' ', ' ', ' '], [' ', ' ', ' ',
                           '4', '1', '9',
                           ' ', '8', ' '], ['2', '8', ' ',
                                            ' ', ' ', '5',
                                            ' ', '7', '9']]



def get_difference(knownNumbers):
    universal = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return universal.difference(knownNumbers)

def get_block(block):
    return set(board[block])


def get_row(block, index):
    row = set()

    # Takes the leftmost block/index and starts from there
    block = math.floor(block/3) * 3
    index = math.floor(index/3) * 3

    for i in range(block, block + 3):
        for j in range(index, index + 3):
            row.add(board[i][j])
    return row


def get_column(block, index):
    column = set()

    # Takes the uppermost block/index and starts from there
    block = math.floor(block % 3)
    index = math.floor(index % 3)

    for i in range(block, 9, 3):
        for j in range(index, 9, 3):
            column.add(board[i][j])
    return column


def get_possible_numbers(block, index):
    blockNumbers = get_block(block)
    rowNumbers = get_row(block, index)
    columnNumbers = get_column(block, index)
    availableNumbers = blockNumbers.union(rowNumbers).union(columnNumbers)

    return get_difference(availableNumbers)


def get_a_possible_number(block, index, usedNumbers):
    possibleNumbers = get_possible_numbers(block, index)

    if len(possibleNumbers.difference(usedNumbers[block][index])) == 0:
        return 0
    return possibleNumbers.difference(usedNumbers[block][index]).pop()


def print_board(board):
    print(board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' { ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' } ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print(board[0][3] + ' | ' + board[0][4] + ' | ' + board[0][5] + ' { ' + board[1][3] + ' | ' + board[1][4] + ' | ' + board[1][5] + ' } ' + board[2][3] + ' | ' + board[2][4] + ' | ' + board[2][5])
    print(board[0][6] + ' | ' + board[0][7] + ' | ' + board[0][8] + ' { ' + board[1][6] + ' | ' + board[1][7] + ' | ' + board[1][8] + ' } ' + board[2][6] + ' | ' + board[2][7] + ' | ' + board[2][8])
    print('-------------------------------------')
    print(board[3][0] + ' | ' + board[3][1] + ' | ' + board[3][2] + ' { ' + board[4][0] + ' | ' + board[4][1] + ' | ' + board[4][2] + ' } ' + board[5][0] + ' | ' + board[5][1] + ' | ' + board[5][2])
    print(board[3][3] + ' | ' + board[3][4] + ' | ' + board[3][5] + ' { ' + board[4][3] + ' | ' + board[4][4] + ' | ' + board[4][5] + ' } ' + board[5][3] + ' | ' + board[5][4] + ' | ' + board[5][5])
    print(board[3][6] + ' | ' + board[3][7] + ' | ' + board[3][8] + ' { ' + board[4][6] + ' | ' + board[4][7] + ' | ' + board[4][8] + ' } ' + board[5][6] + ' | ' + board[5][7] + ' | ' + board[5][8])
    print('-------------------------------------')
    print(board[6][0] + ' | ' + board[6][1] + ' | ' + board[6][2] + ' { ' + board[7][0] + ' | ' + board[7][1] + ' | ' + board[7][2] + ' } ' + board[8][0] + ' | ' + board[8][1] + ' | ' + board[8][2])
    print(board[6][3] + ' | ' + board[6][4] + ' | ' + board[6][5] + ' { ' + board[7][3] + ' | ' + board[7][4] + ' | ' + board[7][5] + ' } ' + board[8][3] + ' | ' + board[8][4] + ' | ' + board[8][5])
    print(board[6][6] + ' | ' + board[6][7] + ' | ' + board[6][8] + ' { ' + board[7][6] + ' | ' + board[7][7] + ' | ' + board[7][8] + ' } ' + board[8][6] + ' | ' + board[8][7] + ' | ' + board[8][8])

def initialize_used_numbers():
    usedNumbers = [[set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()],
                   [set(), set(), set(), set(), set(), set(), set(), set(), set()]]
    return usedNumbers

def decrement(blockPointer, indexPointer):
    if indexPointer == 0:
        blockPointer -= 1
        indexPointer = 7
    elif indexPointer != 0:
        indexPointer -= 2
    return (blockPointer, indexPointer)

def solve(board):
    solved = back = False
    usedNumbers = initialize_used_numbers()
    blockPointer = 0
    indexPointer = -1
    constantBoard = copy.deepcopy(board)
    number = 0
    while not solved:

        indexPointer += 1

        if indexPointer > 8:
            blockPointer += 1
            indexPointer = 0

        if blockPointer == 8 and indexPointer == 8:
            solved = True

        if back and len(usedNumbers[blockPointer][indexPointer]) == 0:
            blockPointer, indexPointer = decrement(blockPointer, indexPointer)
            continue

        if constantBoard[blockPointer][indexPointer] != " ":
            continue

        # Fill up a cell with a unique solution?
        number = get_a_possible_number(blockPointer, indexPointer, usedNumbers)
        back = False

        # No solution, we must go back
        if number == 0:
            print("Turning back...")
            board[blockPointer][indexPointer] = " "
            usedNumbers[blockPointer][indexPointer] = set()
            back = True
            blockPointer, indexPointer = decrement(blockPointer, indexPointer)
            continue

        board[blockPointer][indexPointer] = number
        usedNumbers[blockPointer][indexPointer].add(number)


    return board

print_board(solve(board))

