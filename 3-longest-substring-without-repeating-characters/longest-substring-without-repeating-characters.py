class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return len(s)
        if s.isspace():
            return 1
        substring_lens = []
        seen = set()

        p1 = 0
        p2 = 0
        count = 0

        while p2 < len(s):
            if s[p2] not in seen:
                seen.add(s[p2])
                count = p2 - p1 + 1
                substring_lens.append(count)
                p2 += 1
            else:
                seen.remove(s[p1])
                p1 += 1
        return max(substring_lens)
        # seen = p w

