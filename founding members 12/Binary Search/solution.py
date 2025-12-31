def search(nums: List[int], target: int) -> int: 
    def binary(l, r): 
        mid = (l + r) // 2 
        if l > r: 
            return -1 
            
        if nums[mid] == target: 
            return mid 
        elif nums[mid] > target: 
            binary(l, mid) 
        else: 
            binary(mid, r) 
            
        return -1 
        
    return binary(0, len(nums))