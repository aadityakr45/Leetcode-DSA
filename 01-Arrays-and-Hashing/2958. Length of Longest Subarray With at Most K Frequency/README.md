<h2><a href="https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency">2958. Length of Longest Subarray With at Most K Frequency</a></h2>

<p>You are given an integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>The <strong>frequency</strong> of an element <code>x</code> is the number of times it occurs in an array.</p>

<p>An array is called <strong>good</strong> if the frequency of each element in this array is <strong>less than or equal</strong> to <code>k</code>.</p>

<p>Return <em>the length of the <strong>longest</strong> <strong>good</strong> subarray of</em> <code>nums</code><em>.</em></p>

<p>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3,1,2,3,1,2], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,1,2,1,2,1,2], k = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [5,5,5,5,5,5,5], k = 4
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
It can be shown that there are no good subarrays with length more than 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


---

# 🛍️ Length-of-Longest-Subarray-With-at-Most-K-Frequency | Explained

## Approach 1: Variable-Size Sliding Window with Dynamic Frequency Tracking

### Intuition

The problem asks for the maximum length of a contiguous subarray where no element appears more than $k$ times. This is a classic **Sliding Window (Two Pointers)** problem because a valid subarray exhibits a monotonic property: if a subarray `[left, right]` contains an element with frequency $> k$, expanding it further to the right will never make it valid again. 

Think of this like a security guard managing an exclusive nightclub with a strict capacity rule: **no guest can be inside the club more than $k$ times simultaneously**. 

As guests (`nums[right]`) enter through the front door, the guard updates a counter for each guest. If a guest tries to enter for the $(k+1)$-th time, a violation occurs! The guard must go to the back door (`nums[left]`) and start kicking out guests one by one in the order they arrived until the offending guest's count drops back down to $k$. Only then can the window resume expanding.

### Algorithm Visualized

```mermaid
graph TD
    Start([Start right Loop 0 to N]) --> EndCheck{right == N?}
    EndCheck -- Yes --> UpdateEndMax["max = Math.max(max, right - left)"] --> End([Return max])
    EndCheck -- No --> ReadNum["num = nums[right]"]
    ReadNum --> AddToMap["map[num] = map.getOrDefault(num, 0) + 1"]
    AddToMap --> CheckFreq{fre <= k?}
    CheckFreq -- Yes --> NextIter[Continue to next right]
    CheckFreq -- No --> RecordMax["max = Math.max(max, right - left)"]
    RecordMax --> ShrinkLoop{nums[left] != num?}
    ShrinkLoop -- Yes --> DecrementLeft["map[nums[left]]--<br/>left++"] --> ShrinkLoop
    ShrinkLoop -- No --> MatchFound["left++<br/>map[num] = fre - 1"] --> NextIter
```

---

### Approach

1. **Window Definition**: Maintain a sliding window bounded by `[left, right]`.
2. **Frequency Map**: Use a `HashMap<Integer, Integer>` to track the occurrence count of each integer within the active window.
3. **Expand Window (`right` pointer)**: Iteratively include `nums[right]` into the hash map.
4. **Detect Violation**: Check if the current element's frequency exceeds $k$.
   - **If Valid (`frequency <= k`)**: Continue expanding the window.
   - **If Invalid (`frequency > k`)**:
     1. Record the current maximum valid window length (`right - left`).
     2. Shrink the window from the left by advancing the `left` pointer. Decrement element counts in the map until reaching the first instance of `nums[right]`.
     3. Move `left` past that instance and manually set `num`'s frequency to $k$ (`fre - 1`).
5. **Handle Termination**: Since the loop boundary goes up to `right == nums.length`, perform a final evaluation of the window size when `right` reaches $N$ to capture any valid subarray extending to the end of the input array.

---

### Detailed Code Analysis

Let's dissect the implementation step-by-step:

#### 1. Data Structure & State Initialization
```java
HashMap<Integer, Integer> map = new HashMap<>();
int left = 0;
int max = 0;
int right = 0;
```
* `map`: Stores elements as keys and their current sliding-window frequencies as values.
* `left`: The left boundary of the sliding window.
* `right`: The right boundary of the sliding window.
* `max`: Stores the maximum valid window length encountered.

---

