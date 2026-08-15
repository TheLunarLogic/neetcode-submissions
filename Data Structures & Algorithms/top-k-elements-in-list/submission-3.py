import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for n in nums :
            mp[n] = 1 + mp.get(n , 0)
        
        pq = [] 

        for n in mp.keys():
            heapq.heappush(pq , (mp[n],n))
            if len(pq) > k :
                heapq.heappop(pq)
            
        res = [] 
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res
