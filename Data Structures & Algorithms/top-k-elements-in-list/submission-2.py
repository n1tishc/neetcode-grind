class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)
        # res = []

        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)
        
        # # print(freq)
        # heap = []
        # for num in freq.keys():
        #     heapq.heappush(heap, (freq[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # # print(heap)
        # for i in heap:
        #     res.append(i[1])
        # # print(res)
        # return res

        # Basic approach
        # First get a a frequency count of all the elemets 

        # res = []
        freq_dict = defaultdict(int)

        for num in nums:
            freq_dict[num] = 1 + freq_dict.get(num, 0)
        
        print(freq_dict)

        
        # Secondly, have a heap to keep track of "k" freq elemets
        # Default dict used by python is min heap
        # So its a guarantee that the pop will take out only the least
        # Frequent item, and heap will have the least elements 
        heap = []

        for num in freq_dict.keys():
            heapq.heappush(heap, (freq_dict[num], num))
            # print(heap)
            if len(heap) > k:
                heapq.heappop(heap)
            # print(heap)
        
        # step 3, finally just add or return elemets in heap

        return [x[1] for x in heap]