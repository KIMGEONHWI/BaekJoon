X = int(input())
for i in range(X):
    ox_list=list(input())
    score=0
    sum_score=0
    for ox in ox_list:
        if ox=='0':
            score+=1
            sum_score+=score
        else:
            score=0
    print(sum_score)