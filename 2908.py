A, B = map(str, input().split())
li_A = list(A)
li_B = list(B)
li_A.reverse()
li_B.reverse()

R_A = "".join(li_A)
R_B = "".join(li_B)

if R_A > R_B:
    print(R_A)
else:
    print(R_B)