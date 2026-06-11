class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = {}

        for num in nums:
            dictt[num] = dictt.get(num , 0 ) + 1
        

        listt = sorted(dictt.items(), key=lambda x: x[1], reverse = True)

        return [item[0] for item in listt[:k]]
            