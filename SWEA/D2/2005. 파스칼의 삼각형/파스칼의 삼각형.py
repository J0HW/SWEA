T = int(input())
for t in range(1,T+1):
    N=int(input())
    grid = [[0]*N for _ in range(N)]
    if N==1:
        grid[0][0]=1
        break
    elif N==2:
        grid[0][0]=1
        grid[1][0]=1
        grid[1][1]=1
        break
    
    elif N > 2:
        grid[0][0]=1
        grid[1][0]=1
        grid[1][1]=1
        for r in range(2,N):
            for c in range(0, r+1):
                if c == 0:
                    grid[r][c] = 1
                elif c == r:
                    grid[r][c] = 1
                else:
                    grid[r][c]=grid[r-1][c-1]+grid[r-1][c]
    print(f'#{t}')
    for row in grid:
        print(*[x for x in row if x != 0])