T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result=0
    for r in range(0,N):
        count=0
        for c in range(0, N):
            count+=grid[r][c]
            if grid[r][c]==0:
                if count == K:
                    result+=1
                count=0
        if count == K:
            result+=1

    for c in range(0,N):
        count=0
        for r in range(0, N):
            count+=grid[r][c]
            if grid[r][c]==0:
                if count == K:
                    result+=1
                count=0
        if count == K:
            result+=1

    
    print(f'#{t} {result}')