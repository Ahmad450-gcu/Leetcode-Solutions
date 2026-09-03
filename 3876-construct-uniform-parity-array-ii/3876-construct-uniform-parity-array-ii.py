class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        n = len(nums1)
        minimum = min(nums1)
        if minimum % 2 == 0:
            for i in range(0, n):
                if nums1[i] % 2 != 0:
                    return False
        return True
        