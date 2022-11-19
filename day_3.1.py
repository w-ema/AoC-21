with open('input_3.txt', 'r') as f:
    lines = f.readlines()

gamma = []
epsilon = []

for i in range(len(lines[0]) - 1):
    x = []
    for j in range(len(lines) - 1):
        if lines[j][i] == '0' or lines[j][i] == '1':
            x.append(lines[j][i])
    if x.count('0') > x.count('1'):
        gamma.append('0')
        epsilon .append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
