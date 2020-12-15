import copy


def occupied_seat_in_los(x, y, slope, seat_grid):
    x_max = len(seat_grid[0])
    y_max = len(seat_grid)

    x += slope[1]
    y += slope[0]
    while x >= 0 and x < x_max and y >= 0 and y < y_max:
        if seat_grid[y][x] == '#':
            return True
        if seat_grid[y][x] == 'L':
            return False
        x += slope[1]
        y += slope[0]

    return False


def apply_rules_to_seat(x, y, seat_grid):

    slopes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    occupied_seats = 0
    # Check line of sight in each direction
    for slope in slopes:
        if occupied_seat_in_los(x, y, slope, seat_grid):
            occupied_seats += 1

    if seat_grid[y][x] == 'L':
        if occupied_seats == 0:
            return '#'
    if seat_grid[y][x] == '#':
        if occupied_seats > 4:
            return 'L'
    return seat_grid[y][x]


def do_p2(seat_grid):
    changed = 'Yes'
    # Initialize new seat grid with same size
    new_seat_grid = copy.deepcopy(seat_grid)
    while changed == 'Yes':
        #print(f'Seat grid:')
        #for line in seat_grid:
        #    print(''.join(line))
        changed = 'No'
        for y in range(0, len(seat_grid)):
            for x in range(0,len(seat_grid[0])):
                new_seat_grid[y][x] = apply_rules_to_seat(x, y, seat_grid)
                if new_seat_grid[y][x] != seat_grid[y][x]:
                    changed = 'Yes'
        seat_grid = copy.deepcopy(new_seat_grid)

    print(f'Final seat_grid:')
    for line in seat_grid:
        print(''.join(line))
    occupied_seats = sum([line.count('#') for line in seat_grid])
    print(f'Occupied seats: {occupied_seats}')


def create_neighbor_grid(x, y, seat_grid):
    # Get handy local maximums
    x_max = len(seat_grid[0]) - 1
    y_max = len(seat_grid) - 1
    # Initialize it to all floor. Anything outside of grid considered floor
    grid = [['.','.','.'],['.','.','.'],['.','.','.']]

    for y_adj in [-1, 0, 1]:
        for x_adj in [-1, 0, 1]:
            lookup_x = x + x_adj
            lookup_y = y + y_adj
            if lookup_x < 0 or lookup_x > x_max or lookup_y < 0 or lookup_y > y_max:
                continue
            grid[y_adj + 1][x_adj + 1] = seat_grid[lookup_y][lookup_x]
    return grid


def apply_rules_to_neighbor_grid(grid):
    occupied_seats = sum([line.count('#') for line in grid])
    if grid[1][1] == 'L':
        if occupied_seats == 0:
            return '#'
    if grid[1][1] == '#':
        if occupied_seats > 4:
            return 'L'
    return grid[1][1]


def do_p1(seat_grid):
    changed = 'Yes'
    # Initialize new seat grid with same size
    new_seat_grid = copy.deepcopy(seat_grid)

    while changed == 'Yes':
        #print(f'Seat grid:')
        #for line in seat_grid:
            #print(''.join(line))
        changed = 'No'
        for y in range(0, len(seat_grid)):
            for x in range(0,len(seat_grid[0])):
                if seat_grid[y][x] == '.':
                    continue
                grid = create_neighbor_grid(x, y, seat_grid)
                new_seat_grid[y][x] = apply_rules_to_neighbor_grid(grid)
                if new_seat_grid[y][x] != seat_grid[y][x]:
                    changed = 'Yes'
        seat_grid = copy.deepcopy(new_seat_grid)

    print(f'Final seat_grid:')
    for line in seat_grid:
        print(''.join(line))
    occupied_seats = sum([line.count('#') for line in seat_grid])
    print(f'Occupied seats: {occupied_seats}')


if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-d11.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            seat_grid = [ list(line) for line in f.read().splitlines() ]

        do_p1(seat_grid)
        do_p2(seat_grid)