
class Solution(object):

    def twoSum2(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]

    # 一个循环搞定，每次在已经保存的字典中进行查找
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


solution = Solution()
nums = [3, 3]
target = 6

indexs = solution.twoSum(nums, target)
print(indexs)