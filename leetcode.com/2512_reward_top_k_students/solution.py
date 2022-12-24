class Solution:
    def topStudents(self,
                    positive_feedback: List[str],
                    negative_feedback: List[str],
                    report: List[str],
                    student_id: List[int],
                    k: int
                   ) -> List[int]:

        p = set(positive_feedback)
        n = set(negative_feedback)
        d = {}

        for sid, rep in zip(student_id, report):
            points = 0
            words = Counter(rep.split())

            for w, c in words.items():
                if w in p:
                    points += 3*c
                if w in n:
                    points -= 1*c

            d[sid] = points

        return sorted(student_id, key=lambda sid: (-d[sid], sid))[:k]
