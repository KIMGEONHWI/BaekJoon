import sys
cnt = int(sys.stdin.readline())

def recursion(s):
    global answer
    answer += 1
    if len(s) <= 1: return 1
    if s[0] != s[-1]: return 0
    return recursion(s[1:-1])

for _ in range(cnt):
    answer = 0
    s = sys.stdin.readline()[:-1]
    print(recursion(s), answer)