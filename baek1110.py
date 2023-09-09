int_num = int(input())
num=int_num
cnt=0
while True:
    sum_num=(num//10)+(num%10)
    new_num=((num%10)*10)+(sum_num%10)
    cnt+=1
    if new_num==int_num:
        break
    num=new_num # 헷갈리는 부분
print(cnt)