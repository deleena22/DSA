class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        seen = set()
        dups = set()

        for i in range (0, len(s) - 9):
            subst = s[i:i+10]
            if subst in seen:
                dups.add(subst)
            else:
                seen.add(subst)
        
        return list(dups)
