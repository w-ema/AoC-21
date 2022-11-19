with open('input_1.txt', 'r') as f:
    lines = f.readlines()

def check(inp):
    ans = 0
    for j in range(1,len(inp)):
        if int(inp[j]) > int(inp[j-1]):
            ans += 1
    print(ans)

check(lines)