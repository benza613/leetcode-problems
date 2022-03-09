import collections
import unittest

class Solution:
    def decodeString(self, string) -> str: 

        result = ""
        stack = collections.deque()

        for ch in string:
            if ch == "[":
                stack.append(result)
                result = ""
            elif ch.isdigit(): 
                result = stack.pop() + result* int(ch)
            elif ch.isalpha(): 
                result += ch

        return result  


if __name__ == '__main__':
    result = Solution().decodeString("def[ab[cd]{2}]{3}ghi")
    assert result == "defabcdcdabcdcdabcdcdghi"
