N = int(input())
nums = list(map(int,input().split()))

mx = 1
temp_mx = 1
#크거나같은경우
for i in range(1,len(nums)):
    if nums[i-1] >= nums[i]:
        temp_mx += 1
    else:
        if mx < temp_mx:
            mx = temp_mx
            temp_mx = 1
        else:
            temp_mx = 1
if mx < temp_mx:
    mx = temp_mx

temp_mx = 1
#작거나같은경우
for i in range(1,len(nums)):
    if nums[i-1] <= nums[i]:
        temp_mx += 1
    else:
        if mx < temp_mx:
            mx = temp_mx
            temp_mx = 1
        else:
            temp_mx = 1

if mx < temp_mx:
    mx = temp_mx

print(mx)