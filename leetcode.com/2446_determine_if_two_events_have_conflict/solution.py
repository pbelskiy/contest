class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        def get_timestamp(time):
            h, m = time.split(':')
            return h*60+m

        a1, a2 = get_timestamp(event1[0]), get_timestamp(event1[1])
        b1, b2 = get_timestamp(event2[0]), get_timestamp(event2[1])

        if a1 <= b1 <= a2 or a1 <= b2 <= a2:
            return True

        if b1 <= a1 <= b2 or b1 <= a2 <= b2:
            return True

        return False
