with open('input_2.txt', 'r') as f:
    lines = f.readlines()

    x, y, aim = 0, 0, 0

    for i in lines:
        direction = i.split()[0]
        num_of_steps = int(i.split()[1])
        if direction == 'forward':
            x += num_of_steps
            y += aim * num_of_steps
        elif direction == 'down':
            aim += num_of_steps
        elif direction == 'up':
            aim -= num_of_steps

    print(x*y)