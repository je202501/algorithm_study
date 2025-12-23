N = int(input())
result = []

for num2 in range(1,N+1):
    num1 = N
    temp_lst = [num1,num2]
    temp = N
    while True:
        temp = num1 - num2
        num1 = num2
        num2 = temp
        if temp<0:
            break
        temp_lst.append(temp)
    if len(result) < len(temp_lst):
        result = temp_lst

print(len(result))
for i in result:
    print(i,end=' ')