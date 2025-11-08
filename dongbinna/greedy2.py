s = input()
nums = [int(ch) for ch in s]
result=0

for num in nums:
    if(num < 2 or result < 2):
        result += num
    else:
        result *= num

print(result)