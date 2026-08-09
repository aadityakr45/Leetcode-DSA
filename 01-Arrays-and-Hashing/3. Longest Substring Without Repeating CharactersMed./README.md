<h2><a href="https://leetcode.com/problems/longest-substring-without-repeating-characters">3. Longest Substring Without Repeating CharactersMed.</a></h2>

<p>You are given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?

---

# 🛍️ Longest-Substring-Without-Repeating-CharactersMed. | Explained

## Approach 1: Dynamic Sliding Window with Hash Set

### Intuition
Imagine a flexible window frame sliding over a strip of unique symbols. As long as the window contains distinct symbols, we stretch its right edge further to expand our view. The moment a duplicate symbol enters from the right edge, our window becomes invalid. To restore validity, we do not start over from scratch; instead, we shrink the window from its left edge—removing characters one by one—until the newly added character is no longer a duplicate inside our window.

This dynamic expansion (`right` pointer) and contraction (`left` pointer) ensures that every valid window candidate is checked efficiently without redundant re-checks.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start Loop: right from 0 to len s - 1]) --> CheckDup{s[right] in char_set?}
    
    CheckDup -- Yes --> RemoveLeft[Remove s[left] from char_set]
    RemoveLeft --> IncLeft[left = left + 1]
    IncLeft --> CheckDup
    
    CheckDup -- No --> AddChar[Add s[right] to char_set]
    AddChar --> UpdateMax[Update max_len = max max_len, right - left + 1]
    UpdateMax --> NextIter{More characters?}
    
    NextIter -- Yes --> Start
    NextIter -- No --> End([Return max_len])
```

### Approach
1. **Initialize State**: Maintain a variable `max_len` to store the maximum substring length found, a `left` pointer to track the start of the current window, and a `char_set` (hash set) to track unique characters in the current window.
2. **Expand Window**: Iterate a `right` pointer across the string from index `0` to `len(s) - 1`.
3. **Handle Duplicates**: Before adding `s[right]` to `char_set`, check if it already exists in `char_set`. While it exists:
   - Evict `s[left]` from `char_set`.
   - Increment `left` by 1 to shrink the window boundary from the left.
4. **Update Window State**: Add `s[right]` into `char_set`.
5. **Track Maximum**: Calculate the current window size `(right - left + 1)` and update `max_len` if this size exceeds the current `max_len`.
6. **Return Result**: Once the loop completes, return `max_len`.

---

### Detailed Code Analysis

Let's dissect the provided Python solution step-by-step:

- **State Initialization**:
  ```python
  max_len = 0
  char_set = set()
  left = 0
  ```
  `max_len` keeps track of our best result. `char_set` is chosen because a Python `set` is backed by a hash table, offering average $O(1)$ time complexity for lookup (`in`), insertion (`add`), and deletion (`remove`). `left` marks the left boundary of our active sliding window.

- **Window Expansion Loop**:
  ```python
  for right in range(len(s)):
  ```
  The `right` variable serves as the right boundary of the window, advancing index by index through the input string `s`.

- **Contracting the Window on Duplicates**:
  ```python
  while (s[right] in char_set):
      char_set.remove(s[left])
      left = left + 1
  ```
  If `s[right]` is already inside `char_set`, the substring in window `[left, right]` contains a duplicate. The `while` loop continuously shrinks the window from the left by removing `s[left]` from `char_set` and incrementing `left` until `s[right]` becomes unique in the active set.

- **Updating the Set & Missing Lines**:
  ```python
  char_set.add(s[right])
  ```
  Once uniqueness is guaranteed, `s[right]` is safely added to `char_set`.

  > ⚠️ **Code Review Note**: In the provided snippet, two crucial steps are missing to make the solution functional on LeetCode:
  > 1. Updating `max_len`: Inside the `for` loop, you must update `max_len = max(max_len, right - left + 1)` to record the maximum valid window size.
  > 2. Return statement: The function must explicitly `return max_len` at the end.

---

### Code

Here is the cleaned and formatted version of your exact algorithm logic (with the missing record update and return statement included):

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_set = set()
        left = 0
        
        for right in range(len(s)):
            # Shrink window from the left until duplicate s[right] is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left = left + 1
            
            # Include s[right] in the set
            char_set.add(s[right])
            
            # Maintain the maximum valid window size seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len
```

---

### Complexity

- **Time Complexity:** $\mathcal{O}(N)$  
  Although there is a nested `while` loop inside the `for` loop, each character in the string `s` is processed at most twice: once added to `char_set` by the `right` pointer, and at most once removed from `char_set` by the `left` pointer. Therefore, total operations are bounded by $2N$, which simplifies to linear time $\mathcal{O}(N)$, where $N$ is the length of string `s`.

- **Space Complexity:** $\mathcal{O}(\min(N, M))$  
  Space complexity depends on the size of the character set $M$ (e.g., English alphabet $M=26$, ASCII $M=128$, or Extended ASCII $M=256$). In the worst case where all characters are distinct, the `set` will store at most $\min(N, M)$ characters. Thus, space complexity is $\mathcal{O}(\min(N, M))$, which is effectively $\mathcal{O}(1)$ auxiliary space if the character set bound $M$ is fixed.

---

## 🕵️‍♂️ Follow-up Questions

### 1. How can we optimize this approach so the `left` pointer jumps directly instead of stepping one-by-one?
**Answer:** Instead of using a set and removing elements incrementally with a `while` loop, we can use a **Hash Map** storing the last seen index of each character (`char -> index`). When a duplicate `s[right]` is seen at index `last_seen`, we can immediately jump `left = max(left, last_seen + 1)`. This avoids the inner `while` loop entirely and cuts down hash set deletion operations.

### 2. What if the input string contains only standard ASCII characters?
**Answer:** If the character set is strictly standard ASCII (128 characters), we can replace the dynamic hash set with a fixed-size integer/boolean array of size `128` (or direct lookup array indexed by character ASCII codes `ord(char)`). This eliminates hash overhead, reducing memory overhead and improving cache locality for execution speed.