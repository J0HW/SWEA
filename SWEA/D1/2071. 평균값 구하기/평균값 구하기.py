T=int(input())
for i in range(1,T+1):
    number = list(map(int, input().split()))
    a=sum(number)/10
    print(f"#{i} {a:.0f}")