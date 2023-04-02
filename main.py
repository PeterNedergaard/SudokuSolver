import pandas as pd
import numpy as np

data = pd.read_csv('sudoku_processed.csv', nrows=10)

quiz = data.iloc[:, :81]
solution = data.iloc[:, 81:]

test_quiz = quiz.iloc[0]
grids = [[], [], [],
         [], [], [],
         [], [], []]


grid_row_offset = 0
grid_offset = 0
for i in range(3):
    grid_col_offset = 0

    for j in range(3):
        row_offset = 0

        for k in range(3):

            for p in range(3):
                grids[j+grid_offset].append(test_quiz[p + grid_row_offset + grid_col_offset + row_offset])

            row_offset += 9

        grid_col_offset += 3

    grid_row_offset += 27
    grid_offset += 3


for grid in grids:
    print(grid)


# quiz_index = 0
# for i in range(1, 10):
#     temp_grid = []
#
#     for j in range(1, 10):
#         temp_grid.append(test_quiz[quiz_index])
#         quiz_index += 1
#
#     grids.append(temp_grid)


# print(test_quiz.values)
# print(grids)
