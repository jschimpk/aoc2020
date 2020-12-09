def can_hold_special(bag_name, special_bag):
    rules = bag_dict[bag_name]
    if rules == 'None':
        return False
    if special_bag in rules:
        return True
    for rule in rules:
        if can_hold_special(rule, special_bag):
            return True
    return False


def how_many_bags_can_hold_me(special_bag):
    num_bags = 0
    for bag_name in bag_dict:
        if can_hold_special(bag_name, special_bag):
            num_bags += 1

    return num_bags


def how_many_bags_inside(bag_name):
    num_bags = 0
    rules = bag_dict[bag_name]
    if rules == 'None':
        return 0
    for rule_name, number in rules.items():
        num_bags += number + number * how_many_bags_inside(rule_name)
    return num_bags


def create_rules_dict(rules):
    if len(rules) == 1:
        if rules[0].split()[0] == 'no':
            return 'None'
    # There is at least one other bag that can go inside
    rules_dict = {}
    for rule in rules:
        rules_split = rule.split()
        number = rules_split[0]
        name = ' '.join(rules_split[1:-1])
        rules_dict[name] = int(number)
    return rules_dict


def create_bag_dict(lines):
    for line in lines:
        bag = line.split('bags')[0].rstrip()
        rules = line.split('contain')[1].strip().rstrip('.').split(',')
        bag_dict[bag] = create_rules_dict(rules)
    #for bag_name, rules in bag_dict.items():
        #print(f'bag: {bag_name}, rules: {rules}')


def run_case(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    print(f'Run case for {filename}.')
    special_bag = 'shiny gold'
    create_bag_dict(lines)

    # P1
    count = how_many_bags_can_hold_me(special_bag)
    print(f'Found {count} bags that can hold {special_bag}')

    # P2
    count = how_many_bags_inside(special_bag)
    print(f'Found {count} bags inside of {special_bag}')


if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-sample-p2.txt', 'input-d7p1.txt']
    for filename in filenames:
        bag_dict = {}
        run_case(filename)

