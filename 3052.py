data = []
for _ in range(10):
    num = int(input())
    data.append(num)


remainders = {i % 42 for i in data}

print(len(remainders))
