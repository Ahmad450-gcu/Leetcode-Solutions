class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        sort_nums = []
        for i in range(0, n):
            sort_nums.append((nums[i], i))
        sort_nums.sort()
        answer = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sort_nums[j][0] - sort_nums[j-1][0] <= limit:
                j += 1
            sort_index = [] 
            for k in range(i, j):
                sort_index.append(sort_nums[k][1])
            sort_index.sort()
            m = len(sort_index)
            for k in range(0, m):
                answer[sort_index[k]] = sort_nums[i + k][0]
            i = j
        return answer