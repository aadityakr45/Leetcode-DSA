<h2><a href="https://leetcode.com/problems/set-mismatch">0000. Set Mismatch</a></h2>

<p>You have a set of integers <code>s</code>, which originally contains all the numbers from <code>1</code> to <code>n</code>. Unfortunately, due to some error, one of the numbers in <code>s</code> got duplicated to another number in the set, which results in <strong>repetition of one</strong> number and <strong>loss of another</strong> number.</p>

<p>You are given an integer array <code>nums</code> representing the data status of this set after the error.</p>

<p>Find the number that occurs twice and the number that is missing and return <em>them in the form of an array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2,4]
<strong>Output:</strong> [2,3]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Set-Mismatch | Explained

## Approach 1: Frequency Counting with Hash Map (Counter)

### Intuition
Imagine a classroom roll call where every student is assigned an ID badge numbered strictly from $1$ to $n$. When the teacher calls roll, each student signs their name on a sign-in sheet. If someone signs in twice and another student is absent, the sign-in sheet will show one name with a tally count of $2$, while the absent student's name has a tally count of $0$.

By tabulating the frequency of each number in the array using a hash map (or Python's `Counter`), we can check every expected integer from $1$ to $n$ against our tally sheet. The number missing from the tally is our missing element, and the number recorded with a frequency greater than $1$ is our duplicate.

### Algorithm Visualized

```mermaid
flowchart TD
    A[Start: nums = 1, 2, 2, 4] --> B[Build Counter: c = {1:1, 2:2, 4:1}]
    B --> C[Loop i from 1 to n=4]
    
    C --> D{Is i in c?}
    D -- No --> E[missing_n = i]
    D -- Yes --> F{Is c[i] == 2?}
    
    F -- Yes --> G[repeated_n = i]
    F -- No --> H[Normal element: continue]
    
    E --> I[Next i]
    G --> I
    H --> I
    
    I --> J{Loop finished?}
    J -- No --> C
    J -- Yes --> K[Return repeated_n, missing_n]
```

### Approach
1. **Count Frequencies**: Build a frequency map of `nums` using `collections.Counter`. This produces a mapping of each distinct integer to its occurrence count.
2. **Initialize Tracking Variables**: Set up placeholders `repeated_n` and `missing_n` to store the two target values.
3. **Scan the Expected Range**: Iterate through every integer $i$ from $1$ up to $n$ (where $n = \text{len}(nums)$):
   - **Check for Absence**: If $i$ does not exist in the map, it was never present in `nums`. Set `missing_n = i`.
   - **Check for Duplication**: If $i$ is in the map, check if its frequency is $2$. If so, set `repeated_n = i`.
4. **Return Results**: Once the loop finishes checking all values from $1$ to $n$, return `[repeated_n, missing_n]`.

### Detailed Code Analysis

```python
from collections import Counter
```
- Imports the `Counter` class from Python's standard `collections` module, which specializes in counting hashable objects.

```python
c = Counter(nums)
```
- Traverses the input list `nums` once and builds a hash map where keys are numbers and values are their occurrence counts. Constructing this dictionary takes $O(n)$ time and $O(n)$ space.

```python
repeated_n = 0
missing_n = 0
```
- Allocates two integer variables initialized to `0` to store the result tuple as the loop identifies the duplicate and absent values.

```python
for i in range(1, len(nums) + 1):
```
- Sets up an iteration over the full range of expected values $[1, n]$. Because Python's `range(start, stop)` is exclusive of `stop`, `len(nums) + 1` ensures that $n$ is evaluated.

```python
    if i not in c.keys():
        missing_n = i
    else:
        if c[i] == 2:
            repeated_n = i
```
- Completes the conditional check inside the loop:
  - `if i not in c.keys()`: Queries whether the expected number $i$ was recorded. In Python 3, `c.keys()` returns a dictionary keys view, which performs membership testing via hash lookup in $O(1)$ average time. If $i$ is not found, it is assigned to `missing_n`.
  - `else: if c[i] == 2`: If $i$ is present, its frequency is checked. If it appeared twice, it is assigned to `repeated_n`.

```python
return [repeated_n, missing_n]
```
- Returns the results in the required format: `[duplicate, missing]`.

### Code

```python
from collections import Counter

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        repeated_n = 0
        missing_n = 0
        
        for i in range(1, len(nums) + 1):
            if i not in c.keys():
                missing_n = i
            else:
                if c[i] == 2:
                    repeated_n = i
                    
        return [repeated_n, missing_n]
```

### Complexity
- **Time:** $O(n)$
  - Building the `Counter` takes $O(n)$ time to scan through all elements in `nums`.
  - The `for` loop runs $n$ iterations. In each iteration, membership testing (`i not in c.keys()`) and value lookup (`c[i]`) execute in $O(1)$ average time on a hash table.
  - Overall time complexity is $O(n) + O(n) = O(n)$.
- **Space:** $O(n)$
  - The `Counter` dictionary stores up to $n$ unique keys and their integer counts, requiring $O(n)$ auxiliary memory.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **Can this problem be solved in $O(1)$ auxiliary space if modifying the input array is allowed?**
   - **Answer:** Yes, using **Negative Index Marking**. Because all values lie in the range $[1, n]$, each value $x = |nums[i]|$ can be mapped directly to an index $x - 1$. As we iterate, we negate the value at index $x - 1$ (`nums[x - 1] = -nums[x - 1]`). If the value at that index is already negative, $x$ is our duplicate. In a second pass, the only index holding a positive value corresponds to the missing number (`index + 1`). This achieves $O(n)$ time and $O(1)$ auxiliary space.

2. **Can this problem be solved in $O(1)$ auxiliary space without modifying the input array?**
   - **Answer:** Yes, using **Bit Manipulation (XOR)** or **Mathematical Equations**:
     - *Math:* Let $S$ be the sum of numbers from $1$ to $n$, and $P$ be the sum of squares. Calculate $\Delta_1 = \sum nums - S = \text{dup} - \text{mis}$, and $\Delta_2 = \sum nums^2 - P = \text{dup}^2 - \text{mis}^2$. Since $\text{dup} + \text{mis} = \Delta_2 / \Delta_1$, solving the linear system yields both numbers in $O(n)$ time and $O(1)$ space.
     - *XOR:* XORing all array elements with all integers from $1$ to $n$ cancels out all correct numbers, leaving $\text{dup} \oplus \text{mis}$. Finding the lowest set bit partitions the numbers into two groups, isolating both values in $O(n)$ time and $O(1)$ space without integer overflow risks.