T = int(input())

for tc in range(1,T+1):
    word = input()
    stack = []
    half = len(word)//2
    result = 1

    for i in range(half):
        stack.append(word[i])

    if len(word)%2 == 1:
        for i in range(half):
            temp = stack.pop()

            if temp != word[half+i+1]:
                result = 0
                break
    else:
        for i in range(half):
            temp = stack.pop()
            if temp != word[half+i]:
                result = 0
                break

    print(f"#{tc} {result}")