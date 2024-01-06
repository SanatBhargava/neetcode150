def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = dict()
        for elem in nums:
            if elem not in hashMap.keys():
                hashMap[elem] = 1
            
            else:
                return True
        else:
            return False
