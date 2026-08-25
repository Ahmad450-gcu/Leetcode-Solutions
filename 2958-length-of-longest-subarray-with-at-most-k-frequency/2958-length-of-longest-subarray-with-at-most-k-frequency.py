class Solution(object):
    def maxSubarrayLength(self, nums, k):
        n = len(nums)
        subLen = []
        freq = {}
        start = 0
        for i in range(0, n):
            if nums[i] in freq and ((freq[nums[i]] + 1) > k):
                subLen.append(sum(freq.values()))
                j = start
                while nums[j] != nums[i]:
                    freq[nums[j]] -= 1
                    if freq[nums[j]] == 0:
                        del freq[nums[j]]
                    j += 1
                start = j + 1
                freq[nums[i]] = k
            else:
                if nums[i] in freq:
                    freq[nums[i]] += 1
                else:
                    freq[nums[i]] = 1
        subLen.append(sum(freq.values()))
        return max(subLen)
