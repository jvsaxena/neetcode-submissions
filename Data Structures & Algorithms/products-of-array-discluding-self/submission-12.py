class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running = []
        # If there are 2 or more zeros, every single product will be 0
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        
        
        run = 1
        for num in nums:
            if num != 0:
                run*=num
        
        for num in nums:
            if zero_count == 1:
                # If there's one zero, only the zero's index gets the product
                running.append(run if num == 0 else 0)
            else:
                # No zeros at all, logic works perfectly
                running.append(run // num)
        return running

            
            