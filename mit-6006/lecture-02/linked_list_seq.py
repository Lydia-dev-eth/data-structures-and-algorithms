"""
MIT 6.006 — Recitation 2: Linked List Sequence
------------------------------------------------
Each item lives in its own node anywhere in memory. Nodes are chained
together by a .next pointer. The list only holds a reference to the head.

Key insight: adding/removing at the HEAD is O(1) because you only rewire
one pointer. But reaching item i requires walking i steps — there's no
shortcut — so get_at and set_at are O(i), worst case O(n).

Complexity summary:
    build(X)              O(n)
    get_at / set_at       O(i)   ← must walk from head each time
    insert_first          O(1)   ← just rewire the head pointer
    delete_first          O(1)
    insert_at(i, x)       O(i)   ← walk to position i-1, then rewire
    delete_at(i)          O(i)
    insert/delete last    O(n)   ← last = worst case for walking
"""


class Linked_List_Node:
    def __init__(self, x):   # O(1)
        self.item = x
        self.next = None

    def later_node(self, i):  # O(i)
        """Return the node i steps ahead of this one."""
        if i == 0:
            return self
        assert self.next, "index out of range"
        return self.next.later_node(i - 1)


class Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):   return self.size  # O(1)

    def __iter__(self):  # O(n)
        node = self.head
        while node:
            yield node.item          # FIX: was yielding the node itself, not node.item
            node = node.next

    def build(self, X):  # O(n)
        for a in reversed(X):
            self.insert_first(a)     # FIX: was calling self.set_first (wrong name)

    def get_at(self, i):  # O(i)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):  # O(i)
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):  # O(1)
        new_node = Linked_List_Node(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):  # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):  # O(i)
        if i == 0:
            self.insert_first(x)
            return
        new_node = Linked_List_Node(x)
        node = self.head.later_node(i - 1)
        new_node.next = node.next    # FIX: was node.next = new_node.next (pointer set in wrong order)
        node.next = new_node         # FIX: was node.next = new_node.next (skipped the new node entirely)
        self.size += 1

    def delete_at(self, i):  # O(i)
        if i == 0:                   # FIX: was checking i==1 (off-by-one, should be 0)
            return self.delete_first()
        node = self.head.later_node(i - 1)
        x = node.next.item           # FIX: was x = node.next (stored node, not item)
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):   self.insert_at(len(self), x)        # O(n)
    def delete_last(self):      return self.delete_at(len(self) - 1) # O(n)
