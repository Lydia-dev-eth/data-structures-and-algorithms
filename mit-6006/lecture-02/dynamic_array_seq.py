"""
MIT 6.006 — Recitation 2: Dynamic Array Sequence
--------------------------------------------------
Extends Array_Seq by over-allocating space so that insert_last and
delete_last become O(1) amortized instead of O(n) every time.

The core idea — table doubling:
  - When the array is FULL:  allocate 2× the current size, copy over.
  - When the array drops to ¼ full: shrink to ½, copy over.

This guarantees that any sequence of n appends costs O(n) total — O(1)
amortized per operation — because expensive copies happen exponentially
rarely (at sizes 1, 2, 4, 8, … so the total copy work is 1+2+4+…+n = 2n).

Complexity summary:
    build(X)              O(n)
    get_at / set_at       O(1)   ← inherited from Array_Seq
    insert_last           O(1)a  ← amortized
    delete_last           O(1)a  ← amortized
    insert_at(i, x)       O(n)   ← still need to shift elements
    delete_at(i)          O(n)
"""

from array_seq import Array_Seq


class Dynamic_Array_Seq(Array_Seq):
    def __init__(self, r=2):  # O(1)
        super().__init__()
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):   return self.size   # O(1)
    def __iter__(self):                     # O(n)
        for i in range(len(self)):
            yield self.A[i]

    def build(self, X):  # O(n)
        for a in X:
            self.insert_last(a)

    # ── internal helpers ─────────────────────────────────────────────────────

    def _compute_bounds(self):  # O(1)
        self.upper = len(self.A)                      # FIX: was self.upper = self.array (set to list object)
        self.lower = len(self.A) // (self.r * self.r) # FIX: was self.r**2 (fine, but consistent with lecture)

    def _resize(self, n):  # O(1) amortized, O(n) worst case
        if self.lower < n < self.upper:
            return                                     # still within bounds — no work needed
        m = max(n, 1) * self.r                        # FIX: was max(0, n) — would allocate 0 slots when n=0
        A = [None] * m
        self._copy_forward(0, self.size, A, 0)        # FIX: was writing back into self.array (wrong target)
        self.A = A
        self._compute_bounds()

    # ── O(1) amortized dynamic operations at the end ─────────────────────────

    def insert_last(self, x):   # O(1)a
        self._resize(self.size + 1)
        self.A[self.size] = x
        self.size += 1

    def delete_last(self):      # O(1)a
        x = self.A[self.size - 1]    # save before nulling
        self.A[self.size - 1] = None
        self.size -= 1
        self._resize(self.size)
        return x

    # ── O(n) dynamic operations at arbitrary index ────────────────────────────

    def insert_at(self, i, x):  # O(n)
        self.insert_last(None)
        self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
        self.A[i] = x

    def delete_at(self, i):     # O(n)
        x = self.A[i]
        self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
        self.delete_last()
        return x

    def insert_first(self, x):  self.insert_at(0, x)        # O(n)
    def delete_first(self):     return self.delete_at(0)     # O(n)
