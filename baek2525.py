A, B = map(int, input().split())
#0 <= A <= 23
#0 <= B <= 59
C = int(input())
if B+C<60:
    print(A, B+C)
elif B+C>=60 and A+(B+C)//60 < 24:
    print(A+(B+C)//60, (B+C)%60)
elif B+C>=60 and A+(B+C)//60 >= 24:
    print((A+(B+C)//60)%24, (B+C)%60)