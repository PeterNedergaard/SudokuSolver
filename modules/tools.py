
def nums_to_grid(nums):
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
                    grids[j + grid_offset].append({'index': slot_index, 'num': nums[slot_index]})

                row_offset += 9

            grid_col_offset += 3

        grid_row_offset += 27
        grid_offset += 3

    return grids


def pretty_print(nums):

    slot_index = 0

    for i in range(3):
        if i > 0:
            print('---------------------')
        for j in range(3):
            for k in range(3):
                for p in range(3):
                    print(nums[slot_index], end='')

                    if p < 2:
                        print(' ', end='')

                    slot_index += 1
                if k < 2:
                    print(' | ', end='')

            print()
