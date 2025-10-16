class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        #counts for each letter
        counts = {}

        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        

        stack = []
        seen = set()

        for letter in s:
            counts[letter] -= 1

            if letter in seen:
                continue
        
            while stack and letter < stack[-1] and counts[stack[-1]] > 0:
                # bca bc deleted --> abc
                removed = stack.pop()
                seen.remove(removed)

            stack.append(letter)
            seen.add(letter)

        return ''.join(stack)