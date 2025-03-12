S = input()
result = []

for i in "abcdefghijklmnopqrstuvwxyz":
    if i in S:
        result.append(str(S.index(i)))
    else:
        result.append("-1")

print(" ".join(result))
