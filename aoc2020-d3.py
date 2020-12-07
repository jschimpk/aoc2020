def find_num_trees_any_slope_d(lines, slope_r, slope_d):
    # Find line length to handle wrap condition
    width = len(lines[0])

    pos_x = 0
    pos_y = 0
    num_trees = 0

    for line in lines:
        # Only check lines for each multiple of slope_d
        if pos_y % slope_d != 0:
            pos_y += 1
            continue
        if line[pos_x] == '#':
            num_trees += 1
        # Update position
        pos_x += slope_r
        pos_y += 1
        # Handle wrap to the right
        pos_x %= width

    return num_trees


def find_num_trees(lines, slope_r):
    # Find line length to handle wrap condition
    width = len(lines[0])

    pos_x = 0
    num_trees = 0

    for line in lines:
        if line[pos_x] == '#':
            num_trees += 1
        # Update position
        pos_x += slope_r
        # Handle wrap to the right
        pos_x %= width

    return num_trees

def run_case(filename, slope_r, slope_d):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    print(f'Opened {filename}. Calculating num trees hit with slope: {slope_r}, {slope_d}')
    if slope_d == 1:
        # We can do it line by line. Hurrah!
        num_trees = find_num_trees(lines, slope_r)
    else:
        num_trees = find_num_trees_any_slope_d(lines, slope_r, slope_d)

    print(f'Encountered {num_trees} trees on our journey!')
    return num_trees


if __name__ == '__main__':
    # P1
    print('Running P1')
    filenames = ['input-sample.txt', 'input-d3p1.txt']
    for filename in filenames:
        run_case(filename, 3, 1)

    #P2
    print('Running P2')
    slope_list = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    filenames = ['input-sample.txt', 'input-d3p1.txt']
    for filename in filenames:
        num_trees_list = []
        for slope in slope_list:
            num_trees_list.append(run_case(filename, slope[0], slope[1]))

        trees_product = 1
        for num_trees in num_trees_list:
            trees_product *= num_trees
        print(f'Multiplied together: {trees_product}')