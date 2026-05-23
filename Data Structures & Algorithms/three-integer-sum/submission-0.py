class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        # Iterate through each number
        for i, a in enumerate(nums):

            # Skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            # Optimization
            if a > 0:
                break

            # Two pointers
            l, r = i + 1, len(nums) - 1

            while l < r:

                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1

                elif three_sum < 0:
                    l += 1

                else:
                    res.append([a, nums[l], nums[r]])

                    l += 1

                    # Skip duplicate second elements
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res