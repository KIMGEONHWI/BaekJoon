A = list(map(str,input().split())) 
B = list(map(str,input().split()))
C = list(map(str,input().split()))

LIST = []
LIST = [A] + [B] + [C]

x = []
y = []

for i in LIST:
    if i[0] not in x:
        x.append(i[0])
    else:
        x.remove(i[0])
    if i[1] not in y:
        y.append(i[1])
    else:
        y.remove(i[1])
answer = x + y
print(int(answer[0]), int(answer[1]))
