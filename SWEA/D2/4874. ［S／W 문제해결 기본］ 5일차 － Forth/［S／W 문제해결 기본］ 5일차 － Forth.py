T = int(input())
for i in range(1,T+1):
    arr = input().split()
    for j in range(0,len(arr)):
        if arr[j] != '+' and arr[j] != '-' and arr[j] != '*' and arr[j] != '/' and arr[j] != '.':
            arr[j] = int(arr[j])
    stack=[]
    for x in arr:
        if x=='.':
            break

        if x not in ['+','-','*','/','.']:
            stack.append(x)
        
        elif x == '+':
            if len(stack) < 2:
                stack.clear()
                break
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        elif x == '-':
            if len(stack) < 2:
                stack.clear()
                break
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        elif x == '*':
            if len(stack) < 2:
                stack.clear()
                break
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)
        elif x == '/':
            if len(stack) < 2:
                stack.clear()
                break
            b = stack.pop()
            a = stack.pop()
            stack.append(a//b)
        
    if len(stack) != 1:
        print(f'#{i} error')
    else:
        print(f'#{i} {stack[0]}')