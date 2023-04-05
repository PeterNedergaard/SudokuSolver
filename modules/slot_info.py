import modules.tools as tools


def get_grid_nums(grids, grid_index):
    nums = [d['num'] for d in grids[grid_index]]

    return nums


def get_y_nums(slot_index, quiz_nums):
    nums = []

    index = slot_index
    direction = False
    while True:

        if direction:
            index += 9
        else:
            index -= 9

        if index <= 8:
            index = slot_index
            direction = True

        if index >= 72:
            break

        nums.append(quiz_nums[index])

    return nums


def get_x_nums(slot_index, quiz_nums):
    nums = []

    index = slot_index
    end_index = -1
    start_from_end = False
    while True:

        if (index+1) % 9 == 0:
            start_from_end = True
            end_index = index
        elif not start_from_end:
            index += 1
            continue

        nums.append(quiz_nums[index])

        index -= 1

        if index <= end_index-9:
            break

    return nums


def get_possible_nums(grid_index, index_in_grid, quiz_nums):
    grids = tools.nums_to_grid(quiz_nums)
    slot_index = grids[grid_index][index_in_grid]['index']

    all_nums = range(1, 10)
    nums = []
    nums.extend(get_grid_nums(grids, grid_index))
    nums.extend(get_y_nums(slot_index, quiz_nums))
    nums.extend(get_x_nums(slot_index, quiz_nums))

    unique_nums = set(nums)
    unique_nums.discard(0)

    possible_nums = [x for x in all_nums if x not in nums]

    print(list(unique_nums))

    return possible_nums

