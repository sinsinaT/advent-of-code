"""day 4 - advent of code"""
import itertools as it

import numpy as np


def make_boards(lines):
    boards = []
    for i in lines:
        board = np.zeros((5, 5), dtype=int)
        called = np.zeros((5, 5), dtype=bool)
        for ii, line in enumerate(i.splitlines()):
            for j, val in enumerate(line.split()):
                board[ii][j] = int(val)
        boards.append((board, called))
    return boards


def marknumber(board, number):
    board, called = board
    called[np.where(board == number)] = True


def checkwin(board):
    board, called = board
    return np.any(np.all(called, axis=0)) or np.any(np.all(called, axis=1))


def get_sum_unmarked(board):
    board, called = board
    return np.sum(board[called == False])


def play_bingo(file_):
    data = open(file_).read()
    stuff = data.split("\n\n")
    numbers = stuff[0]
    print(stuff[1:])
    boards = make_boards(stuff[1:])
    print(boards)

    for n in map(int, numbers.strip().split(",")):
        # import pdb;pdb.set_trace()
        for board in boards:
            marknumber(board, n)
            haswon = checkwin(board)

            if haswon:
                s = get_sum_unmarked(board)
                return s * n


def play_bingo_part2(file_):
    data = open(file_).read()
    stuff = data.split("\n\n")
    numbers = stuff[0]
    boards = make_boards(stuff[1:])

    winningscores = []
    skipboards = []
    for n in map(int, numbers.strip().split(",")):
        # import pdb;pdb.set_trace()
        for i, board in enumerate(boards):
            marknumber(board, n)
            haswon = checkwin(board)

            if haswon and not i in skipboards:
                s = get_sum_unmarked(board)
                winningscores.append(s * n)
                skipboards.append(i)
    return winningscores[-1]


def main():
    # part 1
    part1 = play_bingo("input.txt")
    print(part1)
    # part 2
    part2 = play_bingo_part2("input.txt")
    print(part2)


if __name__ == "__main__":
    main()
