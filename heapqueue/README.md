# Heap & Priority Queue

- Find smallest/largest elements
- Track top K elements
- Merge multiple sorted lists/streams
- Schedule tasks/events by priority/time

```
# Find the k largest elements in a list
heap = []
for num in nums:
    push num into heap
    if heap size > k:
        pop smallest
return heap
```

```
# Heap sort
build a minHeap from all elements
while heap not empty:
    pop element -> append to result
return result
```

```
# Merge k sorted lists
heap = []
for each list:
    push (value, list_index, node) into heap
while heap not empty:
    pop smallest element
    push next element from same list into heap
```

```
# Median from data stream
maxHeap stores smaller half
minHeap stores larger half
rebalance when size difference > 1
median = avg(maxHeap.top, minHeap.top)
```

| **Question Mentions / Keywords**                | **Window Type**      | **Movement Logic**                            | **Example Problem**                           |
| ----------------------------------------------- | -------------------- | --------------------------------------------- | --------------------------------------------- |
| “kth smallest”, “kth largest”, “top k elements” | Fixed-size heap      | Keep heap of size `k`; pop when exceeded      | Kth Largest Element in Array                  |
| “Sort by frequency”, “Reorganize string”        | Frequency-based heap | Push (−freq, element) into heap               | Top K Frequent Elements                       |
| “Merge k sorted lists / arrays”                 | Min-heap             | Always pop smallest current element           | Merge K Sorted Lists                          |
| “Running median”, “median of data stream”       | Dual heap            | Maintain balance between two heaps            | Find Median from Data Stream                  |
| “Task scheduler”, “intervals with priority”     | Min-heap             | Pop earliest finishing / least duration first | Task Scheduler                                |
| “Smallest range covering elements from k lists” | Min-heap             | Pop min, track max, shrink window             | Smallest Range Covering Elements from K Lists |
