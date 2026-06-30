Lecture 2 — Sequences: Arrays, Linked Lists, Dynamic Arrays


What this covers

Three ways to implement the Sequence interface — the abstract idea of a
ranked, ordered collection — and the tradeoffs each one makes between
speed of access and speed of modification.


Note: this lecture also introduces the Set interface as a contrast.
Sets are ordered by what the item is (its key). Sequences are ordered
by where you put it (its rank). They are different interfaces —
the three data structures here all implement Sequence, not Set.



Files

FileWhat it isarray_seq.pyArray Sequence implementationlinked_list_seq.pyLinked List Node + Sequence implementationdynamic_array_seq.pyDynamic Array Sequence (table doubling)notes.mdFull notes: concepts, mental models, complexity table, amortized analysisREADME.mdThis file

The one-line summary per structure


Array Sequence — O(1) random access, O(n) insert/delete everywhere
Linked List Sequence — O(1) insert/delete at the head, O(n) to reach anything else
Dynamic Array Sequence — O(1) random access + O(1) amortized append/pop, O(n) insert/delete in the middle


