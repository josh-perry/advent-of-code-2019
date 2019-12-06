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
            break
        else:
            break
        
        # Increment
        position += 4


def load_from_file(filename):
    with open(filename) as f:
        return [int(i) for i in f.read().split(",")]


def set_noun_verb(intcode, n, v):
    intcode[1] = n
    intcode[2] = v


if __name__ == '__main__':
    result = None

    noun = None
    verb = None
    answer_found = False

    for noun in range(0, 99+1):
        for verb in range(0, 99+1):
            opcode = load_from_file("day2/input")
            position = 0

            set_noun_verb(opcode, noun, verb)
            execute_intcode(opcode)

            result = opcode[0]
            
            if result == 19690720:
                answer_found = True
                break

        if answer_found:
            break

    if answer_found:
        print("{}\t{}\t{}".format(noun, verb, 100*noun+verb))
        print(opcode[0])
    else:
        print("No answer found!")