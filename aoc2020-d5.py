def calculate_seat_id(ticket):
    row_binary = ''.join(['1' if char == 'B' else '0' for char in ticket[0:7]])
    row = int(row_binary, 2)

    column_binary = ''.join(['1' if char == 'R' else '0' for char in ticket[7:]])
    column = int(column_binary, 2)

    seat_id = row * 8 + column
    print(f'Ticket: {ticket}. Seat ID: {seat_id}. Found row: {row} ({row_binary}), column: {column} ({column_binary})')
    return seat_id


def find_missing_sequential_seat(seat_id_list):
    seat_id_list.sort()
    print(f'Sorted seat ID list: {seat_id_list}')
    for idx, seat_id in enumerate(seat_id_list, start=seat_id_list[0]):
        if idx != seat_id:
            print(f'Found missing seat ID: {idx}')
            return seat_id

def run_case(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    seat_id_list = [ calculate_seat_id(line) for line in lines ]
    print(f'Found max seat ID: {max(seat_id_list)} in seat_id_list: {seat_id_list}')

    my_seat_id = find_missing_sequential_seat(seat_id_list)




if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-d5p1.txt']
    for filename in filenames:
        run_case(filename)