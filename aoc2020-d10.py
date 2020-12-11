ones_map = {}

def create_consecutive_ones_map():
    ones_map[1] = 1
    ones_map[2] = 2
    ones_map[3] = 4
    ones_map[4] = 7


def make_consecutive_ones_count_list(diff_list):
    ones_count_list = []
    in_ones_sequence = 'No'
    for idx in range(0, num_values - 1):
        if diff_list[idx] == 1 and in_ones_sequence == 'No':
            # Start of ones sequence. Begin counting
            in_ones_sequence = 'Yes'
            num_ones = 1
            continue
        if diff_list[idx] == 1:
            num_ones += 1
            continue
        if diff_list[idx] == 3:
            if in_ones_sequence == 'Yes':
                in_ones_sequence = 'No'
                if num_ones > 1:
                    ones_count_list.append(num_ones)

    return ones_count_list


def do_p2_better(values):
    diff_list = [ values[idx + 1] - values[idx] for idx in range(0, num_values - 1)]
    ones_list = ''.join([str(x) for x in diff_list]).split('3')
    create_consecutive_ones_map()
    result = 1
    for value in ones_list:
        if value == '':
            continue
        result *= ones_map[value.count('1')]

    print(f'Number of paths: {result}')


def do_p2(values):
    # P1 done better as part of setup for P2
    diff_list = [ values[idx + 1] - values[idx] for idx in range(0, num_values - 1)]
    print(f'diff of one: {diff_list.count(1)} diff of three: {diff_list.count(3)}')
    print(diff_list)
    ones_count_list = make_consecutive_ones_count_list(diff_list)
    print(f'Ones count list: {ones_count_list}')
    create_consecutive_ones_map()
    result = 1
    for value in ones_count_list:
        result *= ones_map[value]

    print(f'Number of paths: {result}')



def find_differences_of_one_and_three(values):
    diff_of_one = 0
    diff_of_three = 0
    for idx in range(0, len(values) - 1):
        diff = values[idx+1] - values[idx]
        if diff == 1:
            diff_of_one += 1
        elif diff == 3:
            diff_of_three += 1
    return diff_of_one, diff_of_three


def do_p1(values):
    diff_of_one, diff_of_three = find_differences_of_one_and_three(values)
    print(f'Processed {filename}')
    print(f'values: {values}')
    print(f'Found diff_of_one: {diff_of_one} and diff_of_three: {diff_of_three}. Product: {diff_of_one * diff_of_three}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-test1.txt', 'input-sample2.txt', 'input-d10.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            values = [ int(x) for x in f.read().split() ]
            values.sort()
            # Add wall outlet and built-in adapter to list
            values.insert(0, 0)
            values.append(values[-1] + 3)
            num_values = len(values)
            do_p1(values)
            do_p2(values)
            do_p2_better(values)

