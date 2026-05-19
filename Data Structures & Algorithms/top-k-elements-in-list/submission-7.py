class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most = {}
        #key is the number and value is the count of that number
        for num in nums:
            if num in most:
                most[num]+=1
            else:
                most[num] = 1
        top_n_values = heapq.nlargest(k, most.keys(), key=most.get)
        return top_n_values
        