# Use this to watch how the program solves the sudoku puzzle, no additional modules need to be installed.

import turtle
import math
import copy
import time


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

wn = turtle.Screen()
wn.title("Sudoku game - GUI with optimised visualization")
wn.bgcolor("white")

xPos = [-298, -226, -154, -82, -10, 62, 134, 206, 278]
yPos = [265, 193, 121, 49, -23, -95, -167, -239, -311]

tablepen = turtle.Turtle()
tablepen.speed(0)
tablepen.color("black")
tablepen.penup()
tablepen.setposition(-324, -324)
tablepen.pensize(4)
tablepen.pendown()
tablepen.hideturtle()

def draw_table():
    for side in range(4):
        tablepen.forward(648)
        tablepen.left(90)
    tablepen.left(90)
    for i in range(-108, 540, 216):
        tablepen.penup()
        tablepen.setposition(i, -324)
        tablepen.pendown()
        tablepen.forward(648)
    tablepen.left(90)
    for j in range(-108, 540, 216):
        tablepen.penup()
        tablepen.setposition(324, j)
        tablepen.pendown()
        tablepen.forward(648)

    tablepen.pensize(1)
    tablepen.left(180)

    for i in range(-252, 396, 72):
        tablepen.penup()
        tablepen.setposition(-324, i)
        tablepen.pendown()
        tablepen.forward(648)
    tablepen.left(90)
    for j in range(-252, 396, 72):
        tablepen.penup()
        tablepen.setposition(j, -324)
        tablepen.pendown()
        tablepen.forward(648)

draw_table()

var_pen = turtle.Turtle()
var_pen.speed(0)
var_pen.color("red")
var_pen.penup()
var_pen.setposition(0, -275)
var_pen.pensize(4)
var_pen.pendown()
var_pen.hideturtle()

const_pen = turtle.Turtle()
const_pen.speed(0)
const_pen.color("black")
const_pen.penup()
const_pen.setposition(0, -275)
const_pen.pensize(4)
const_pen.pendown()
const_pen.hideturtle()

def draw(xPos, yPos, text, writer):
    writer.penup()
    writer.setposition(xPos, yPos)
    writer.pendown()
    writer.write(text, False, align="left", font=("Arial", 30, "normal"))

