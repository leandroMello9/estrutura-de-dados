class Solution(object):
    def twoSum(self, nums, target):
        numeros = {}
        for i, num in enumerate(nums):
            print(f"Target => {target} and nums {num}")
            if target - num in numeros:
                print(f"Target => {target} and nums {num}")
                return [i, numeros[target - num]]
            numeros[num] = i
            print(f"Numeros directonary -> {numeros}")



s = Solution()
print(s.twoSum([1,2,3,4,5], 5))