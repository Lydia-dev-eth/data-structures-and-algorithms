from typing import List, Tuple, Optional

Student = Tuple[str, object]  # (name, bday)

def birthday_match(students: List[Student]) -> Optional[Tuple[str, str]]:
    """
    Naive duplicate detection (lecture example).
    Time complexity: O(n^2) worst-case (quadratic)
    """
    n = len(students)              # O(1)
    record = [None] * n            # O(n) allocation
    for k in range(n):             # n iterations
        name1, bday1 = students[k] # O(1)
        for i in range(k):         # up to k iterations
            name2, bday2 = record[i]  # O(1)
            if bday1 == bday2:
                return (name1, name2)
        record[k] = (name1, bday1) # O(1)
    return None
