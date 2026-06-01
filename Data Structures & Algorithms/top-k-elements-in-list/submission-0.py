class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        items = list(freq.items())

        def count(x):
            return x[1]

        items.sort(key=count, reverse = True)

        result = []

        for i in range(k):
            result.append(items[i][0])

        return result

        