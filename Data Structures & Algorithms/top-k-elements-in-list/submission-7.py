class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Count frequency of each number
        count = Counter(nums)

        # Example:
        # {1:3, 2:2, 3:1}

        top_k_pairs = count.most_common(k)

        # Example:
        # [(1,3), (2,2)]

        result = []

        for pair in top_k_pairs:

            num = pair[0]
            freq = pair[1]

            result.append(num)

        return result