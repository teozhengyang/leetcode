# Arrays/Strings

### Prefix/Suffix Sum

- Range sum, difference array, subarray, cumulative pattern, balancing conditions

```
def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix
```

```
# variables
counter = {}
prefix_sum = 0
result = 0

for num in arr:
    prefix_sum += num
    # process result based on condition
    # update counter

```

```
def suffix_sum(arr):
    n = len(arr)
    suffix = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]
    return suffix
```

### Anagram

- Compare strings for rearranged equality using hash map or sorting

```
def is_anagram(s, t):
    if len(s) != len(t): return False
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    for c in t:
        if c not in freq:
			return False
        freq[c] -= 1
        if freq[c] == 0:
            del freq[c]
    return not freq
```

```
# Group anagrams
groups = defaultdict(list)
for word in words:
    key = tuple(sorted(word))
    groups[key].append(word)
```

### Palindrome

- Check symmetry in strings/arrays using two pointers, string reverse, expanding around center

```
# Two pointers
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

```
# Expand around center
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1

def longest_palindrome(s):
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        length = max(len1, len2)
        if length > end - start:
            start = i - (length - 1)//2
            end = i + length//2
    return s[start:end+1]
```

# Hashing

### Hash Map

- Track occurrences (duplicates, majority, matching), map relationships (index, complement, frequency), string/array comparison (e.g. anagram, palindrome, subarray sum)

```
from collections import Counter

# Using Counter
freq = Counter(arr)

# Using dictionary
freq = {}
for num in arr:
	freq[num] = freq.get(num, 0) + 1

# Process
for k, v in freq.items():
    process(k, v)
```

# Patterns
| **Question Mentions...**            | **Think of...**     | **Approach**                   |
| ----------------------------------- | ------------------- | ------------------------------ |
| “Sum of subarray”                   | Prefix / suffix sum | Precompute or prefix-hash      |
| “Count occurrences / duplicates”    | Hash map / set      | Use Counter or dict            |
| “Rearranged / permutation equality” | Anagram             | Frequency map or sorted        |
| “Mirror / symmetric / reverse”      | Palindrome          | Two pointers                   |
| “Find range or prefix condition”    | Prefix/suffix sums  | Running total or map of prefix |
