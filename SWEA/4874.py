T = int(input())

for tc in range(1,T+1):
    forth = list(map(str,input().split()))
    stack = []
    result = 0
    for i in forth:
        if i not in '+-*/.':
            stack.append(int(i))
        elif i == '.':
            if len(stack) != 1:
                result = 'error'
                break
            result = stack.pop()
            break
        else:
            if len(stack) < 2:
                result = 'error'
                break
            num2 = stack.pop()
            num1 = stack.pop()
            if i == '+':
                stack.append(num1 + num2)
            elif i == '-':
                stack.append(num1 - num2)
            elif i == '*':
                stack.append(num1 * num2)
            elif i == '/':
                stack.append(num1 // num2)
    print(f"#{tc} {result}")