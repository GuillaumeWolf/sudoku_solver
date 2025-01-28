import numpy as np
import time


import sudoku_config as conf
from funcs import show, can_add, is_solved, is_valide, is_complete


def first_empty_box(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i,j]==0: 
                return i,j
    return -1,-1


def solve(sudoku, output=False):
    if is_solved(sudoku,output=output): 
            return [sudoku]
    if is_complete(sudoku) and not is_valide(sudoku): 
        return []
    all_sudokus = []
    i0,j0 = first_empty_box(sudoku)
    for k in range(1,10):
        if not can_add(k,i0,j0,sudoku):
            continue
        new_sudoku = np.copy(sudoku)
        new_sudoku[i0,j0] = k
        all_sudokus += solve(new_sudoku, output=output)

    return all_sudokus






stest = conf.sfinal
t0 = time.time()
all_sudokus = solve(stest,output=False)
dt = time.time()-t0
print(f'Time to solve all possibilities: {dt:.2f} s. ')

print('\n\n\nInitial sudoku:')
show(stest)
print(f'\n\n{len(all_sudokus)} solutions were founds:')
for s in all_sudokus:
    show(s)





