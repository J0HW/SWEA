T=int(input())
for i in range(1, T+1):
    N=int(input())
    numbers = list(map(int, input().split()))
    sum=0
    max = numbers[-1]
    for j in range(len(numbers)-1,-1,-1):
        
        if max > numbers[j]:
            sum += max - numbers[j]
        elif max < numbers[j]:
            max = numbers[j]
    print(f'#{i} {sum}')