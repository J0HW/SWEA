T=int(input())
for i in range(1, T+1):
    N=int(input())
    grid=[[0]*N for _ in range(N)]

    r,c,dist=0,0,0
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]

    num=1
    for _ in range(N*N):
        grid[r][c]=num

        if num == N*N:
            break

        nr=r+dr[dist]
        nc=c+dc[dist]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] != 0:
            dist = (dist + 1) % 4
            nr = r + dr[dist]
            nc = c + dc[dist]

        r,c=nr,nc
        num+=1
    print(f'#{i}')
    for row in grid:
        print(*row)