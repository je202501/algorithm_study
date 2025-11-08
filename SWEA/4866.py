T = int(input())

for tc in range(1,T+1):
    N = input()
    stack = []
    result = 1
    for i in N:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')' or i == '}':
            if len(stack) < 1:
                result = 0
                break
            top = stack.pop()
            if (i == ')' and top == '{') or (i == '}' and top == '('):
                result = 0
                break
    if len(stack) != 0:
        result = 0
    print(f"#{tc} {result}")