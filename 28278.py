N = int(input())

li = []
stack = []

for i in range(N):
    li.append(list(map(int, input().split())))


for i in li:
    if i[0] == 4 and len(stack) == 0:
        print(1)
    elif i[0] == 4 and len(stack) != 0:
        print(0)
    elif len(i) > 1:
        stack.append(i[1])
    elif i[0] == 3:
        print(len(stack))
    elif i[0] == 2 and len(stack) > 0:
        print(stack.pop())
    elif i[0] == 2 and len(stack) == 0:
        print(-1)
    elif i[0] == 5 and len(stack) > 0:
        print(stack[-1])
    elif i[0] == 5 and len(stack) == 0:
        print(-1)
        