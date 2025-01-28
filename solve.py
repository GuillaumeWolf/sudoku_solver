import numpy as np
import time


import sudoku_config as conf
from funcs import show, is_solved, is_valide, is_complete


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
        # if len(all_sudokus)>=1: continue ## only to get one solution
        new_sudoku = np.copy(sudoku)
        new_sudoku[i0,j0] = k
        if not is_valide(new_sudoku, output=output): 
            # print(f'{i0=},{j0=},{k=} \n')
            continue
        all_sudokus += solve(new_sudoku, output=output)

    return all_sudokus






stest = conf.s2
t0 = time.time()
all_sudokus = solve(stest,output=False)
dt = time.time()-t0
print(f'Time to solve all possibilities: {dt:.2f} s. ')

print('\n\n\nInitial sudoku:')
show(stest)
print(f'\n\n{len(all_sudokus)} solutions were founds:')
for s in all_sudokus:
    show(s)



# show(stest)
# print(is_valide(stest))
# print(is_complete(stest))


