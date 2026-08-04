class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Buckets: index = frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Place numbers into buckets
        for num, c in count.items():
            freq[c].append(num)

        # Collect from highest frequency down
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res