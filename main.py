# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(len(nums) - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False
#

def containsDuplicate(nums) -> bool:
    seen = {}
    for i, n in enumerate(nums):
        if n in seen:
            return True
        else:
            seen[n] = i

    return False


if __name__ == '__main__':
    print(containsDuplicate([3,1]))
    print(containsDuplicate([3,1,3,2,6]))

