import pandas as pd
import numpy as np
import modules.slot_info as info

# data = pd.read_csv('sudoku.csv')
#
# split_col1 = data['quizzes'].apply(lambda x: pd.Series(list(x))).astype(int)
# split_col2 = data['solutions'].apply(lambda x: pd.Series(list(x))).astype(int)
# result = pd.concat([split_col1, split_col2], axis=1)
# result.columns = [f'f{i+1}' for i in range(81)] + [f't{i+1}' for i in range(81)]
# result.to_csv('sudoku_processed.csv', index=False)

data = pd.read_csv('sudoku_processed.csv', nrows=10)

quiz = data.iloc[:, :81]

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
                slot_index = p + grid_row_offset + grid_col_offset + row_offset
                grids[j+grid_offset].append({'index': slot_index, 'num': test_quiz[slot_index]})

            row_offset += 9

        grid_col_offset += 3

    grid_row_offset += 27
    grid_offset += 3


empty_slots = 0
for grid in grids:
    empty_slots += grid.count(0)

print(grids)
# print(info.get_grid_nums(grids, 4))
print(info.get_vert_nums(grids, 4, 5))


slot_list = []
for grid in grids:
    temp_grid = []
    for num in grid:
        if num != 0:
            temp_grid.append([num])
            continue

    slot_list.append(temp_grid)
