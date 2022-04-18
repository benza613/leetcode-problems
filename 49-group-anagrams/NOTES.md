Approach 1:
![49_groupanagrams1](https://leetcode.com/problems/group-anagrams/Figures/49_groupanagrams1.png)
​
```
Complexity Analysis
​
Time Complexity: O(NK logK), where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K logK) time.
​
Space Complexity: O(NK), the total information content stored in ans.
​
```
Approach 2: using 26 bit tuple
​
```
Complexity Analysis for alternate approach
​
Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
​
Space Complexity: O(NK), the total information content stored in ans.
```