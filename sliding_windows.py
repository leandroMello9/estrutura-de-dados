
def sliding_windows(nums, k):
    seen = {}
    for i in range(len(nums)):
        print(seen)
        if nums[i] in seen:
            if abs(i - seen[nums[i]] <= k):
                return True
        seen[nums[i]] = i
    return False

print(sliding_windows([1,2,3,1],2))