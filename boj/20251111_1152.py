str1 = input()
count = 0

for i in range(len(str1)-1):
    if count == 0 and str1[i] != ' ':
        count += 1
    elif str1[i] == ' ' and str1[i+1] != ' ':
        count += 1


print(count)
