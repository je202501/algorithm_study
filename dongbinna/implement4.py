S = input()

num=0
result=[]
for ch in S:
    if ch.isalpha():
        result += ch
    else:
        num += int(ch)

result.sort()
if num != 0:
    result += str(num)
result = ''.join(result)

print(result)