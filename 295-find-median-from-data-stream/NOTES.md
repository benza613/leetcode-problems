## Two Heaps
​
current solution -
- Time complexity: O(5⋅logn)+O(1)≈O(logn).
- At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about O(\log n)O(logn) time.
- Finding the median takes constant O(1)O(1) time since the tops of heaps are directly accessible.
- Space complexity: O(n)O(n) linear space to hold input in containers.
​
​
## alternatives
​
Reservoir Sampling. Following along the lines of using buckets: if the stream is statistically distributed, you can rely on Reservoir Sampling. Basically, if you could maintain just one good bucket (or reservoir) which could hold a representative sample of the entire stream, you could estimate the median of the entire stream from just this one bucket. This means good time and memory performance. Reservoir Sampling lets you do just that. Determining a "good" size for your reservoir? Now, that's a whole other challenge. A good explanation for this can be found in this [StackOverflow](https://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers/10693752#10693752) answer.
​
Segment Trees are a great data structure if you need to do a lot of insertions or a lot of read queries over a limited range of input values. They allow us to do all such operations fast and in roughly the same amount of time, always. The only problem is that they are far from trivial to implement. Take a look at my introductory article on Segment Trees if you are interested.
​
Order Statistic Trees are data structures which seem to be tailor-made for this problem. They have all the nice features of a BST, but also let you find the k-th order element stored in the tree. They are a pain to implement and no standard interview would require you to code these up. But they are fun to use if they are already implemented in the language of your choice.