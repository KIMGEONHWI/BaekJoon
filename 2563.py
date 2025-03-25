n = int(input())
paper = [[0] * 100 for _ in range(100)]
area = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, min(x + 10, 100)):
        for j in range(y, min(y + 10, 100)):
            paper[i][j] = 1

for row in paper:
    area += row.count(1)

print(area)