<h2><a href="https://leetcode.com/problems/max-consecutive-ones">487. Max Consecutive Ones II</a></h2>

<p>Given a binary array <code>nums</code>, return <em>the maximum number of consecutive </em><code>1</code><em>'s in the array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,0,1,1,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,0,1,1,0,1]
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


---

# 🛍️ Max-Consecutive-Ones-II | Explained

## Approach 1: Single-Pass Streak Reset (No-Flip Counter)
### Intuition
Imagine walking along a track where you are counting consecutive green lights (`1`s). Every time you see a green light, your streak increments by one. The moment you hit a red light (`0`), your current streak is broken: you record your best score so far, reset your counter back to zero, and begin counting anew from the next light.

*Note on Problem Context:* In LeetCode 487 (*Max Consecutive Ones II*), the problem allows flipping at most **one** `0` to a `1`. The provided code implements a strict zero-flip streak counter (the exact solution to LeetCode 485, *Max Consecutive Ones I*). It treats every `0` as an immediate delimiter rather than using the available flip allowance.

### Algorithm Visualized
```mermaid
flowchart TD
    A[Start: i = 0, count = 0, max_count = 0] --> B{i < len nums?}
    B -- Yes --> C{nums[i] == 1?}
    C -- Yes --> D[count = count + 1]
    C -- No --> E["max_count = max(count, max_count)"]
    E --> F[count = 0]
    D --> G[i = i + 1]
    F --> G
    G --> B
    B -- No --> H["return max(count, max_count)"]
```

### Approach
1. **Initialize State Trackers:** 
   - `count`: Tracks the current running streak of consecutive `1`s.
   - `max_count`: Stores the highest streak achieved across all evaluated subarrays.
2. **Iterate Through the Input Array:**
   - Loop index `i` through `0` to `len(nums) - 1`.
   - **Case 1 (`nums[i] == 1`):** Extend the active streak by incrementing `count` by 1.
   - **Case 2 (`nums[i] == 0`):** The streak has ended. Update `max_count` with `max(count, max_count)` to safeguard the maximum seen so far, then reset `count` to `0`.
3. **Handle Edge Case (Trailing Ones):**
   - If the array terminates with a sequence of `1`s, the loop finishes without executing the `else` block for those trailing elements. A final `max(count, max_count)` evaluation ensures any trailing streak is compared against `max_count` before returning.

### Detailed Code Analysis
```python
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        count,max_count=0,0
```
- Line 3 initializes two integer variables, `count` and `max_count`, to `0`. `count` tracks the local streak; `max_count` tracks the global maximum.

```python
4        for i in range(len(nums)):
5            if nums[i]==1:
6                count=count+1
```
- Line 4 begins a standard index-based traversal across `nums`.
- Lines 5–6 inspect the current value: if it is `1`, the active sequence continues, and `count` is incremented by 1.

```python
7            else:
8                max_count=max(count,max_count)
9                count=0
```
- Lines 7–9 execute when `nums[i]` is not `1` (it is `0`). 
- Line 8 performs an update: `max_count = max(count, max_count)`. The longest sequence encountered prior to this zero is persisted.
- Line 9 flushes the active counter (`count = 0`), meaning no historical context or flip allowance is carried across the zero boundary.

```python
10        return max(count,max_count)
```
- Line 10 handles the final state. If the array ends on a `1`, `count` holds the length of the final streak which was never committed to `max_count` inside the loop. Returning `max(count, max_count)` resolves this boundary condition cleanly.

### Code
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(count, max_count)
```

### Complexity
- **Time:** $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`. The algorithm traverses the array in a single pass using a standard `for` loop, performing $\mathcal{O}(1)$ operations per element.
- **Space:** $\mathcal{O}(1)$ auxiliary space. Only two integer scalar variables (`count` and `max_count`) are allocated regardless of the input size.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **How does this code need to change to satisfy the LeetCode 487 constraint (allowing at most one `0` to be flipped to `1`)?**
   - To support 1 flip, we must allow the window to bridge across a single zero. This can be achieved in $\mathcal{O}(N)$ time and $\mathcal{O}(1)$ space by maintaining two counters: `current_streak` (streak after the most recent zero) and `previous_streak` (streak before the most recent zero), or by using a sliding window where the window expands while the count of zeros inside is $\le 1$.

2. **What if the input is an infinite data stream that cannot fit into memory?**
   - A sliding window approach that stores indices of zeros would require $\mathcal{O}(K)$ space where $K$ is the number of allowed flips. For $K=1$, keeping just the index of the last seen zero in memory allows streaming updates in $\mathcal{O}(1)$ space and $\mathcal{O}(1)$ time per incoming number.