
def get_grid_nums(grids, grid_index):
    unique_nums = set([d['num'] for d in grids[grid_index]])
    unique_nums.discard(0)

    return list(unique_nums)


def get_vert_nums(grids, grid_index, index_in_grid):
    slot_index = grids[grid_index][index_in_grid]['index']

    nums = []
    if slot_index < 10:
        print()

    return nums
