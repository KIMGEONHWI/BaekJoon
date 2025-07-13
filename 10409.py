n, T = map(int, input().split())
tasks = list(map(int, input().split()))

count = 0
total_time = 0

for task in tasks:
    if total_time + task > T:
        break
    total_time += task
    count += 1

print(count)