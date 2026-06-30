# Lecture 2 — Sequences: Arrays, Linked Lists, Dynamic Arrays

## What is a Sequence?

A sequence stores items in an order **you control**. The order is extrinsic —
meaning the first item is first not because of what it is, but because you put
it there. Think of it as a ranked list: every item has a position (rank), and
you can insert, delete, or access by that position.

Sequences are a generalization of stacks and queues — those are just sequences
with restricted operations.

---

## The Sequence Interface

Two categories of operations:

**Static** — just reading, no structural changes:
- `build(X)` — create the sequence from an iterable
- `len()` — how many items
- `iter_seq()` — walk through all items in order
- `get_at(i)` — read item at rank i
- `set_at(i, x)` — overwrite item at rank i

**Dynamic** — structural changes:
- `insert_at(i, x)` / `delete_at(i)` — insert or remove at any rank
- `insert_first(x)` / `delete_first()` — at the front
- `insert_last(x)` / `delete_last()` — at the back

Note: any insert or delete shifts the rank of everything after it.

---

## The Three Implementations

### Array Sequence

Uses a contiguous block of memory. Item at rank `i` is literally stored at
memory offset `i`, so the CPU can jump straight to it — O(1) random access.

The cost: inserting or deleting in the middle means physically shifting every
item after it into a new array. That's O(n) every time.

> Lockers in a hallway. Instant to open locker 47. But inserting a new locker
> in the middle means renumbering every locker to its right.

### Linked List Sequence

Each item lives in its own node anywhere in memory. Every node holds the item
and a pointer to the next node. The list only stores a reference to the head.

Adding at the head is O(1) — just rewire one pointer. But reaching rank `i`
means walking `i` steps from the head one by one. No shortcuts. So `get_at`
and `set_at` are O(i), worst case O(n).

> A treasure hunt. Each clue tells you where the next one is. Easy to add a
> new first clue. Impossible to jump directly to clue 40.

### Dynamic Array Sequence

Same as Array Sequence but over-allocates space using **table doubling**:
- When the array fills up → allocate 2× the space, copy everything over
- When it shrinks to ¼ full → shrink to ½, copy over

Resizes are expensive (O(n)) but happen so rarely — at sizes 1, 2, 4, 8, 16…
— that the total cost of n appends is only O(n). Spread across n operations,
that's O(1) per operation on average. This is called **amortized O(1)**.

> A parking lot that doubles in size when full. Most days parking is instant.
> Occasionally you rebuild the lot, but averaged across all days, each car
> still costs constant time.

---

## Complexity Comparison

| Operation | Array | Linked List | Dynamic Array |
|---|---|---|---|
| `build(X)` | O(n) | O(n) | O(n) |
| `get_at / set_at` | **O(1)** | O(i) | **O(1)** |
| `insert/delete first` | O(n) | **O(1)** | O(n) |
| `insert/delete last` | O(n) | O(n) | **O(1) amortized** |
| `insert/delete at(i)` | O(n) | O(i) | O(n) |

No single structure wins everywhere. The right choice depends on which
operations you need to be fast.

---

## Amortized Analysis — the key idea

Amortized means distributing the cost of rare expensive operations across
many cheap ones.

Table doubling works because each time you double, you must have done at
least n/2 cheap inserts since the last resize. So the expensive O(n) copy
gets paid for by the n/2 cheap inserts that came before it — roughly O(2)
cost per insert on average.

If you only added a constant amount of space each time (e.g. +10 slots),
you'd resize constantly and lose the amortized guarantee.

---

## What's coming next

None of these support fast insert/delete at an arbitrary index in sub-linear
time — they're all O(n) or O(i) for that. Lecture 7 introduces trees, which
bring this down to O(log n).
