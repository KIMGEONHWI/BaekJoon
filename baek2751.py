import sys
arr=[]
n=int(input())
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
def QuickSort(left, right, arr):
    if(left>=right):
         return
    i = left
    j= right
    pivot = arr[(left+right)//2]

    while(i<=j):
        while(arr[i] < pivot):
            i+=1
        
