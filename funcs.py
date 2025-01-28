import numpy as np

from sudoku_config import nrow, ncol


def is_valide(sudoku, output=False):
    valide = True
    for i in range(9):
        to_test = {}
        to_test['row'] = sudoku[i,:]
        to_test['col'] = sudoku[:,i]
        i_s, j_s = i-i%3, (i%3)*3
        to_test['square'] = sudoku[i_s:i_s+3,j_s:j_s+3]
        
        for t in to_test.values():
            unique, counts = np.unique(t, return_counts=True)
            for k,c in zip(unique,counts):
                if not k==0 and c>1:
                    valide=False
    return valide

def is_complete(sudoku, output=False):
    return np.all(sudoku)

def is_solved(sudoku, output=False):
    if is_complete(sudoku) and is_valide(sudoku):
        print('The sudoku is resolved. ')
    elif output and not is_valide(sudoku):
        print('The sudoku is impossible. ')
    elif output and not is_complete(sudoku):
        print('The sudoku is not complet. ')
    return is_complete(sudoku) and is_valide(sudoku)


def show(sudoku):
    print("\n-------------------------")

    for i in range(9):
        for j in range(9):
            if sudoku[i,j] is not None:
                if j == 0:
                    print("|", end=" ")
                print(f"{sudoku[i,j]} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        if (i + 1) % 3 == 0:
            print("\n-------------------------", end=" ")
        print()

