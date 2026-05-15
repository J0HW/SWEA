T=int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pari_count=[]
    for a in range(0,N-M+1):
        for b in range(0,N-M+1):
            r=a
            c=b
            pari=0
            for j in range(0,M):
                for k in range(0,M):
                    pari+= arr[r+j][c+k]
            pari_count.append(pari)

    print(f'#{i} {max(pari_count)}')