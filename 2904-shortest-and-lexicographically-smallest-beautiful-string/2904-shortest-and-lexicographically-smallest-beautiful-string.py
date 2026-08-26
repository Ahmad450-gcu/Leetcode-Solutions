class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count("1") < k:
            return ""
        exact = k * '1'
        if exact in s:
            return exact
        smallest = ''
        count_1 = 0
        start = 0
        n = len(s)
        for end in range(0, n):
            if s[end] == '1':
                count_1 += 1
            while (count_1 == k):
                current_ans = s[start:end+1]
                if not smallest or len(current_ans) < len(smallest):
                    smallest = current_ans
                elif len(current_ans) == len(smallest):
                    smallest = min(current_ans, smallest)
                
                if s[start] == '1':
                    count_1 -= 1
                start += 1 
        return smallest
        
            