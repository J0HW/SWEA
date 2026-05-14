T=int(input())
for i in range(1, T+1):
    N=int(input())
    score = [0]*101
    numbers = list(map(int, input().split()))
    for num in numbers:
        score[num] += 1

    max_score = max(score)
    result=[]
    for j in range(len(score)):
        if score[j] == max_score:
            result.append(j)
    
    print(f'#{i} {max(result)}')
