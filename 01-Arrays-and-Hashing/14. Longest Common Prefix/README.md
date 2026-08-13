<h2><a href="https://leetcode.com/problems/longest-common-prefix">14. Longest Common Prefix</a></h2>

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>


---

# 🛍️ Longest-Common-Prefix | Explained

## Approach 1: Lexicographical Sorting & Boundary Comparison
### Intuition
Imagine you have a stack of words printed on index cards and you arrange them alphabetically in a physical dictionary. For example, if you sort `["flower", "flow", "flight", "dog"]`, the sorted order becomes `["dog", "flight", "flow", "flower"]`. 

Notice what happens: words that share the same starting letters naturally group together, while words with different starting letters are pushed to opposite ends of the sorted list. 

Because the list is ordered lexicographically, the two strings that are **most different** from each other will end up at the extreme boundaries—index `0` (the first element) and index `-1` (the last element). If the first and last strings share a common prefix, every single string sandwiched between them in the sorted array must also share that exact same prefix. Thus, instead of comparing all strings against each other, we only need to compare the first and last strings character by character!

### Algorithm Visualized
```mermaid
flowchart TD
    A[Input: strs] --> B[Sort strs lexicographically]
    B --> C[Set first_ele = strs[0]]
    B --> D[Set last_ele = strs[-1]]
    C --> E[Iterate i from 0 to min len of first_ele, last_ele]
    D --> E
    E --> F{first_ele[i] == last_ele[i]?}
    F -- Yes --> G[Append char to lg_cm_str]
    G --> E
    F -- No --> H[Return lg_cm_str immediately]
    E -- Loop ends --> I[Return lg_cm_str]
```

### Approach
1. Initialize an empty string `lg_cm_str` to accumulate the matching common prefix.
2. Sort the input list `strs` lexicographically in-place using Python's `sort()`.
3. Select the first string (`first_ele = strs[0]`) and the last string (`last_ele = strs[-1]`).
4. Calculate the minimum length between `first_ele` and `last_ele` to avoid index out-of-bounds errors during iteration.
5. Iterate through both strings character by character at each index `i`:
   - If `first_ele[i]` does not match `last_ele[i]`, stop and immediately return `lg_cm_str`.
   - If they match, append `first_ele[i]` to `lg_cm_str`.
6. If the loop completes without finding a mismatch, return `lg_cm_str`.

### Detailed Code Analysis
Let's break down the exact execution of your Python code:

* **Line 3: `lg_cm_str = ""`**  
  *(Note: Corrected the missing initial value typo from `lg_cm_str=` to `lg_cm_str = ""`)*. This initializes our string accumulator. We start with an empty string so that if no common prefix exists across the input, we naturally return `""`.

* **Line 4: `strs.sort()`**  
  This sorts the array of strings in ASCII/lexicographical order. Python uses **Timsort**, which compares strings character by character. After sorting, `strs[0]` contains the lexicographically smallest string and `strs[-1]` contains the lexicographically largest string.

* **Lines 5–6: `first_ele = strs[0]` and `last_ele = strs[-1]`**  
  We capture the two extreme elements. Any character sequence shared by both `first_ele` and `last_ele` is guaranteed to be shared by every string in between.

* **Line 7: `for i in range(min(len(first_ele), len(last_ele))):`**  
  We limit the loop upper bound to `min(len(first_ele), len(last_ele))`. This prevents an `IndexError` when one string is shorter than the other.

* **Lines 8–9: `if first_ele[i] != last_ele[i]: return lg_cm_str`**  
  At the first index where `first_ele` and `last_ele` differ, the common prefix ends. We return `lg_cm_str` immediately, providing an early exit optimization.

* **Line 10: `lg_cm_str += first_ele[i]`**  
  If the characters at index `i` are identical, we concatenate that character to our result variable.

* **Line 11: `return lg_cm_str`**  
  If the loop finishes entirely (meaning one string was a complete prefix of the other), we return the accumulated string.

### Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lg_cm_str = ""
        strs.sort()
        first_ele = strs[0]
        last_ele = strs[-1]
        for i in range(min(len(first_ele), len(last_ele))):
            if first_ele[i] != last_ele[i]:
                return lg_cm_str
            lg_cm_str += first_ele[i]
        return lg_cm_str
```

### Complexity
- **Time Complexity:** $\mathcal{O}(N \cdot K \log N + K)$  
  - Sorting an array of $N$ strings where each string has a maximum length of $K$ requires comparing strings, taking $\mathcal{O}(N \cdot K \log N)$ time.
  - The subsequent `for` loop runs at most $K$ times, taking $\mathcal{O}(K)$ time.
  - Overall time complexity is dominated by the sorting step: $\mathcal{O}(N \cdot K \log N)$.

- **Space Complexity:** $\mathcal{O}(N \cdot K)$ or $\mathcal{O}(1)$ auxiliary space  
  - Python's `sort()` (Timsort) requires $\mathcal{O}(N)$ extra space to store pointers/references during sorting.
  - The memory used by `lg_cm_str` takes $\mathcal{O}(K)$ space to hold the output string.

---

## 🕵️‍♂️ Follow-up Questions

### 1. Can we solve this problem in $\mathcal{O}(N \cdot K)$ time without sorting?
**Answer:** Yes! Sorting adds an unnecessary $\mathcal{O}(\log N)$ factor. We can achieve linear time $\mathcal{O}(N \cdot K)$ using **Vertical Scanning**:
- Iterate character by character through the first string (`strs[0]`).
- For each character at index `i`, check if all other strings in `strs` have the same character at index `i`.
- Stop and return as soon as a mismatch occurs or a string's length is exceeded.

### 2. How would you design a system to find the longest common prefix if strings are continually added and queried in real-time?
**Answer:** We should use a **Trie (Prefix Tree)** data structure:
- Insert all strings into a Trie where each node represents a character.
- To find the longest common prefix for all inserted strings, traverse from the root down as long as a node has **exactly one child** and is not marked as the end of a word (`is_end = False`).
- This allows query times proportional only to the length of the prefix $\mathcal{O}(K)$, independent of the total number of strings $N$.