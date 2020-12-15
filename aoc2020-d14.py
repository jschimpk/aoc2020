# Shamelessly stolen from stack overflow
# https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
def replace_str_index(text,index=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])


def create_addr_list(addr, bitmask):
    for i, bit in enumerate(bitmask):
        if bit == 'X':
            # Create bitmask with 0 in place of X
            bitmask2 = replace_str_index(bitmask, i, '0')
            # Create two addr values
            addr1 = addr | (1 << (35 - i))
            addr2 = addr & ~(1 << (35 -i))
            #print(f'X found at i: {35-i}. addr: {addr}, bitmask: {bitmask}. addr1: {addr1}, addr2: {addr2}, bitmask2: {bitmask2}')
            return f'{create_addr_list(addr1, bitmask2)}\n{create_addr_list(addr2, bitmask2)}'

        if bit == '0':
            continue
        if bit == '1':
            addr |= (1 << (35 - i))
    #print(f'Returning {addr}')
    return f'{addr}\n'




def execute_instr_and_return_sum_p2(input):
    mem = {}
    instr_sets = input.split('mask = ')
    for instr_set in instr_sets:
        if instr_set == '':
            continue
        input = instr_set.split('\n')
        bitmask = input[0]
        instr = input[1:]
        print(f'Mask: {bitmask}, instr: {instr}')
        for op in instr:
            if op == '':
                continue
            print(f'op: {op}')
            addr = int(op.split(']')[0].split('[')[1])
            val = int(op.split('=')[1].strip())
            addr_list = create_addr_list(addr, bitmask).split()
            addr_list.sort()
            print(addr_list)
            for addr in addr_list:
                mem[addr] = val
    sum = 0
    for key, val in mem.items():
        sum += val
        #print(f'key: {key}, val: {val}, sum: {sum}')
    return sum


def apply_mask(bitmask, val):
    mask = 0x1
    for bit in reversed(bitmask):
        #print(f'Checking bit: {mask}. bitmask: {bit}, starting val: {val}')
        if bit == '0' and val & mask:
            #print(f'mask: {mask} bit is 0 and value is 1, do subtraction')
            val -= mask
        elif bit == '1' and val & mask == 0:
            #print(f'mask: {mask} bit is 1 and value is 0, do addition')
            val += mask
        #print(f'Ending val: {val}')
        mask = mask << 1
    return val


def execute_instr_and_return_sum(input):
    mem = {}
    instr_sets = input.split('mask = ')
    for instr_set in instr_sets:
        if instr_set == '':
            continue
        input = instr_set.split('\n')
        bitmask = input[0]
        instr = input[1:]
        #print(f'Mask: {bitmask}, instr: {instr}')
        for op in instr:
            if op == '':
                continue
            #print(f'op: {op}')
            addr = op.split(']')[0].split('[')[1]
            val = int(op.split('=')[1].strip())
            wr_val = apply_mask(bitmask, val)
            #print(f'op: {op}, addr: {addr}, val: {val} (0x{val:0x}), wr_val: {wr_val} (0x{wr_val:0x})')
            mem[addr] = wr_val

    sum = 0
    for key, val in mem.items():
        sum += val
        #print(f'key: {key}, val: {val}, sum: {sum}')
    return sum

if __name__ == '__main__':
    filenames = ['input-sample.txt', 'input-test.txt', 'input.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            input = f.read()
            sum = execute_instr_and_return_sum(input)
            #print(f'The sum of all memory after execution is: {sum}')

    # P2
    filenames = ['input-sample-p2.txt', 'input.txt']
    for filename in filenames:
        with open(filename, 'r') as f:
            input = f.read()
            sum = execute_instr_and_return_sum_p2(input)
            print(f'The sum of all memory after execution is: {sum}')