import sys

class Solution:
    
    def myAtoi(self, s: str) -> int:
        
        MAX_INT = 2**31 -1
        MIN_INT = -(2**31)
        SIGN = 0 
        RESULT = 0
        
        s = s.strip()
        
        if len(s) == 0:
            return 0
        
        # check the 1 char 
        tmp = ord(s[0])
        
        if tmp != 45 and tmp != 43 and 48 > tmp > 57:
            return 0
        else :
            for idx, chr in enumerate(s):
                tmp = ord(chr)
                if tmp == 45 and idx == 0:
                    SIGN = -1
                # parse if valid number 
                elif 48 <= tmp <= 57:
                    RESULT =  int(chr) + (RESULT * 10)
                    
                    if SIGN == 0 and RESULT > MAX_INT:
                        return MAX_INT
                    elif SIGN == -1 and -RESULT < MIN_INT:
                        return MIN_INT
                # check if plus has been encountered before
                elif tmp == 43:
                    if idx > 0:
                        break
                else:    
                    break
                
            return RESULT if SIGN == 0 else -RESULT
    

x = Solution() 
print(x.myAtoi('42'))
print(x.myAtoi('-42'))
print(x.myAtoi('4193 with words'))
print(x.myAtoi('words and 987'))
print(x.myAtoi('-91283472332'))
print(x.myAtoi('3.14159'))
print(x.myAtoi('+1'))
print(x.myAtoi('13+1'))
print(x.myAtoi('+-12'))

## Interesting problem, weird edge cases
## prefer using for-loop with indexer so constraints for non-int chars are more easily fulfilled