def draw_individual(block, index, writer, Board):
    draw_tool = [[lambda: draw(xPos[0], yPos[0], board[0][0], writer),
                  lambda: draw(xPos[1], yPos[0], board[0][1], writer),
                  lambda: draw(xPos[2], yPos[0], board[0][2], writer),
                  lambda: draw(xPos[0], yPos[1], board[0][3], writer),
                  lambda: draw(xPos[1], yPos[1], board[0][4], writer),
                  lambda: draw(xPos[2], yPos[1], board[0][5], writer),
                  lambda: draw(xPos[0], yPos[2], board[0][6], writer),
                  lambda: draw(xPos[1], yPos[2], board[0][7], writer),
                  lambda: draw(xPos[2], yPos[2], board[0][8], writer)],

                 [lambda: draw(xPos[3], yPos[0], board[1][0], writer),
                  lambda: draw(xPos[4], yPos[0], board[1][1], writer),
                  lambda: draw(xPos[5], yPos[0], board[1][2], writer),
                  lambda: draw(xPos[3], yPos[1], board[1][3], writer),
                  lambda: draw(xPos[4], yPos[1], board[1][4], writer),
                  lambda: draw(xPos[5], yPos[1], board[1][5], writer),
                  lambda: draw(xPos[3], yPos[2], board[1][6], writer),
                  lambda: draw(xPos[4], yPos[2], board[1][7], writer),
                  lambda: draw(xPos[5], yPos[2], board[1][8], writer)],

                 [lambda: draw(xPos[6], yPos[0], board[2][0], writer),
                  lambda: draw(xPos[7], yPos[0], board[2][1], writer),
                  lambda: draw(xPos[8], yPos[0], board[2][2], writer),
                  lambda: draw(xPos[6], yPos[1], board[2][3], writer),
                  lambda: draw(xPos[7], yPos[1], board[2][4], writer),
                  lambda: draw(xPos[8], yPos[1], board[2][5], writer),
                  lambda: draw(xPos[6], yPos[2], board[2][6], writer),
                  lambda: draw(xPos[7], yPos[2], board[2][7], writer),
                  lambda: draw(xPos[8], yPos[2], board[2][8], writer)],

                 [lambda: draw(xPos[0], yPos[3], board[3][0], writer),
                  lambda: draw(xPos[1], yPos[3], board[3][1], writer),
                  lambda: draw(xPos[2], yPos[3], board[3][2], writer),
                  lambda: draw(xPos[0], yPos[4], board[3][3], writer),
                  lambda: draw(xPos[1], yPos[4], board[3][4], writer),
                  lambda: draw(xPos[2], yPos[4], board[3][5], writer),
                  lambda: draw(xPos[0], yPos[5], board[3][6], writer),
                  lambda: draw(xPos[1], yPos[5], board[3][7], writer),
                  lambda: draw(xPos[2], yPos[5], board[3][8], writer)],

                 [lambda: draw(xPos[3], yPos[3], board[4][0], writer),
                  lambda: draw(xPos[4], yPos[3], board[4][1], writer),
                  lambda: draw(xPos[5], yPos[3], board[4][2], writer),
                  lambda: draw(xPos[3], yPos[4], board[4][3], writer),
                  lambda: draw(xPos[4], yPos[4], board[4][4], writer),
                  lambda: draw(xPos[5], yPos[4], board[4][5], writer),
                  lambda: draw(xPos[3], yPos[5], board[4][6], writer),
                  lambda: draw(xPos[4], yPos[5], board[4][7], writer),
                  lambda: draw(xPos[5], yPos[5], board[4][8], writer)],

                 [lambda: draw(xPos[6], yPos[3], board[5][0], writer),
                  lambda: draw(xPos[7], yPos[3], board[5][1], writer),
                  lambda: draw(xPos[8], yPos[3], board[5][2], writer),
                  lambda: draw(xPos[6], yPos[4], board[5][3], writer),
                  lambda: draw(xPos[7], yPos[4], board[5][4], writer),
                  lambda: draw(xPos[8], yPos[4], board[5][5], writer),
                  lambda: draw(xPos[6], yPos[5], board[5][6], writer),
                  lambda: draw(xPos[7], yPos[5], board[5][7], writer),
                  lambda: draw(xPos[8], yPos[5], board[5][8], writer)],

                 [lambda: draw(xPos[0], yPos[6], board[6][0], writer),
                  lambda: draw(xPos[1], yPos[6], board[6][1], writer),
                  lambda: draw(xPos[2], yPos[6], board[6][2], writer),
                  lambda: draw(xPos[0], yPos[7], board[6][3], writer),
                  lambda: draw(xPos[1], yPos[7], board[6][4], writer),
                  lambda: draw(xPos[2], yPos[7], board[6][5], writer),
                  lambda: draw(xPos[0], yPos[8], board[6][6], writer),
                  lambda: draw(xPos[1], yPos[8], board[6][7], writer),
                  lambda: draw(xPos[2], yPos[8], board[6][8], writer)],

                 [lambda: draw(xPos[3], yPos[6], board[7][0], writer),
                  lambda: draw(xPos[4], yPos[6], board[7][1], writer),
                  lambda: draw(xPos[5], yPos[6], board[7][2], writer),
                  lambda: draw(xPos[3], yPos[7], board[7][3], writer),
                  lambda: draw(xPos[4], yPos[7], board[7][4], writer),
                  lambda: draw(xPos[5], yPos[7], board[7][5], writer),
                  lambda: draw(xPos[3], yPos[8], board[7][6], writer),
                  lambda: draw(xPos[4], yPos[8], board[7][7], writer),
                  lambda: draw(xPos[5], yPos[8], board[7][8], writer)],

                 [lambda: draw(xPos[6], yPos[6], board[8][0], writer),
                  lambda: draw(xPos[7], yPos[6], board[8][1], writer),
                  lambda: draw(xPos[8], yPos[6], board[8][2], writer),
                  lambda: draw(xPos[6], yPos[7], board[8][3], writer),
                  lambda: draw(xPos[7], yPos[7], board[8][4], writer),
                  lambda: draw(xPos[8], yPos[7], board[8][5], writer),
                  lambda: draw(xPos[6], yPos[8], board[8][6], writer),
                  lambda: draw(xPos[7], yPos[8], board[8][7], writer),
                  lambda: draw(xPos[8], yPos[8], board[8][8], writer)]]
    if Board[block][index] == " ":
        draw_tool[block][index]()

