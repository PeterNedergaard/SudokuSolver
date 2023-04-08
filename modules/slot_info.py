import modules.tools as tools
import copy
import pandas as pd


def get_square_nums(grid, row, col):
    # nums = [d['num'] for d in grids[grid_index]]

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    square = [
        grid.values[start_row + r][start_col + c]
        for r in range(3)
        for c in range(3)
    ]
    return [x for x in set(square) if x != 0]


def get_col_nums(grid, col):
    # nums = []
    # index = slot_index
    # direction = False
    # while True:
    #
    #     if direction:
    #         index += 9
    #     else:
    #         index -= 9
    #
    #     if index <= 8:
    #         index = slot_index
    #         direction = True
    #
    #     if index >= 72:
    #         break
    #
    #     nums.append(quiz_nums[index])

    return [x for x in set(grid.iloc[:, col].values) if x != 0]


def get_row_nums(grid, row):
    # nums = []
    # index = slot_index
    # end_index = -1
    # start_from_end = False
    # while True:
    #
    #     if (index+1) % 9 == 0:
    #         start_from_end = True
    #         end_index = index
    #     elif not start_from_end:
    #         index += 1
    #         continue
    #
    #     nums.append(quiz_nums[index])
    #
    #     index -= 1
    #
    #     if index <= end_index-9:
    #         break

    return [x for x in set(grid.iloc[row].values) if x != 0]


def get_possible_nums(grid, row, col):
    all_nums = range(1, 10)
    unique_nums = set()
    unique_nums.update(get_square_nums(grid, row, col))
    unique_nums.update(get_col_nums(grid, col))
    unique_nums.update(get_row_nums(grid, row))

    unique_nums.discard(0)

    possible_nums = [x for x in all_nums if x not in unique_nums]

    return possible_nums


def fill_solo_slots(grid):
    def fill_solo(row):
        new_row = []
        for col, value in enumerate(row):
            if value == 0:
                row_index = int(str.split(row.name, 'r')[1])
                possible_nums = get_possible_nums(grid, row_index, col)

                if len(possible_nums) == 1:
                    new_row.append(possible_nums[0])
                    continue

            new_row.append(value)

        return pd.Series(new_row, index=row.index)

    temp_grid = grid.apply(fill_solo, axis=1)

    # quiz_nums = tools.grid_to_nums(grid)
    #
    # for index_i, grid in enumerate(grid):
    #     for index_j, num in enumerate(grid):
    #         if num['num'] == 0:
    #             possible_nums = get_possible_nums(grid, index_i, index_j)
    #
    #             if len(possible_nums) == 1:
    #                 temp_grid[index_i][index_j]['num'] = possible_nums[0]

    return temp_grid


def fill_solo_until_no_change(grid):
    test_grid = copy.deepcopy(grid)
    no_change = False

    while not no_change:
        prev_grid = test_grid
        test_grid = fill_solo_slots(test_grid)

        if tools.grid_to_nums(prev_grid) == tools.grid_to_nums(test_grid):
            # print('No change')
            no_change = True
        # else:
        #     print('Changed')

    return test_grid


def clue_count(grid):
    non_zero_mask = grid.ne(0)
    non_zero_count = non_zero_mask.sum().sum()

    return non_zero_count
