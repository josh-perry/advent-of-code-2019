def get_opcode(intcode, position):
    return intcode[position:position+4]


def execute_intcode(intcode):
    position = 0

    while True:
        # Fetch
        op = get_opcode(intcode, position)

        # Execute
        if op[0] == 1:
            intcode[op[3]] = intcode[op[1]] + intcode[op[2]]
        elif op[0] == 2:
            intcode[op[3]] = intcode[op[1]] * intcode[op[2]]
        elif op[0] == 99:
            print("halt!")
            break
        else:
            raise Exception("Unknown opcode!")
        
        # Increment
        position += 4

if __name__ == '__main__':
    opcode = []

    with open("day2/input") as f:
        opcode = [int(i) for i in f.read().split(",")]

    # Restore previous state:
    opcode[1] = 12
    opcode[2] = 2

    execute_intcode(opcode)

    print(opcode[0])
