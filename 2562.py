answer = []

for i in range(1, 10):
    answer.append(int(input()))

print(max(answer))
print(answer.index(max(answer))+1)
