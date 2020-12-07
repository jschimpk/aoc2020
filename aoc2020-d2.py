def parse_policy(policy):
    first_half, char = policy.split()
    min = int(first_half.split('-')[0])
    max = int(first_half.split('-')[1])
    return min, max, char


def password_is_valid(line):
    policy, password = line.split(':')
    min, max, char = parse_policy(policy)
    num_char = password.count(char)
    if num_char >= min and num_char <= max:
        return True
    return False


def password_is_valid_p2(line):
    policy, password = line.split(':')
    password = password.strip().rstrip()
    pos1, pos2, char = parse_policy(policy)

    # Policy is 1-based, but python indices are 0-based. Adjust
    pos1 -= 1
    pos2 -= 1

    # Check if *exactly* one of the positions is the character
    matches = 0
    for pos in [pos1, pos2]:
        if password[pos] == char:
            matches += 1

    if matches == 1:
        return True
    return False




def number_of_valid_passwords(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    print(f'Read in file: {filename}  Number of lines: {len(lines)}')

    valid_passwords = 0
    for line in lines:
        if password_is_valid(line):
            valid_passwords += 1

    print(f'Number of valid passwords found for p1: {valid_passwords}')

    valid_passwords = 0
    for line in lines:
        if password_is_valid_p2(line):
            valid_passwords += 1

    print(f'Number of valid passwords found for p2: {valid_passwords}')


if __name__ == '__main__':
    filename = 'sample-input.txt'
    number_of_valid_passwords(filename)
    filename = 'input-d1p1.txt'
    number_of_valid_passwords(filename)