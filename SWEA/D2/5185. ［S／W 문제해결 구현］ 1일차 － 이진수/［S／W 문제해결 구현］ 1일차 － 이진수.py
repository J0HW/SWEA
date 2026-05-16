T = int(input())
for t in range(1,T+1):
    N, number=input().split()
    N=int(N)
    number = int(number,16)
    print(f'#{t} {bin(number)[2:].zfill(N*4)}')