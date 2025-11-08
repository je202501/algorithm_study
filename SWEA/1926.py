T = int(input())

result = []

for test_case in range(1,T+1):
    clap = ''
    for i in str(test_case):
        if i == '3' or i == '6' or i == '9':
            clap += '-'

    if clap == '':
        result.append(test_case)
    else:
        result.append(clap)

for i in result:
    print(f'{i}',end=' ')
