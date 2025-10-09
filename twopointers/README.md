# Two Pointers

- Search/compare/partition elements in sorted array/linked list
- Traverse from both ends toward the center (e.g. palindrome, sum to target)
- Scan a range/window dynamically without restarting (e.g. sliding window)
- Remove/deduplicate/rearrange in-place without extra space

```
# Opposite ends (Palindrome/Two Sum)
left, right = 0, len(arr) - 1
while left < right:
    if condition(arr[left], arr[right]):
        # do something
        left += 1
        right -= 1
    elif too_small_condition:
        left += 1
    else:
        right -= 1
```

```
# Fast & Slow (Linked List/Cycle)
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle detected
return False
```

```
# In-place filtering (Remove Duplicates/Move Zeroes)
slow = 0
for fast in range(len(nums)):
    if keep(nums[fast]):         # e.g., nums[fast] != 0
        nums[slow] = nums[fast]
        slow += 1
return slow  # new length or count of valid elements
```

```
# Sliding window (Substring/Min Window)
left = 0
for right in range(len(nums)):
    # expand the window
    while condition_not_satisfied():
        # shrink from left
        left += 1
    # record answer based on [left, right] window
```

| **Question Mentions / Looks Like...**                               | **Pointer Pattern to Use**                 | **Typical Movement / Logic**                                                  | **Common Examples**                                         |
| ------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| “Find pair / triplet that sums to target”<br>“Array is sorted”      | **Opposite Ends**                          | Start at both ends, move `left` or `right` inward depending on sum comparison | Two Sum II, 3Sum, Container With Most Water                 |
| “Check if string / array is palindrome / symmetric”                 | **Opposite Ends**                          | Compare `s[left]` and `s[right]`, move inward                                 | Valid Palindrome, Reverse String                            |
| “Detect cycle / find middle / nth from end”                         | **Fast & Slow Pointers**                   | `fast` moves 2×, `slow` moves 1×                                              | Linked List Cycle, Middle of Linked List, Remove Nth Node   |
| “Remove duplicates / move zeroes / partition array”                 | **In-Place Filtering (Slow–Fast)**         | `fast` scans input; `slow` writes valid values                                | Remove Duplicates, Move Zeroes, Sort Colors                 |
| “Find longest / shortest subarray / substring satisfying condition” | **Sliding Window**                         | Expand `right`, shrink `left` while invalid                                   | Longest Substring Without Repeats, Minimum Window Substring |
| “Merge sorted arrays / lists / intervals”                           | **Merge Pattern**                          | Traverse both lists with pointers, append smaller                             | Merge Two Sorted Lists, Merge Intervals                     |
| “Partition by condition (odd/even, color, sign)”                    | **Opposite Ends or Slow–Fast Variant**     | Move pointers until misaligned values found, then swap                        | Dutch National Flag, Sort Array by Parity                   |
| “Find kth element / median of sorted arrays”                        | **Binary Partition (Two-pointer variant)** | Move boundaries toward median using conditions                                | Median of Two Sorted Arrays                                 |
