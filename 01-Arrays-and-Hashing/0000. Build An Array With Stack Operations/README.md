<h2><a href="https://leetcode.com/problems/build-an-array-with-stack-operations">0000. Build An Array With Stack Operations</a></h2>

<p>You are given an integer array <code>target</code> and an integer <code>n</code>.</p>

<p>You have an empty stack with the two following operations:</p>

<ul>
	<li><strong><code>"Push"</code></strong>: pushes an integer to the top of the stack.</li>
	<li><strong><code>"Pop"</code></strong>: removes the integer on the top of the stack.</li>
</ul>

<p>You also have a stream of the integers in the range <code>[1, n]</code>.</p>

<p>Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to <code>target</code>. You should follow the following rules:</p>

<ul>
	<li>If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.</li>
	<li>If the stack is not empty, pop the integer at the top of the stack.</li>
	<li>If, at any moment, the elements in the stack (from the bottom to the top) are equal to <code>target</code>, do not read new integers from the stream and do not do more operations on the stack.</li>
</ul>

<p>Return <em>the stack operations needed to build </em><code>target</code> following the mentioned rules. If there are multiple valid answers, return <strong>any of them</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> target = [1,3], n = 3
<strong>Output:</strong> ["Push","Push","Pop","Push"]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> target = [1,2,3], n = 3
<strong>Output:</strong> ["Push","Push","Push"]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> target = [1,2], n = 4
<strong>Output:</strong> ["Push","Push"]
<strong>Explanation:</strong> Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= target[i] &lt;= n</code></li>
	<li><code>target</code> is strictly increasing.</li>
</ul>


---

# 🛍️ Build-An-Array-With-Stack-Operations | Explained

## Approach 1: Hash Set Simulation with Early Stopping

### Intuition
Imagine you are standing in front of a conveyor belt that dispenses numbered items sequentially: $1, 2, 3, 4, \dots, n$. You have a box (your stack), and your goal is to leave only the numbers specified in `target` inside the box, in that exact order. 

Because the stream only provides numbers in increasing order and you must process them one by one, whenever an item arrives, you are forced to pick it up and place it into the box (`"Push"`). If that item is on your shopping list (`target`), you keep it. If it is not on your list, you immediately discard it from the box (`"Pop"`). Once you have secured the highest number on your list (`target[-1]`), you do not need to look at any subsequent items coming down the belt, so you can stop early.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start Loop: i = 1 to target[-1]]) --> PushOp["Append 'Push' to results"]
    PushOp --> CheckSet{"Is i in target_set?"}
    CheckSet -- Yes --> NextIter{"i == target[-1]?"}
    CheckSet -- No --> PopOp["Append 'Pop' to results"]
    PopOp --> NextIter
    NextIter -- No --> Inc["i = i + 1"] --> PushOp
    NextIter -- Yes --> End([Return results])
```

### Approach
1. **Identify the Boundary:** The `target` array is strictly increasing. Therefore, the largest element we ever need to consider is the last element, `target[-1]`. We define `max_val = target[-1]`.
2. **Fast Membership Check:** Convert `target` into a hash set (`target_set`) so that checking if any stream number `i` belongs in our final array takes $O(1)$ average time.
3. **Iterate Stream:** Loop through every integer $i$ from $1$ up to `max_val` inclusive:
   - Always append `"Push"` because the number must enter the stack first.
   - If $i$ is not found in `target_set`, immediately append `"Pop"` to remove it.
4. **Return Result:** Once the loop finishes at `max_val`, return the recorded list of operations.

### Detailed Code Analysis

```python
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        results = []
        target_set = set(target)
        max_val = target[-1]  # We only need to process up to the last element in target
        
        for i in range(1, max_val + 1):
            results.append("Push")
            if i not in target_set:
                results.append("Pop")
                
        return results
```

* **Line 3 (`results = []`):** Initializes the dynamic array to collect the sequence of string operations (`"Push"` and `"Pop"`).
* **Line 4 (`target_set = set(target)`):** Converts the input list into a hash set. This provides $O(1)$ average-time complexity for lookups inside the loop, preventing an $O(k)$ linear search per iteration.
* **Line 5 (`max_val = target[-1]`):** Reads the last element in `target`. Because the problem statement guarantees that `target` is strictly increasing, the stream of numbers beyond `target[-1]` is irrelevant. This avoids iterating all the way to $n$.
* **Line 7 (`for i in range(1, max_val + 1):`):** Generates the stream of integers sequentially starting from $1$ up to `max_val`.
* **Line 8 (`results.append("Push")`):** Every number in the stream must be pushed onto the stack initially to be inspected or retained. *(Note: The raw identifiers `Push` and `Pop` in the original snippet are treated as string literals `"Push"` and `"Pop"` as required by LeetCode).*
* **Lines 9–10 (`if i not in target_set: results.append("Pop")`):** If the current integer $i$ is an unwanted value, it cannot remain in the stack. Appending `"Pop"` cancels out the preceding `"Push"`, effectively discarding $i$.
* **Line 12 (`return results`):** Returns the final sequence of stack operations.

### Complexity
- **Time Complexity:** $O(M)$, where $M = \text{target}[-1]$ (with $M \le n$). 
  - Converting `target` of length $k$ to a set takes $O(k)$ time.
  - The loop runs $M$ times. In each iteration, set membership lookup and array appends run in $O(1)$ time.
  - Since $k \le M \le n$, the total time complexity is bounded by $O(M)$.
- **Space Complexity:** $O(k)$ auxiliary space, where $k$ is the length of `target`.
  - Storing elements in `target_set` requires $O(k)$ memory.
  - (Excluding the output array `results`, which is required for returning the answer).

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **Can we optimize this to $O(1)$ auxiliary space?**
   - **Answer:** Yes. Since `target` is already sorted in strictly increasing order, we do not need a hash set. We can maintain a pointer index `target_idx = 0`. For each integer `i` from `1` to `target[-1]`, if `i == target[target_idx]`, we append `"Push"` and increment `target_idx`. Otherwise, we append `"Push"` followed by `"Pop"`. This reduces auxiliary space to $O(1)$.

2. **What if the target array was not guaranteed to be strictly increasing, or could contain duplicates?**
   - **Answer:** The problem premise relies on the stack maintaining a strictly increasing sequence derived from the stream $[1, 2, \dots, n]$. If duplicates or decreasing values were allowed, a standard linear push-pop sequence from an increasing stream would be unable to produce non-monotonic configurations without a secondary buffer or multiple pop stages.