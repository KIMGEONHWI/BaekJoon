
V=int(input())
vote = list(str(input()))
voteA=0
voteB=0

for i in range (V):
    if vote[i] == 'A':
        voteA += 1
    else:
        voteB += 1

if voteA>voteB :
    print ("A")
elif voteA<voteB:
    print("B")
else:
    print("Tie")