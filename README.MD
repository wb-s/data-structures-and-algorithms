# Data Structures and Algorithms

Balanced Binary Search Tree:

- Module: balanced_bst.py
- Tests: test_balanced_bst.py

Binary Search Tree:

- Module: bst.py
- Tests: test_bst.py

Binary Heap:

- Module: binheap.py
- Tests: test_binheap.py

Linked List:

- Module: linked_list.py
- Tests: test_linked_list.py

Double Linked List:

- Module: dbl_linked_list.py
- Tests: test_dbl_linked_list.py

Deque:

- Module: deque.py
- Tests: test_deque.py

Graph:

- Module: graph.py
- Tests: test_graph.py

Insertion Sort:

- Module: insertion_sort.py
- Tests: test_insertion_sort.py

Merge Sort:

- Module: merge_sort.py
- Tests: merge_sort.py

Priority Queue:

- Module: priorityq.py
- Tests: test_priorityq.py

Queue:

- Module: queue_ds.py
- Tests: test_queue.py

Quick Sort:

- Module: quick_sort.py
- Tests: test_quick_sort.py

Stack:

- Module: stack.py
- Tests: test_stack.py

Trie:

- Module: trie.py
- Tests: test_trie.py

Weighted Graph:
- Module: weighted_graph.py
- Tests: test_weighted_graph.py

# Testing and Coverage
```
========================================================================================= test session starts =========================================================================================
platform darwin -- Python 3.10.2, pytest-7.1.2, pluggy-1.0.0
rootdir: /Users/williamshields/data-structures-and-algorithms
plugins: cov-3.0.0
collected 349 items                                                                                                                                                                                   

src/test_balanced_bst.py ..............................................                                                                                                                         [ 13%]
src/test_bst.py ...................................                                                                                                                                             [ 23%]
src/test_dbl_linked_list.py ..............................                                                                                                                                      [ 31%]
src/test_deque.py .....................                                                                                                                                                         [ 37%]
src/test_graph.py ............................                                                                                                                                                  [ 45%]
src/test_insertion_sort.py ...........................                                                                                                                                          [ 53%]
src/test_linked_list.py ...............                                                                                                                                                         [ 57%]
src/test_merge_sort.py ............................                                                                                                                                             [ 65%]
src/test_priorityq.py ..............                                                                                                                                                            [ 69%]
src/test_queue.py ..............                                                                                                                                                                [ 73%]
src/test_quick_sort.py ............................                                                                                                                                             [ 81%]
src/test_stack.py .........                                                                                                                                                                     [ 84%]
src/test_trie.py ...........                                                                                                                                                                    [ 87%]
src/test_weighted_graph.py ...........................................                                                                                                                          [100%]

---------- coverage: platform darwin, python 3.10.2-final-0 ----------
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
src/balanced_bst.py             410    186    55%   41-42, 50, 54-56, 60-72, 81, 98-100, 108, 112-122, 126, 130-139, 143, 147-161, 165, 169-177, 208, 217, 219-250, 268-269, 277-306, 314-343, 350-358, 362-371, 449-453, 481-485
src/bst.py                      243     24    90%   40-41, 72, 94, 125, 187, 191-199, 250, 280-285, 314, 322
src/dbl_linked_list.py           80      0   100%
src/deque.py                     32      0   100%
src/graph.py                     95      9    91%   48, 97, 110, 140, 144, 150-153
src/hash_table.py                51     39    24%   26-28, 32-36, 40-46, 50-53, 56, 59-67, 89-113
src/insertion_sort.py            34     16    53%   26-47
src/linked_list.py               67     15    78%   8-11, 34, 66-74, 93, 97
src/merge_sort.py                45     16    64%   46-67
src/priorityq.py                 42      0   100%
src/queue_ds.py                  23      0   100%
src/quick_sort.py                39     16    59%   33-54
src/stack.py                      8      0   100%
src/test_balanced_bst.py        686      0   100%
src/test_binheap.py               0      0   100%
src/test_bst.py                 384      0   100%
src/test_dbl_linked_list.py     133      0   100%
src/test_deque.py                88      0   100%
src/test_graph.py               178      0   100%
src/test_hash_table.py            2      0   100%
src/test_insertion_sort.py       43      0   100%
src/test_linked_list.py          78      0   100%
src/test_merge_sort.py           51      0   100%
src/test_priorityq.py            77     11    86%   66-70, 96-101
src/test_queue.py                79      0   100%
src/test_quick_sort.py           51      0   100%
src/test_stack.py                50      0   100%
src/test_trie.py                 52      8    85%   33-36, 42-45
src/test_weighted_graph.py      196     54    72%   23-24, 29-33, 38-45, 50-56, 61-67, 72-78, 83-89, 94-100, 104-108
src/trie.py                      68      6    91%   79, 85-86, 88-90
src/weighted_graph.py           125     52    58%   32, 49, 51, 53, 59-65, 69-72, 76-78, 82-85, 89-97, 101-110, 114-129, 186
-----------------------------------------------------------
TOTAL                          3510    452    87%


========================================================================================= 349 passed in 0.34s =========================================================================================

```
