N = int(input())

list = []

for _ in range(N):
    data = input()
    if 6 <= len(data) and len(data) <= 9:
        print("yes")
    else:
        print("no")
