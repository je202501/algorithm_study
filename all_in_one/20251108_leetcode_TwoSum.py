#https://leetcode.com/problems/two-sum/description/

def TwoSum(nums,target):
    nums.sort()
    l = 0
    r = len(nums)-1
    while l<r:
        num = nums[l]+nums[r]
        if num < target:
            l += 1
        elif num > target:
            r -= 1
        elif num == target:
            return True
    return False

print(TwoSum([1,2,6,3,4],4))
