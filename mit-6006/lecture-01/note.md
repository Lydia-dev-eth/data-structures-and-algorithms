# Lecture 1 — Introduction (short note)

 
## Main concepts
- **Problem vs Algorithm**
  - A *problem* defines the relation from inputs to correct outputs (via a verifiable predicate).
  - An *algorithm* is a deterministic procedure mapping each input to a single output; it *solves* the problem if it returns a correct output for every input.

- **Correctness**
  - Programs are finite; to prove correctness for arbitrarily large inputs use **induction** or loop/recurrence invariants.
  - Example proof technique: induct on the number of processed items (k) to show the algorithm maintains the invariant.

- **Efficiency**
  - Count fixed‑time operations to get machine‑independent runtime estimates.
  - Use asymptotic notation (O, Θ, Ω). Efficient usually means polynomial time; exponential time is often infeasible.

- **Model of computation (Word‑RAM)**
  - Memory is an addressable sequence of machine words (word size = w bits).
  - To address n words need \(w \ge \log_2 n\). Example limits: 32‑bit ≈ 4 GB, 64‑bit ≈ 16 EB.
  - A stored word can hold the address (pointer) of a larger object.

- **Data structures**
  - Different data structures implement the same interface with different performance (e.g., StaticArray: `get_at`/`set_at` O(1); allocation O(n)).

## Example: Birthday matching
- **Problem:** Given a list of students `(name, bday)`, find any pair sharing the same birthday or return `None`.
- **Naïve algorithm (lecture):**
  - For each student k, compare their birthday with all previous k students.
  - **Time complexity:**`sum_{k=0}^{n-1} k = n*(n-1)/2 = (n^2 - n)/2`.

 

## Proof sketch (correctness of the lecture's algorithm)
- Induct on k = number of students already in the record.
- Base k = 0: record empty, invariant holds.
- Inductive step: assume invariant for k; when adding student k+1, algorithm checks whether their birthday matches any in first k; if so, returns a correct pair; otherwise invariant holds for k+1.
