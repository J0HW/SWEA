T=int(input())
for i in range(1,T+1):
    grid=[list(map(int, input().split())) for _ in range(9)]
    result=[]
    for r in range(0,9):
        arr = [0]*9
        for c in range(0,9):
            arr[grid[r][c]-1]+=1
        if any(x > 1 for x in arr) or 0 in arr:
            result.append(0)
        else:
            result.append(1)

    for c in range(0,9):
        arr=[0]*9
        for r in range(0,9):
            arr[grid[r][c]-1]+=1
        if any(x > 1 for x in arr) or 0 in arr:
            result.append(0)
        else:
            result.append(1)
    
    for _ in range(9):
        a=[]
        for q in range(0,9,3):
            for w in range(0,9,3):
                r=q
                c=w
                for g in range(0,3):
                    for h in range(0,3):
                        a.append(grid[r+g][c+h])

        arr=[0]*9
        for j in range(0,9):
            arr[a[j]-1]+=1
        if any(x > 1 for x in arr) or 0 in arr:
            result.append(0)
        else:
            result.append(1)


    if 0 in result:
        answer=0
    else:
        answer=1
    
    print(f'#{i} {answer}')
