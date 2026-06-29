 # Lecture 1 — Introduction to Algorithms 

This folder contains a concise note and example code derived directly from the Lecture 1 PDF for MIT 6.006 (Introduction to Algorithms).

## Contents
- `lec1_note.md` — short lecture note (main concepts, correctness sketch, and complexity for the example).
- `birthday_match.py` — two implementations of the birthday-matching example: naive (O(n²)) and hash-based (O(n) expected).
 
## Key takeaways (brief)
- **Problem vs Algorithm:** problems map inputs to correct outputs; algorithms are deterministic procedures that must be correct for all inputs.  
- **Correctness:** prove using induction or loop invariants for arbitrarily large inputs.  
- **Efficiency:** count fixed-time operations; use asymptotic notation (Big‑O).  
- **Model:** Word‑RAM — memory is an addressable sequence of machine words; word size must satisfy \(w \ge \log_2 n\).  
- **Example:** Naïve birthday matching is **O(n²)** 

