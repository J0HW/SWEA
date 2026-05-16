T = int(input())
for t in range(1,T+1):
    N = int(input())
    if N < 3:
        print(f'#{t} 0')
    else:
        print(f'#{t} {N // 3}')