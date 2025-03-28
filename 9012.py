import sys

N = int(sys.stdin.readline())


for _ in range(N):
    stack = []
    data = sys.stdin.readline().strip()

    for j in data:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) == 0:
                stack.append(j)
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print("NO")
    else:
        print("YES")
