def run_case(filename):
    with open(filename, 'r') as f:
        groups = f.read().split('\n\n')

    # P1
    group_sum = sum([len(set(group.replace('\n', ''))) for group in groups])
    print(f'Sum of group responses: {group_sum}')

    # P2
    num_yes_list = []
    for group in groups:
        all_yes = 0
        num_people = group.count('\n') + 1
        responses = group.replace('\n', '')
        resp_set = set(responses)
        for resp in resp_set:
            if responses.count(resp) == num_people:
                all_yes += 1
        num_yes_list.append(all_yes)

    print(f'Found sum: {sum(num_yes_list)} for num_yes_list: {num_yes_list}')


if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-d6p1.txt']
    for filename in filenames:
        run_case(filename)
