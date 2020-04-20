"""
    三数之和
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/3sum
"""


class Solution(object):

    def threeSum(self, nums):

        nums.sort()  # 排序
        n = len(nums)
        res, k = [], 0

        for k in range(n-2):
            if nums[k] > 0: break  # 例外情况
            if k > 0 and nums[k] == nums[k-1]: # 例外情况
                continue
            i, j = k + 1,len(nums) - 1  # 初始化i, j
            while i < j: # 双指针
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i< j and nums[i] == nums[i-1]: i += 1  # 如果又重复就跳过
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1  # 如果又重复就跳过
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i -1]: i += 1   # 如果又重复就跳过
                    while i < j and nums[j] == nums[j+ 1]: j -= 1   # 如果又重复就跳过
        return res


solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]

res = solution.threeSum(nums)
print(res)
