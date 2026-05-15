N=int(input())
arr=[]
for i in range(1,N+1):
    arr.append(i)
arr=list(map(str, arr))
i=0
for _ in range(N):
    if '3' in arr[i] or '6' in arr[i] or '9' in arr[i]:
        count=0
        count += arr[i].count('3')
        count += arr[i].count('6')
        count += arr[i].count('9')
        arr[i] = '-'*count
    i+=1
print(*arr)