#### 2. Loop Execution & Upper Bound Handle
```java
for(; right <= nums.length; right++){

    if(right == nums.length){
        max = Math.max(max, right - left);
        continue;
    }
```
* The `for` loop condition `right <= nums.length` allows `right` to hit `nums.length`.
* **Why?** If the array ends while maintaining a valid window (or right after recovering from a violation), the max length needs to be updated one final time. `right - left` correctly represents the length of the window spanning from `left` up to `nums.length - 1`.

---

#### 3. Frequency Update & Validation
```java
    int num = nums[right];
    map.put(num, map.getOrDefault(num, 0) + 1);
    int fre = map.get(num);

    if(fre <= k) continue;
```
* Reads the current element `nums[right]` and increments its count in `map`.
* If `fre <= k`, the invariant holds: every element in `[left, right]` appears at most $k$ times. The algorithm proceeds to the next iteration to expand `right`.

---

#### 4. Violating Element Recovery Strategy
```java
    max = Math.max(max, right - left);

    while(nums[left] != num){
        map.put(nums[left], map.get(nums[left]) - 1);
        left++;
    }
    left++;
    map.put(num, fre - 1);
```
When `fre > k`, the current window `[left, right]` has just become invalid due to `num`.
1. `max = Math.max(max, right - left);`: The subarray `[left, right - 1]` was valid prior to adding `nums[right]`. Its length is `(right - 1) - left + 1 = right - left`. We capture this length before modifying `left`.
2. `while(nums[left] != num)`: Evicts elements from the left side of the window until the *first* occurrence of `num` inside the current window is reached. Each evicted element's count is decremented in `map`.
3. `left++`: Advances `left` past that first occurrence of `num`.
4. `map.put(num, fre - 1)`: Decrements the count of `num` from $k+1$ back down to $k$ to reflect the removal of its earliest occurrence.

---

### Code

```java
class Solution {

    public int maxSubarrayLength(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        int left = 0;
        int max = 0;
        int right = 0;
        for(; right <= nums.length; right++){

            if(right == nums.length){
                max = Math.max(max, right - left);
                continue;
            }

            int num = nums[right];
            map.put(num, map.getOrDefault(num, 0) + 1);

            int fre = map.get(num);

            if(fre <= k) continue;

            max = Math.max(max, right - left);

            while(nums[left] != num){
                map.put(nums[left], map.get(nums[left]) - 1);
                left++;
            }
            left++;
            map.put(num, fre - 1);
        }
        
        return max;
    }
}
```

---

### Complexity

- **Time Complexity:** $\mathcal{O}(N)$
  - Although there is a nested `while` loop, both the `right` pointer and `left` pointer travel from index `0` to $N$ at most once across the entire execution of the algorithm.
  - Each element is added to the hash map once and removed at most once.
  - Assuming standard hash map operations execute in amortized $\mathcal{O}(1)$ time, the total time complexity is strictly linear, $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`.

- **Space Complexity:** $\mathcal{O}(N)$
  - In the worst-case scenario where all elements in `nums` are unique, the `HashMap` will store up to $N$ key-value pairs.
  - Therefore, the auxiliary space complexity is $\mathcal{O}(N)$ (or $\mathcal{O}(U)$, where $U \le N$ is the number of unique elements in `nums`).

---

## 🕵️‍♂️ Follow-up Questions

### 1. How would you optimize the space complexity if constraints specify $nums[i] \le 10^5$?
**Answer:** Instead of using an overhead-heavy object-based `HashMap<Integer, Integer>`, we can replace it with a primitive fixed-size frequency array `int[] count = new int[100001];`. This reduces space overhead from object instantiation, garbage collection, and hashing collisions to a clean, flat $\mathcal{O}(\max(nums[i]))$ auxiliary memory footprint with faster CPU cache locality.

### 2. Can we simplify the sliding window shrinking logic to make the code cleaner without changing time complexity?
**Answer:** Yes. Instead of jumping directly to `nums[left] == num` with explicit assignment `fre - 1`, we can use a standard sliding window contraction pattern:
```java
while (map.get(num) > k) {
    map.put(nums[left], map.get(nums[left]) - 1);
    left++;
}
```
This reduces edge-case checks (like `right == nums.length`) because `max` can be continuously updated at every iteration as `max = Math.max(max, right - left + 1)` after the window is restored to a valid state.