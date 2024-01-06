def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            if num not in counter.keys():
                counter[num] = 1
            else:
                counter[num]+= 1
        
        vals = sorted(counter.items(),key=lambda x: x[1],reverse=True)[:k]
        result = [x[0] for x in vals]
        return result
