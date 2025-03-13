dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

word = list(input())
result = 0

for i in word:
    for j in dial:
        if i in j:
            num = dial.index(j) + 3
            result += num
print(result)
