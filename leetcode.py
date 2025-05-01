def count_max_subarrays(nums, k):
    from collections import deque

    n = len(nums)
    count = 0
    maximum = max(nums)
    
    left = 0
    max_count = 0

    for right in range(n):
        if nums[right] == maximum:
            max_count += 1
        
        # Shrink window from the left if window size exceeds k
        while right - left + 1 > k:
            if nums[left] == maximum:
                max_count -= 1
            left += 1
        
        if right - left + 1 >= k and max_count >= k:
            count += 1

    return count



class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1

            while max_count >= k:
                # all subarrays from current `right` to end are valid
                count += len(nums) - right
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

        return count