def find_three_values_that_sum(lines, sum=2020):
    for idx1, line1 in enumerate(lines):
        for idx2, line2 in enumerate(lines[idx1:]):
            for idx3, line3 in enumerate(lines[idx1+idx2:]):
                num1 = int(line1)
                num2 = int(line2)
                num3 = int(line3)
                if (num1 + num2 + num3 == sum):
                    print(f'Found the matching values (idx):value: ({idx1}): {num1}, ({idx2}): {num2}, ({idx3}): {num3}')
                    return num1, num2, num3


def find_two_values_that_sum(lines, sum=2020):
    for idx1, line1 in enumerate(lines):
        for idx2, line2 in enumerate(lines[idx1:]):
            num1 = int(line1)
            num2 = int(line2)
            if (num1 + num2 == sum):
                print(f'Found the matching values (idx):value: ({idx1}): {num1}, ({idx2}): {num2}')
                return num1, num2


def main():
    filename = 'input-p1.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()

    print(f'Read in file: {filename}  Number of lines: {len(lines)}')

    num1, num2 = find_two_values_that_sum(lines, sum=2020)
    print(f'Multiply two values together: {num1 * num2}')

    num1, num2, num3 = find_three_values_that_sum(lines, sum=2020)
    print(f'Multiply three values together: {num1 * num2 * num3}')


if __name__ == '__main__':
    main()
