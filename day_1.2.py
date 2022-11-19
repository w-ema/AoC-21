with open('input_1.txt', 'r') as f:
    lines = f.readlines()

numbers = [int(i) for i in lines]


def sum_of_three(i):
    return numbers[i] + numbers[i+1] + numbers[i+2]


def check(inp):
    ans = 0
    for j in range(1, len(inp)-2):
        if sum_of_three(j) > sum_of_three(j-1):
            ans += 1
    print(ans)


check(numbers)
