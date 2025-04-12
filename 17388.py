S, K, H = map(int, input().split())

if S + K + H >= 100:
    print("OK")
else:
    min_participation = min(S, K, H)
    
    if min_participation == S:
        print("Soongsil")
    elif min_participation == K:
        print("Korea")
    else: 
        print("Hanyang")