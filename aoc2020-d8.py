def run_program(lines):
    acc = 0
    pc = 0
    pc_executed_list = []

    while pc not in pc_executed_list:
        instr = lines[pc]
        op, value = instr.split()
        pc_executed_list.append(pc)
        if op == 'nop':
            pc +=1
            continue
        if op == 'acc':
            acc += int(value)
            pc += 1
            continue
        if op == 'jmp':
            pc += int(value)
    print(f'Final acc: {acc}')


def run_program_p2(lines):
    acc = 0
    pc = 0
    pc_executed_list = []
    loc = len(lines)

    while pc not in pc_executed_list and pc < loc:
        instr = lines[pc]
        op, value = instr.split()
        pc_executed_list.append(pc)
        if op == 'nop':
            pc +=1
            continue
        if op == 'acc':
            acc += int(value)
            pc += 1
            continue
        if op == 'jmp':
            pc += int(value)

    if pc == loc:
        return (True, acc)
    else:
        return (False, 0)


def run_case(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    # P1
    run_program(lines)

    # P2
    for idx, instr in enumerate(lines):
        op, value = instr.split()
        test_prog = lines.copy()
        if op == 'nop':
            test_prog[idx] = test_prog[idx].replace('nop', 'jmp')
        elif op == 'jmp':
            test_prog[idx] = test_prog[idx].replace('jmp', 'nop')
        success, acc = run_program_p2(test_prog)
        if success:
            print(f'Success!  acc: {acc}.  Swapped istr: {instr} at idx: {idx}')
            break

if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-d8.txt']
    for filename in filenames:
        run_case(filename)