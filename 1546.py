N = int(input())

scores = list(map(int, input().split()))


Max_ = max(scores)

data = [ i/Max_*100 for i in scores ]

answer = sum(data) / N
print(answer)
