Approach 1: Simple Sorting

**Intuition**
​

Do what the question says.

​
**Algorithm**

​
Store the numbers in a window container of size kk. The following operations must take place:
​
Inserting the incoming element.

Deleting the outgoing element.

Sorting the window to find the medians.

One primitive approach is to copy kk consecutive elements from the input to the window and keep sorting these every time. This constitutes duplication of effort.

​
We can do a bit better if we instead insert and delete one element per window shift. The challenge then is to maintain the window as sorted, before and after the insert and delete operations.

​
Python comes with an excellent bisect module to help perform efficient insert operations on lists while maintaining their sorted property.
​
## Complexity Analysis
```

Time complexity: O(n⋅klogk) to O(n⋅k).

​
Copying elements into the container takes about O(k) time each. This happens about (n−k) times.

​
Sorting for each of the (n−k) sliding window instances takes about O(k.logk) time each.

​
Bisected insertion or deletion takes about O(logk) for searching and O(k) for actual shifting of elements. This takes place about n times.

​
Space complexity: O(k) extra linear space for the window container.

```
