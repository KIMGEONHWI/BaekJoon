n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data_x = [i[0] for i in data]
data_y = [j[1] for j in data]

answer = (max(data_x) - min(data_x)) * (max(data_y) - min(data_y))

print(answer)