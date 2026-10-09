<h2><a href="https://leetcode.com/problems/first-bad-version">278. First Bad Version</a></h2>

<p>You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.</p>

<p>Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.</p>

<p>You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 5, bad = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong>
call isBadVersion(3) -&gt; false
call isBadVersion(5)&nbsp;-&gt; true
call isBadVersion(4)&nbsp;-&gt; true
Then 4 is the first bad version.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 1, bad = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bad &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


---

# 🛍️ First-Bad-Version | Explained

## Approach 1: Binary Search (Boundary Convergence)

### Intuition
Imagine an assembly line of products stamped sequentially from $1$ to $n$. A machine malfunction occurs at some point: every item made before that point is intact (`False`), and every item made at or after that point is defective (`True`). 

Because all versions after a bad version are also bad, the system status is strictly monotonic:
`[Good, Good, Good, ..., Bad, Bad, Bad]`

If you test items one by one starting from 1, you might end up making $n$ checks in the worst case. Instead, test the item directly in the middle. If it's defective, you instantly know the very first defective item must be this item or somewhere to its left. If it's intact, the first defect must have occurred strictly to the right. By halving the candidate window at each step, you eliminate half of the remaining versions with a single API call.

### Algorithm Visualized
```mermaid
flowchart TD
    Start([Start: Search Range [left, right]]) --> LoopCheck{left < right?}
    LoopCheck -- Yes --> CalcMid["mid = (left + right) // 2"]
    CalcMid --> APICall{"isBadVersion(mid)"}
    
    APICall -- True --> Defective["First bad version is at or before mid<br/>right = mid"]
    APICall -- False --> Intact["mid is good; bad version must be after mid<br/>left = mid + 1"]
    
    Defective --> LoopCheck
    Intact --> LoopCheck
    
    LoopCheck -- No (left == right) --> Converged["Pointers converged on first bad version"]
    Converged --> End([Return left])
```

### Approach
1. **Define the Search Space:** Initialize two pointers: `left = 1` and `right = n`, encompassing the entire range of potential versions.
2. **Loop Condition (`left < right`):** Maintain a loop that continues as long as there are at least two elements in the search space. Once `left == right`, the search window has collapsed to a single version, which must be the answer.
3. **Midpoint Inspection:** Compute the midpoint `mid = (left + right) // 2`.
4. **Pruning the Search Space:**
   - If `isBadVersion(mid)` is `True`: `mid` might be the *first* bad version, or the first bad version occurred earlier. Therefore, `mid` cannot be eliminated entirely, but anything strictly greater than `mid` can be discarded. We update `right = mid`.
   - If `isBadVersion(mid)` is `False`: Version `mid` is verified good, meaning the first bad version must exist strictly after `mid`. We update `left = mid + 1`.
5. **Termination:** When `left == right`, the search space has shrunk to a single index representing the earliest defective version. Return `left`.

### Detailed Code Analysis

```python
class Solution(object):
    def firstBadVersion(self, n):
```
- The function signature receives an integer `n` denoting the total number of versions and returns an integer corresponding to the index of the first defective version.

```python
        left, right = 1, n
```
- Sets the boundary of our search space. Since versions are 1-indexed (from $1$ to $n$), `left` starts at $1$ and `right` starts at $n$.

```python
        while left < right:
```
- Uses a strict inequality (`<`) rather than `<=`. This is intentional because `right` is updated to `mid` (not `mid - 1`). If `left <= right` were used alongside `right = mid`, the loop would spin infinitely when `left == right`. By terminating when `left == right`, the pointers converge on the boundary element without an explicit `return` inside the loop.

```python
            mid = (left + right) // 2
```
- Computes the middle index using integer division.
- *Language note:* In Python, integers have arbitrary precision, so `(left + right) // 2` cannot overflow. In statically typed languages like C++ or Java, `left + (right - left) // 2` is standard to avoid 32-bit signed integer overflow.

```python
            if isBadVersion(mid):
                right = mid
```
- Queries the given black-box API.
- If `mid` is bad, it is a candidate for the answer. We cannot discard it, so we set `right = mid` instead of `mid - 1`. This safely discards all elements in the range `[mid + 1, right]`.

```python
            else:
                left = mid + 1
```
- If `mid` is not bad, it cannot possibly be the first bad version. We discard `mid` and everything before it by shifting the lower boundary to `mid + 1`.

```python
        return left
```
- Upon exiting the `while` loop, invariant `left == right` holds true. The range has converged onto the exact index where the condition toggles from `False` to `True`. Returning `left` (or `right`) gives the first bad version.

### Code
```python
class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

### Complexity
- **Time Complexity:** $\mathcal{O}(\log n)$. The search interval is divided in half during each iteration, requiring at most $\lceil \log_2(n) \rceil$ calls to the `isBadVersion` API.
- **Space Complexity:** $\mathcal{O}(1)$. The algorithm operates in-place using two scalar pointer variables (`left` and `right`) and an auxiliary variable (`mid`), maintaining strictly constant additional memory.

---

## 🕵️‍♂️ Follow-up Questions

### 1. How would you prevent integer overflow in lower-level languages like C++ or Java?
In languages with fixed-width integers (e.g., 32-bit signed integers where max value is $2^{31} - 1 \approx 2.14 \times 10^9$), computing `left + right` can overflow if $n$ is close to the upper limit.
To prevent this, calculate `mid` using subtraction:
```c
int mid = left + (right - left) / 2;
```
This produces the identical midpoint without ever exceeding the upper boundary `right`.

### 2. What if the total number of versions $n$ is unbounded or unknown (Infinite Stream)?
If $n$ is not provided upfront, you can use **Exponential Search** (Galloping Search):
1. Start at index $1$ and double the index consecutively ($1, 2, 4, 8, 16, \dots$) until `isBadVersion(k)` returns `True`.
2. Once an upper bound $k$ is found, the first bad version is guaranteed to lie in the range $[k/2, k]$.
3. Run this exact standard binary search within $[k/2, k]$. The overall time complexity remains $\mathcal{O}(\log k)$, where $k$ is the position of the first bad version.