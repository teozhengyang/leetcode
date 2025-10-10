# Sliding Windows

- Find subarray/substring that satisfies a condition (e.g. contains all chars, no duplicates, max sum)
- Involve 'longest', 'shortest', 'count', 'exactly k', 'at most k', 'at least k'
- Use a dynamic range/window that expands/contracts without restarting
- Often combined with hash map/set to track counts/frequencies

```
# Variable Size Window
left = 0
for right in range(len(arr)):
    # expand window by including arr[right]

    while condition_violated():
        # shrink window from left
        left += 1

    # update result if valid
    result = max(result, right - left + 1)
```

```
# Fixed Size Window
window_sum = sum(arr[:k])
max_sum = window_sum

for right in range(k, len(arr)):
    window_sum += arr[right] - arr[right - k]
    max_sum = max(max_sum, window_sum)
```

```
# initialise map/list to track window elements
# initialise left pointer
# initialise result

# loop through right pointer
    # update map/list with arr[right]
    # while window is invalid
        # update map/list by removing arr[left]
        # move left pointer
```

| **Question Mentions / Keywords**      | **Window Type** | **Movement Logic**                            | **Example Problem**                            |
| ------------------------------------- | --------------- | --------------------------------------------- | ---------------------------------------------- |
| “subarray/substring” + “longest”      | Variable-length | Expand right, shrink left when invalid        | Longest Substring Without Repeating Characters |
| “subarray of size k” / “exactly k”    | Fixed-length    | Move both left/right together by 1            | Max Sum Subarray of Size K                     |
| “at most k distinct elements”         | Variable-length | Expand until > k, shrink until valid          | Fruits Into Baskets                            |
| “sum ≤ target”                        | Variable-length | Shrink when sum > target                      | Minimum Size Subarray Sum                      |
| “average of every k elements”         | Fixed-length    | Maintain rolling sum                          | Sliding Window Average                         |
| “contains all chars of X” / “anagram” | Variable-length | Expand until valid, shrink to minimize        | Minimum Window Substring / Find All Anagrams   |
| “max/min in window”                   | Fixed-length    | Use deque for fast min/max                    | Sliding Window Maximum                         |
| “count subarrays that…”               | Variable-length | Expand and count windows satisfying condition | Subarrays with K Different Integers            |

# Questions

- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
- [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)
- [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)