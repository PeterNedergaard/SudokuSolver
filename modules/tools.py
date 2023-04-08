import pandas as pd


def nums_to_grid(nums):

    matrix = [nums[i:i + 9] for i in range(0, 81, 9)]

    row_labels = ['r'+str(x) for x in list(range(9))]
    col_labels = ['c'+str(x) for x in list(range(9))]

    grid = pd.DataFrame(matrix, columns=col_labels, index=row_labels)

    # grids = [[], [], [],
    #          [], [], [],
    #          [], [], []]
    #
    # for index, num in enumerate(nums):
    #     r = index // 9
    #     c = index % 9
    #
    #     grid_index = ((r // 3) * 3) + (c // 3)
    #
    #     grids[grid_index].append({'index': index, 'num': num})

    # grid_row_offset = 0
    # grid_offset = 0
    # for i in range(3):
    #     grid_col_offset = 0
    #
    #     for j in range(3):
    #         row_offset = 0
    #
    #         for k in range(3):
    #
    #             for p in range(3):
    #                 slot_index = p + grid_row_offset + grid_col_offset + row_offset
    #                 grids[j + grid_offset].append({'index': slot_index, 'num': nums[slot_index]})
    #
    #             row_offset += 9
    #
    #         grid_col_offset += 3
    #
    #     grid_row_offset += 27
    #     grid_offset += 3

    return grid


def grid_to_nums(grid):
    # nums = []
    # for i in range(3):
    #
    #     for j in range(3):
    #
    #         for k in range(3):
    #
    #             for p in range(3):
    #                 nums.append(grids[(i*3) + k][(j*3) + p]['num'])

    return grid.values.flatten().tolist()


# def pretty_print(nums):
#
#     slot_index = 0
#
#     for i in range(3):
#         if i > 0:
#             print('---------------------')
#         for j in range(3):
#             for k in range(3):
#                 for p in range(3):
#                     print(nums[slot_index], end='')
#
#                     if p < 2:
#                         print(' ', end='')
#
#                     slot_index += 1
#                 if k < 2:
#                     print(' | ', end='')
#
#             print()
