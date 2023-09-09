n = int(input())
m = list(map(int,input().split()))
m_max=max(m)

new_list=[]
for i in range(n):
    m[i]=m[i]/m_max*100
    new_list.append(m[i])
avg=sum(new_list)/n
print(avg)
