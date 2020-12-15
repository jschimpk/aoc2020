def find_2020th_number_spoken(starting_numbers):
    num_list = []
    starting_numbers = [ int(num) for num in starting_numbers.split(',') ]
    for i in range(0, 2020):
        #print(f'i:{i}, num_list: {num_list}')
        if i < len(starting_numbers):
            #print(f'Still in starting numbers')
            num_list.append(starting_numbers[i])
        else:
            last_num = num_list[i-1]
            found_num = False
            for j, num in enumerate(reversed(num_list[0:-1])):
                if num == last_num:
                    #print(f'Found {last_num} at {j+1} numbers back')
                    num_list.append(j+1)
                    found_num = True
                    break
            if found_num == False:
                #print(f'Didn\'t find {last_num}, add 0 to list')
                num_list.append(0)
    return num_list[-1]


def find_nth_number_spoken(n, starting_numbers):
    num_list = []
    starting_numbers = [ int(num) for num in starting_numbers.split(',') ]
    for i in range(0, n):
        #if i % 10000 == 0:
        #print(f'i:{i}, num_list: {num_list}')
        if i < len(starting_numbers):
            #print(f'Still in starting numbers')
            num_list.append(starting_numbers[i])
        else:
            last_num = num_list[i-1]
            found_num = False
            for j, num in enumerate(reversed(num_list[0:-1])):
                if num == last_num:
                    #print(f'Found {last_num} at {j+1} numbers back')
                    num_list.append(j+1)
                    found_num = True
                    break
            if found_num == False:
                #print(f'Didn\'t find {last_num}, add 0 to list')
                num_list.append(0)
    return num_list[-1]


def find_nth_number_spoken_dict(n, starting_numbers):
    num_list = []
    num_dict = {}
    old_dict = {}
    starting_numbers = [ int(num) for num in starting_numbers.split(',') ]
    for i in range(0, n):
        #if i % 10000 == 0:
        #    print(f'i:{i}')
        #print(f'i:{i}, num_list: {num_list}, num_dict: {num_dict}, old_dict: {old_dict}')

        if i < len(starting_numbers):
            #print(f'Still in starting numbers')
            num = starting_numbers[i]
            num_list.append(num)
            if num in num_dict:
                old_dict[num] = num_dict[num]
            num_dict[num] = i
        else:
            last_num = num_list[i-1]
            if last_num in old_dict:
                new_num = i - 1 - old_dict[last_num]
                #print(f'Found last_num: {last_num} at index: {old_dict[last_num]}. new_num: {new_num}')
                num_list.append(new_num)
                old_dict[last_num] = num_dict[last_num]
                if new_num in num_dict:
                    old_dict[new_num] = num_dict[new_num]
                num_dict[new_num] = i
            else:
                #print(f'Did not find last_num: {last_num} in old_dict')
                if last_num in num_dict:
                    #print(f'Found last_num: {last_num} in new_dict with value: {num_dict[last_num]}')
                    if num_dict[last_num] == i - 1:
                        pass
                        #print(f'Found it at previous index. Ignore')
                    else:
                        #print(f'Found it at other index. Add old_dict entry')
                        old_dict[num] = num_dict[num]
                    num_list.append(0)
                    if 0 in num_dict:
                        old_dict[0] = num_dict[0]
                    num_dict[0] = i
                else:
                    print(f'How did this happen?')

    return num_list[-1]


if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            starting_numbers_list = f.read().splitlines()
            for starting_numbers in starting_numbers_list:
                #num = find_2020th_number_spoken(starting_numbers)
                #print(f'2020th number: {num}')
                num = find_nth_number_spoken(2020, starting_numbers)
                print(f'2020th number: {num}')
                num = find_nth_number_spoken_dict(2020, starting_numbers)
                print(f'2020th number: {num}')
            for starting_numbers in starting_numbers_list:
                num = find_nth_number_spoken_dict(30000000, starting_numbers)
                print(f'30000000th number: {num}')
