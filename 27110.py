N = int(input())

data = list(map(int, input().split()))

List = []

for i in data:
    if i < N:
        List.append(i)
    else:
        List.append(N)

print(sum(List))