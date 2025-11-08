T=int(input())

result=[]
for test_case in range(1, T + 1):
    a = input()
    year = a[0]+a[1]+a[2]+a[3]
    month_str=a[4]+a[5]
    day_str=a[6]+a[7]
    month = int(a[4]+a[5])
    day = int(a[6]+a[7])
    if month>12 or month<1:
        result.append(-1)
        continue
    if day<1 :
        result.append(-1)
        continue
    elif (month == 1 or month == 3 or month == 5 or month ==7 or month == 8 or month ==10 or month == 12) and day>31:
        result.append(-1)
        continue
    elif (month == 4 or month == 6 or month ==9 or month == 11) and day>30:
        result.append(-1)
        continue
    elif month == 2 and day>28:
        result.append(-1)
        continue
    else:
        result.append('{}/{}/{}'.format(year,month_str,day_str))

for i in range(len(result)):
    print('#{} {}'.format(i+1,result[i]))