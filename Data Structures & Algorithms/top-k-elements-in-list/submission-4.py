class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for n in nums :
            mp[n] = 1 + mp.get( n , 0)

        heap = []
        for key in mp.keys():
            heapq.heappush(heap , (mp[key] , key))
            if len(heap) > k :
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        