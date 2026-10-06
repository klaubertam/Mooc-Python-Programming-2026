def run(program):
    locations = {}
    for i, line in enumerate(program):
        if line.endswith(':'):
            locations[line[:-1]] = i
    
    variables = {chr(ord('A') + i): 0 for i in range(26)}
    output = []
    pc = 0
    
    def get_value(token):
        if token in variables:
            return variables[token]
        return int(token)
    
    while pc < len(program):
        line = program[pc]
        parts = line.split()
        cmd = parts[0]
        
        if cmd == 'END':
            break
        elif cmd == 'PRINT':
            output.append(get_value(parts[1]))
        elif cmd == 'MOV':
            variables[parts[1]] = get_value(parts[2])
        elif cmd == 'ADD':
            variables[parts[1]] += get_value(parts[2])
        elif cmd == 'SUB':
            variables[parts[1]] -= get_value(parts[2])
        elif cmd == 'MUL':
            variables[parts[1]] *= get_value(parts[2])
        elif cmd == 'JUMP':
            pc = locations[parts[1]]
            continue
        elif cmd == 'IF':
            a, op, b, _, loc = parts[1], parts[2], parts[3], parts[4], parts[5]
            av, bv = get_value(a), get_value(b)
            cond = (op == '==' and av == bv) or (op == '!=' and av != bv) or \
                   (op == '<' and av < bv) or (op == '<=' and av <= bv) or \
                   (op == '>' and av > bv) or (op == '>=' and av >= bv)
            if cond:
                pc = locations[loc]
                continue
        
        pc += 1
    
    return output