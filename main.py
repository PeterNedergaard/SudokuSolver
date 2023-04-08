import pandas as pd
import numpy as np
import modules.slot_info as info
import modules.tools as tools
import copy

# data = pd.read_csv('sudoku.csv')
#
# split_col1 = data['quizzes'].apply(lambda x: pd.Series(list(x))).astype(int)
# split_col2 = data['solutions'].apply(lambda x: pd.Series(list(x))).astype(int)
# result = pd.concat([split_col1, split_col2], axis=1)
# result.columns = [f'f{i+1}' for i in range(81)] + [f't{i+1}' for i in range(81)]
# result.to_csv('sudoku_processed.csv', index=False)

data = pd.read_csv('sudoku_processed.csv', nrows=10)
quiz = data.iloc[:, :81]
solution = data.iloc[:, 81:]
test_quiz = quiz.iloc[1]
test_solution = solution.iloc[1]
quiz_nums = test_quiz.values
solution_nums = test_solution.values

grid = tools.nums_to_grid(quiz_nums)


# print(grid)
# print(tools.grid_to_nums(grid))
# print(info.get_col_nums(grid, 6))
# print(info.get_row_nums(grid, 5))
# print(info.get_square_nums(grid, 5, 6))
# print(info.get_possible_nums(grid, 5, 6))
# print(info.fill_solo_slots(grid))

for i in range(10):
    print('Quiz ' + str(i))
    test_quiz = quiz.iloc[i]
    test_solution = solution.iloc[i]
    quiz_nums = test_quiz.values
    solution_nums = test_solution.values.flatten().tolist()
    grid = tools.nums_to_grid(quiz_nums)
    clue_count = info.clue_count(grid)

    print('Clues: ' + str(clue_count))

    if 32 <= clue_count <= 40:
        print('Easy')
    else:
        print('Other')

    # if tools.grid_to_nums(info.fill_solo_until_no_change(grid)) == solution_nums:
    #     print('Solved')
    # else:
    #     print('Not solved')

# test_grid = info.fill_solo_until_no_change(grid)

# print(test_grid)
# print(tools.nums_to_grid(solution_nums))
