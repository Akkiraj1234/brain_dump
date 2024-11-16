# Linked Lists and List Nodes

Linked lists are a fundamental data structure in computer science that are used to store a `sequence of elements.`
each element (node) contains a reference (link) to the next node in the sequence not in contiguous memory locations.

## important

`each node contains:`

1. **Data**: The value the node.

2. **Next Pointer**: A reference of next node

3. *we can modify same list referance will do the work for 203*

`Types of Linked Lists:`

1. **Types of Linked Lists**: Each node points to the next node, lastnode == null

2. **Doubly Linked List**: Each node points to both the next and the previous node, lastnode == previous_node, null

3. **Circular Linked List**: Each node points to the next node, lastnode == 1st node

## Singly Linked Lists

```python
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Creating nodes
node1 = ListNode(10)
node2 = ListNode(20)

# Linking nodes 10 -> 20 -> None
node1.next = node2
```

## methods and uses

1. `inserting at begining` : keep track of head of node and create a new node and insert data in it and insrt head in the .next and return the new node

2. `inserting at the end` : create a new node and then go to the end of the node by using while till head_node.next =None and at that place insert it

3. `insert at a Specific Position` : create a new node add data and then iternate trough node till we reach to postion node and then add postion node.next to new_node.next and at postion node.next add new_node

4. `for delteting` : When you delete a node from a linked list, you need to adjust the pointers correctly to maintain the integrity of the list. Simply setting .next to None doesn't necessarily delete a node; it just breaks the link between nodes and use del to delete at last.

## methods and example

```python
# inserting at begining
def insert_at_beginning(head, data):
    new_node = ListNode(data)
    new_node.next = head
    return new_node

# inserting at the end
def insert_at_end(head, data):
    new_node = ListNode(data)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# insert at a Specific Position
def insert_at_position(head, data, position):
    new_node = ListNode(data)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if not current:
            return head  # Position out of bounds
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return head
```

## Advanced Linked List Concepts

1. `Reverse a Linked List`: Reversing a linked list can be done iteratively or recursively.

    the Iterative Approach is where we iterate over whole linked list and reverse the next of previous and first and return prev and Recursive Approach will check for call itself multiple time and reach the last and then reverse all value

    ```python
    # Iterative Approach:
    def reverse_linked_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    # Recursive Approach:
    def reverse_linked_list_recursive(head):
        if not head or not head.next:
            return head
        reversed_list = reverse_linked_list_recursive(head.next)
        head.next.next = head
        head.next = None
        return reversed_list
    ```

2. `finding the middele of linked list`
    use 2 pointer aproach to figure out the middele

    ```python
    def find_middle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    ```

3. `merging 2 sorted list`
    we use 2 pointer to store the referance of current and then check which 2 of them value is high and something like and add it and increase the pointer where u add and continue doing it and return the new linked list

    ```python
    def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
    ```

4. `Detecting a infininte loop in a Linked List`

    ```python
    def has_cycle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    ```

## Complex Problems and Techniques

1. Flattening a Multilevel Doubly Linked List.
2. Copy List with Random Pointer.
3. Partitioning a Linked List Around a Value.
4. `Use Dummy Nodes`: Simplifies edge cases (e.g., merging lists).
5. `Two Pointer Technique`: Great for cycle detection, finding middle, and more.
6. `Edge Case Handling`: Always consider empty lists, single-node lists, and lists with cycles.
