with open('input_3.txt', 'r') as f:
    lines = f.readlines()

ox = lines.copy()
co2 = lines.copy()


def ox_finder(inp, i):
    a = sum([x[i].count('0') for x in inp])
    b = sum([x[i].count('1') for x in inp])
    new_lines = []
    if b >= a:
        for x in inp:
            if x[i] == '1':
                new_lines.append(x)
    else:
        for x in inp:
            if x[i] == '0':
                new_lines.append(x)
    if len(new_lines) == 1:
        print(new_lines)
    else:
        ox_finder(new_lines, i+1)


def co2_finder(inp, i):
    a = sum([x[i].count('0') for x in inp])
    b = sum([x[i].count('1') for x in inp])
    new_lines = []
    if b < a:
        for x in inp:
            if x[i] == '1':
                new_lines.append(x)
    else:
        for x in inp:
            if x[i] == '0':
                new_lines.append(x)
    check_lines = new_lines
    if len(check_lines) == 1:
        print(check_lines)
    else:
        co2_finder(new_lines, i+1)

o = ox_finder(ox, 0)
o_o = 1391
print(o)
c = co2_finder(co2, 0)
c_c = 2455
print(c)

print(o_o * c_c)
