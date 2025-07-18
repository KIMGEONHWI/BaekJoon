import math

case = 1
while True:
    a, b, c = map(float, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(f"Triangle #{case}")
    if a == -1:
        if c <= b:
            print("Impossible.")
        else:
            print(f"a = {math.sqrt(c**2 - b**2):.3f}")
    elif b == -1:
        if c <= a:
            print("Impossible.")
        else:
            print(f"b = {math.sqrt(c**2 - a**2):.3f}")
    elif c == -1:
        print(f"c = {math.sqrt(a**2 + b**2):.3f}")
    else:
        print("Impossible.")
    print()
    case += 1
