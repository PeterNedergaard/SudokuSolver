import pandas as pd
import numpy as np
import modules.slot_info as info
import modules.tools as tools

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

grids = tools.nums_to_grid(test_quiz)


# print(grids)
# print(info.get_grid_nums(grids, 4))
# print(info.get_y_nums(grids[2][4]['index'], test_quiz))
# print(info.get_x_nums(grids[8][8]['index'], test_quiz))
print(info.get_possible_nums(6, 0, test_quiz))
tools.pretty_print(test_quiz)
