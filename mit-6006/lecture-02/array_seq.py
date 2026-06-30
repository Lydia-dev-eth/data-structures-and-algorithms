"""
MIT 6.006 — Recitation 2: Array Sequence
-----------------------------------------
A static array-based sequence. Memory is a contiguous block; index i in the
array maps directly to rank i in the sequence, giving O(1) random access.

The tradeoff: any insert or delete requires allocating a new array and
copying all elements over — O(n) every time.

Complexity summary:
    build(X)          O(n)
    get_at / set_at   O(1)   ← random access is the whole point
    insert_at(i, x)   O(n)   ← must shift everything after i
    delete_at(i)      O(n)   ← same reason
    insert/delete first/last  O(n)  ← these call insert_at / delete_at
"""


class Array_Seq:
    def __init__(self):  # O(1)
        self.A = []
        self.size = 0

    def __len__(self):   return self.size        # O(1)
    def __iter__(self):  yield from self.A       # O(n)

    def build(self, X):  # O(n)
        self.A = [a for a in X]
        self.size = len(self.A)

    def get_at(self, i):       return self.A[i]   # O(1)
    def set_at(self, i, x):    self.A[i] = x      # O(1)

    # ── internal helpers ─────────────────────────────────────────────────────

    def _copy_forward(self, i, n, A, j):   # O(n)
        """Copy n items starting at self.A[i] into A starting at A[j]."""
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i, n, A, j):  # O(n)
        """Same as _copy_forward but iterates in reverse (safe for overlapping)."""
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    # ── dynamic operations ───────────────────────────────────────────────────

    def insert_at(self, i, x):   # O(n)
        n = len(self)
        A = [None] * (n + 1)          # FIX: was [None]*n + 1 (list concat bug)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i):      # O(n)
        n = len(self)
        A = [None] * (n - 1)          # FIX: was [None]*n - 1 (same concat bug)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_first(self, x):  self.insert_at(0, x)           # O(n)
    def delete_first(self):     return self.delete_at(0)        # O(n)
    def insert_last(self, x):   self.insert_at(len(self), x)   # O(n)
    def delete_last(self):      return self.delete_at(len(self) - 1)  # O(n)
