n = int(input())
for i in range(1, n + 1):
    sides = list(map(int, input().split()))
    sides.sort()
    print(f"Scenario #{i}:")
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print("yes")
    else:
        print("no")
    print()