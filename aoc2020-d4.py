def number_is_in_range(num, min, max):
    if num < min or num > max:
        print(f'Num: {num} out of range: {min}-{max}!')
        return False
    return True


def is_decimal(char):
    if number_is_in_range(ord(char), ord('0'), ord('9')):
        return True
    return False


def is_hexidecimal(char):
    if number_is_in_range(ord(char), ord('a'), ord('f')) or is_decimal(char):
        return True
    else:
        return False


def item_is_valid(field, value):
    if field == 'byr':
        return number_is_in_range(int(value), 1920, 2002)
    if field == 'iyr':
        return number_is_in_range(int(value), 2010, 2020)
    if field == 'eyr':
        return number_is_in_range(int(value), 2020, 2030)
    if field == 'hgt':
        if len(value) < 4:
            print(f'Did not find units: Length too small')
            return False
        units = value[-2:]
        num = int(value[:-2])
        if units == 'cm':
            return number_is_in_range(num, 150, 193)
        if units == 'in':
            return number_is_in_range(num, 59, 76)
        print(f'Did not find valid units: {units}')
        return False
    if field == 'hcl':
        if value[0] != '#':
            print(f'hcl didn\'t start with #: {value}')
            return False
        if len(value) != 7:
            print(f'hcl not long enough: {value}')
            return False
        for char in value[1:]:
            if not is_hexidecimal(char):
                print(f'hcl: found non-hexidecimal value: {char}')
                return False
        return True
    if field == 'ecl':
        valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value not in valid_ecl:
            print(f'ecl: {value} not valid!')
            return False
        return True
    if field == 'pid':
        if len(value) != 9:
            print(f'pid: {value} length ({len(value)} is not 9!')
            return False
        for char in value[1:]:
            if not is_decimal(char):
                print(f'pid: found non-decimal value: {char}!')
                return False
        return True
    if field == 'cid':
        return True
    print(f'Unknown field: {field}')
    return False


def passport_is_valid(lines, validate_fields='no'):
    required_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    joined_lines = ' '.join(lines)
    data = joined_lines.split(' ')
    print(f'Processing passport data (len: {len(data)}): {data}')
    data_dict = {}
    for item in data:
        field, value = item.split(':')
        data_dict[field] = value

    for item in required_list:
        if item not in data_dict:
            print(f'Did not find {item} in passport data.')
            return False
        if validate_fields and not item_is_valid(item, data_dict[item]):
            print(f'Found invalid value! field: {item}, value: {data_dict[item]}')
            return False
    print(f'Found all required items in passport data.')
    return True

def num_valid_passports(lines, validate_fields='no'):
    num_valid = 0
    num_entries = 0
    first_idx = 0
    for idx, line in enumerate(lines):
        if line == '' or idx == len(lines) - 1:
            num_entries += 1
            # Found passport. Validate it
            passport_lines = lines[first_idx:idx]
            if passport_is_valid(passport_lines, validate_fields):
                num_valid += 1
            first_idx = idx + 1

    return num_valid, num_entries


def run_case(filename, validate_fields='no'):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    num_valid, num_entries = num_valid_passports(lines, validate_fields)
    print(f'Parsed {num_entries} passports and found {num_valid} are valid!')

if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-d4p1.txt']
    for filename in filenames:
        run_case(filename)

    for filename in filenames:
        run_case(filename, validate_fields='yes')