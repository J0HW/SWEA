for t in range(1,11):
    N = int(input())
    high = list(map(int,input().split()))
    sum=0
    for i in range(2, N-2):
        arr=[]
        for j in range(i-2,i+3):
            arr.append(high[j])
        if high[i] == max(arr):
            arr.remove(max(arr))
            sum += high[i]-max(arr)
    print(f'#{t} {sum}')