def draw_board(Board):
    draw_tool = [[lambda: draw(xPos[0], yPos[0], board[0][0], const_pen),
                  lambda: draw(xPos[1], yPos[0], board[0][1], const_pen),
                  lambda: draw(xPos[2], yPos[0], board[0][2], const_pen),
                  lambda: draw(xPos[0], yPos[1], board[0][3], const_pen),
                  lambda: draw(xPos[1], yPos[1], board[0][4], const_pen),
                  lambda: draw(xPos[2], yPos[1], board[0][5], const_pen),
                  lambda: draw(xPos[0], yPos[2], board[0][6], const_pen),
                  lambda: draw(xPos[1], yPos[2], board[0][7], const_pen),
                  lambda: draw(xPos[2], yPos[2], board[0][8], const_pen)],

                 [lambda: draw(xPos[3], yPos[0], board[1][0], const_pen),
                  lambda: draw(xPos[4], yPos[0], board[1][1], const_pen),
                  lambda: draw(xPos[5], yPos[0], board[1][2], const_pen),
                  lambda: draw(xPos[3], yPos[1], board[1][3], const_pen),
                  lambda: draw(xPos[4], yPos[1], board[1][4], const_pen),
                  lambda: draw(xPos[5], yPos[1], board[1][5], const_pen),
                  lambda: draw(xPos[3], yPos[2], board[1][6], const_pen),
                  lambda: draw(xPos[4], yPos[2], board[1][7], const_pen),
                  lambda: draw(xPos[5], yPos[2], board[1][8], const_pen)],

                 [lambda: draw(xPos[6], yPos[0], board[2][0], const_pen),
                  lambda: draw(xPos[7], yPos[0], board[2][1], const_pen),
                  lambda: draw(xPos[8], yPos[0], board[2][2], const_pen),
                  lambda: draw(xPos[6], yPos[1], board[2][3], const_pen),
                  lambda: draw(xPos[7], yPos[1], board[2][4], const_pen),
                  lambda: draw(xPos[8], yPos[1], board[2][5], const_pen),
                  lambda: draw(xPos[6], yPos[2], board[2][6], const_pen),
                  lambda: draw(xPos[7], yPos[2], board[2][7], const_pen),
                  lambda: draw(xPos[8], yPos[2], board[2][8], const_pen)],


                 [lambda: draw(xPos[0], yPos[3], board[3][0], const_pen),
                  lambda: draw(xPos[1], yPos[3], board[3][1], const_pen),
                  lambda: draw(xPos[2], yPos[3], board[3][2], const_pen),
                  lambda: draw(xPos[0], yPos[4], board[3][3], const_pen),
                  lambda: draw(xPos[1], yPos[4], board[3][4], const_pen),
                  lambda: draw(xPos[2], yPos[4], board[3][5], const_pen),
                  lambda: draw(xPos[0], yPos[5], board[3][6], const_pen),
                  lambda: draw(xPos[1], yPos[5], board[3][7], const_pen),
                  lambda: draw(xPos[2], yPos[5], board[3][8], const_pen)],

                 [lambda: draw(xPos[3], yPos[3], board[4][0], const_pen),
                  lambda: draw(xPos[4], yPos[3], board[4][1], const_pen),
                  lambda: draw(xPos[5], yPos[3], board[4][2], const_pen),
                  lambda: draw(xPos[3], yPos[4], board[4][3], const_pen),
                  lambda: draw(xPos[4], yPos[4], board[4][4], const_pen),
                  lambda: draw(xPos[5], yPos[4], board[4][5], const_pen),
                  lambda: draw(xPos[3], yPos[5], board[4][6], const_pen),
                  lambda: draw(xPos[4], yPos[5], board[4][7], const_pen),
                  lambda: draw(xPos[5], yPos[5], board[4][8], const_pen)],

                 [lambda: draw(xPos[6], yPos[3], board[5][0], const_pen),
                  lambda: draw(xPos[7], yPos[3], board[5][1], const_pen),
                  lambda: draw(xPos[8], yPos[3], board[5][2], const_pen),
                  lambda: draw(xPos[6], yPos[4], board[5][3], const_pen),
                  lambda: draw(xPos[7], yPos[4], board[5][4], const_pen),
                  lambda: draw(xPos[8], yPos[4], board[5][5], const_pen),
                  lambda: draw(xPos[6], yPos[5], board[5][6], const_pen),
                  lambda: draw(xPos[7], yPos[5], board[5][7], const_pen),
                  lambda: draw(xPos[8], yPos[5], board[5][8], const_pen)],


                 [lambda: draw(xPos[0], yPos[6], board[6][0], const_pen),
                  lambda: draw(xPos[1], yPos[6], board[6][1], const_pen),
                  lambda: draw(xPos[2], yPos[6], board[6][2], const_pen),
                  lambda: draw(xPos[0], yPos[7], board[6][3], const_pen),
                  lambda: draw(xPos[1], yPos[7], board[6][4], const_pen),
                  lambda: draw(xPos[2], yPos[7], board[6][5], const_pen),
                  lambda: draw(xPos[0], yPos[8], board[6][6], const_pen),
                  lambda: draw(xPos[1], yPos[8], board[6][7], const_pen),
                  lambda: draw(xPos[2], yPos[8], board[6][8], const_pen)],

                 [lambda: draw(xPos[3], yPos[6], board[7][0], const_pen),
                  lambda: draw(xPos[4], yPos[6], board[7][1], const_pen),
                  lambda: draw(xPos[5], yPos[6], board[7][2], const_pen),
                  lambda: draw(xPos[3], yPos[7], board[7][3], const_pen),
                  lambda: draw(xPos[4], yPos[7], board[7][4], const_pen),
                  lambda: draw(xPos[5], yPos[7], board[7][5], const_pen),
                  lambda: draw(xPos[3], yPos[8], board[7][6], const_pen),
                  lambda: draw(xPos[4], yPos[8], board[7][7], const_pen),
                  lambda: draw(xPos[5], yPos[8], board[7][8], const_pen)],

                 [lambda: draw(xPos[6], yPos[6], board[8][0], const_pen),
                  lambda: draw(xPos[7], yPos[6], board[8][1], const_pen),
                  lambda: draw(xPos[8], yPos[6], board[8][2], const_pen),
                  lambda: draw(xPos[6], yPos[7], board[8][3], const_pen),
                  lambda: draw(xPos[7], yPos[7], board[8][4], const_pen),
                  lambda: draw(xPos[8], yPos[7], board[8][5], const_pen),
                  lambda: draw(xPos[6], yPos[8], board[8][6], const_pen),
                  lambda: draw(xPos[7], yPos[8], board[8][7], const_pen),
                  lambda: draw(xPos[8], yPos[8], board[8][8], const_pen)]]
    for i in range(9):
        for j in range(9):
            if Board[i][j] != " ":
                draw_tool[i][j]()

def undo_individual():
    for i in range(4):
        var_pen.undo()

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

        # When we reach the end we leave
        if blockPointer == 8 and indexPointer == 8:
            solved = True

        # We are going back and it happens to be an inactive cell
        if back and len(usedNumbers[blockPointer][indexPointer]) == 0:
            blockPointer, indexPointer = decrement(blockPointer, indexPointer)
            continue

        # We are going forward, lets not edit an inactive cell
        if constantBoard[blockPointer][indexPointer] != " ":
            continue

        # Fill up a cell with a unique solution?
        number = get_a_possible_number(blockPointer, indexPointer, usedNumbers)

        if number == 0:
            board[blockPointer][indexPointer] = " "
            usedNumbers[blockPointer][indexPointer] = set()
            undo_individual()
            back = True
            blockPointer, indexPointer = decrement(blockPointer, indexPointer)
            continue
        
        # We found a unique solution, lets fill the cell up and not use it again
        back = False
        board[blockPointer][indexPointer] = number
        usedNumbers[blockPointer][indexPointer].add(number)
        draw_individual(blockPointer, indexPointer, var_pen, constantBoard)

    return board

draw_board(board)
solve(board)

wn.mainloop()
