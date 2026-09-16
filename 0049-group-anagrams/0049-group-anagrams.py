class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs)
        if n == 1:
            return [strs] 
        word_dict = {}
        ans_list = []
        for word in strs: 
            sorted_word = "".join(sorted(word))
            if sorted_word not in word_dict:
                word_dict[sorted_word] = [word]
            else: 
                word_dict[sorted_word].append(word)
        for value in word_dict.values():
            ans_list.append(value)
        return ans_list