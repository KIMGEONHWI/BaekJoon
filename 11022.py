T = int(input())
for i in range(1,T+1):
     A,B = map(int, input().split())
     ans=A+B
     print("Case #%s: %s + %s = %s"%(i,A,B,ans))