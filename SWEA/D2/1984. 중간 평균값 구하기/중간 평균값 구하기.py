T=int(input())
for i in range(1,T+1):
    arr=list(map(int, input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))
    std=sum(arr)/8
    print(f'#{i} {std:.0f}')