with open('input_2.txt', 'r') as f:
    lines = f.readlines()

    x, y = 0, 0

    for i in lines:
        direction = i.split()[0]
        num_of_steps = int(i.split()[1])
        if direction == 'forward':
            x += num_of_steps
        elif direction == 'down':
            y += num_of_steps
        elif direction == 'up':
            y -= num_of_steps

    print(x*y)
