T = int(input())

for tc in range(1,T+1):
    str1 = input()
    len_str = len(str1)
    result = "NO"

    if str1 == str1[::-1]:
        if str1[:len_str//2] == str1[:len_str//2][::-1]:
            if str1[(len_str+1)//2:] == str1[(len_str+1)//2:][::-1]:
                result = "YES"

    print(f"#{tc} {result}")