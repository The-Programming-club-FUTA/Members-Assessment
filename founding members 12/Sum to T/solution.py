def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        seen[num] = i + 1
        diff = target - num
        
        if diff in seen:
            return [num, diff]