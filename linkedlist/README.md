# Linked List

- Reordering, merging, reversing, or removing nodes.
- Detecting cycles or intersections.

```
# two pointer
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is now at the middle
```

```
# merge
dummy = new Node(0)
tail = dummy

while l1 != null and l2 != null:
    if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next

# Attach remaining nodes
if l1 != null: tail.next = l1
if l2 != null: tail.next = l2

return dummy.next
```

```
# reverse
prev = null
curr = head

while curr != null:
    nextNode = curr.next
    curr.next = prev
    prev = curr
    curr = nextNode

return prev  # new head
```

```
# add two numbers
carry = 0
dummy = new Node(0)
tail = dummy

while l1 != null or l2 != null or carry:
    x = (l1.val if l1 else 0)
    y = (l2.val if l2 else 0)
    total = x + y + carry
    carry = total // 10

    tail.next = new Node(total % 10)
    tail = tail.next

    if l1 != null: l1 = l1.next
    if l2 != null: l2 = l2.next

return dummy.next
```

| **Question Mentions / Keywords**   | **Type / Technique**        | **Typical Movement Logic**                | **Example Problem**                       |
| ---------------------------------- | --------------------------- | ----------------------------------------- | ----------------------------------------- |
| “reverse”, “invert”, “rotate”      | Pointer manipulation        | Move through nodes, flip `.next` pointers | Reverse Linked List (LC 206)              |
| “merge”, “combine”, “sort list”    | Two-pointer traversal       | Traverse both lists simultaneously        | Merge Two Sorted Lists (LC 21)            |
| “sum”, “add two numbers”           | Parallel traversal          | Move both until null; handle carry        | Add Two Numbers (LC 2)                    |
| “detect cycle”, “loop exists”      | Floyd’s Tortoise-Hare       | Move slow by 1, fast by 2                 | Linked List Cycle (LC 141)                |
| “middle node”, “nth from end”      | Fast & slow pointer         | Fast moves 2×, slow moves 1×              | Middle of Linked List (LC 876)            |
| “palindrome”                       | Split + reverse second half | Compare halves                            | Palindrome Linked List (LC 234)           |
| “intersection”, “merge point”      | Length difference           | Align starts and walk together            | Intersection of Two Linked Lists (LC 160) |
| “reorder”, “swap pairs”, “k-group” | Group manipulation          | Reverse in chunks                         | Reverse Nodes in k-Group (LC 25)          |

# Questions

- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers)
- [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)
- [86. Partition List](https://leetcode.com/problems/partition-list)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii)
- [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list)