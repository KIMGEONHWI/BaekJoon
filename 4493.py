def winner(p1, p2):

    if p1 == p2:
        return 0  
    if (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
        return 1  
    return 2 

t = int(input())
for _ in range(t):
    n = int(input())
    p1_score, p2_score = 0, 0
    for _ in range(n):
        a, b = input().split()
        res = winner(a, b)
        if res == 1:
            p1_score += 1
        elif res == 2:
            p2_score += 1
    if p1_score > p2_score:
        print("Player 1")
    elif p2_score > p1_score:
        print("Player 2")
    else:
        print("TIE")
