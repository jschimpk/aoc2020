def calculate_quadrant(coord):
    if coord[0] >= 0 and coord[1] >= 0:
        return 0
    if coord[0] >= 0 and coord[1] < 0:
        return 1
    if coord[0] < 0 and coord[1] < 0:
        return 2
    if coord[0] < 0 and coord[1] >= 0:
        return 3
    print(f'Unknown quadrant: coord: {coord}')
    sys.exit()


def follow_instructions_p2(instructions):
    # Quadrants are organized like this:
    # .....|.....
    # ..3..|..0..
    # -----|-----
    # ..2..|..1..
    # .....|.....
    wp_quad = 0
    quad_signs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    wp_coord = (10, 1)

    turn_dict = {'L': -1, 'R': 1}
    turn_units = {90:1, 180:2, 270:3}
    position = (0, 0)
    bearing_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    for instr in instructions:
        op, unit = instr[0], int(instr[1:])
        #print(f'Coord: ({position[0]}, {position[1]}), wp_quad: {wp_quad}: wp_coord: ({wp_coord[0]}, {wp_coord[1]}), instr: {instr} => op: {op}, unit: {unit}')
        if wp_quad != calculate_quadrant(wp_coord):
            print(f'Incorrect wp_quad: {wp_quad}, should be: {calculate_quadrant(wp_coord)}')
            sys.exit()
        if op == 'N' or op == 'S' or op == 'E' or op == 'W':
            wp_coord = (wp_coord[0] + bearing_dict[op][0] * unit,
                        wp_coord[1] + bearing_dict[op][1] * unit)
            # Calculate quadrant in case we passed into a new one
            if calculate_quadrant(wp_coord) != wp_quad:
                wp_quad = calculate_quadrant(wp_coord)
                #print(f'New quadrant: {wp_quad}, new wp_coord: {wp_coord}')

        elif op == 'L' or op == 'R':
            wp_quad = (wp_quad + turn_dict[op] * turn_units[unit]) % 4
            if unit != 180:
                # Swap coords
                wp_coord = (wp_coord[1], wp_coord[0])

            # Adjust sign based on new quadrant
            wp_coord = (quad_signs[wp_quad][0] * abs(wp_coord[0]),
                        quad_signs[wp_quad][1] * abs(wp_coord[1]))
            # Handle edge cases where one coord is 0
            wp_quad = calculate_quadrant(wp_coord)
            #print(f'New wp_quad: {wp_quad}: wp_coord: ({wp_coord[0]}, {wp_coord[1]})')
        elif op == 'F':
            position = (position[0] + wp_coord[0] * unit,
                        position[1] + wp_coord[1] * unit)
        else:
            print('What happened?')

    return position[0], position[1]

def follow_instructions(instructions):
    # Setup bearing list in order
    bearing_list = ['N', 'E', 'S', 'W']
    bearing_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    turn_dict = {'L': -1, 'R': 1}
    # Initial bearing is East
    bearing = 1
    position = (0, 0)
    for instr in instructions:
        op, unit = instr[0], int(instr[1:])
        #print(f'Coord: ({position[0]}, {position[1]}), bearing: {bearing_list[bearing]}: instr: {instr} => op: {op}, unit: {unit}')
        if op == 'L' or op == 'R':
            bearing = (bearing + turn_dict[op] * int(unit / 90)) % 4
            continue

        if op == 'F':
            # Substitute bearing in for op to use common logic
            op = bearing_list[bearing]

        # Common logic using bearing lookup
        position = (position[0] + bearing_dict[op][0] * unit,
                    position[1] + bearing_dict[op][1] * unit)

    return position


if __name__ == '__main__':
    filenames = ['input-sample-d12.txt', 'input-d12.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            instructions = f.read().splitlines()
            x, y = follow_instructions(instructions)
            print(f'Final coordinates: {x}, {y}. Sum: {abs(x)+abs(y)}')
            #print(20 * f'============================================\n')
            x, y = follow_instructions_p2(instructions)
            print(f'Final coordinates P2: {x}, {y}. Sum: {abs(x) + abs(y)}')