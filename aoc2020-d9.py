def find_contiguous_sum_in_list(value, values):
    for idx1 in range(len(values) - 1):
        for idx2 in range(idx1, len(values)):
            slice = values[idx1:idx2]
            if value == sum(slice):
                print(f'Found contiguous sum from {idx1}-{idx2-1}')
                return min(slice), max(slice)
    return 0,0

def check_sl_wind_for_sum(value, window):
    for idx1, val1 in enumerate(window):
        if idx1 == len(window) - 1:
            return False
        for idx2, val2 in enumerate(window[idx1+1:]):
            sum = val1 + val2
            if value == sum:
                return True
    # Shouldn't reach here
    print('How is that even possible?')
    return False

def run_case(filename, window_sz=25):
    with open(filename, 'r') as f:
        values = [ int(x) for x in f.read().split() ]

    # P1
    window = values[0:window_sz]
    for value in values[window_sz:]:
        if not check_sl_wind_for_sum(value, window):
            break
        window.pop(0)
        window.append(value)
    print(f'{value} not found in previous window')
    # P2
    range_l, range_h = find_contiguous_sum_in_list(value, values)
    print(f'Found values: {range_l}, {range_h}, sum: {range_l + range_h}')


if __name__ == '__main__':
    run_case('input-sample.txt', 5)
    run_case('input-d9.txt', 25)