class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        if limit <= 5:
            return []

        length = 5  # <1/9>
        cap = 9

        # calc start cap
        while True:
            chunks = len(message) / (limit - length)
            if chunks < cap:
                break
            cap = int(str(cap) + '9')

        # count total chunks
        j = 0
        total = 0

        while j < len(message):
            curr_chunk_len = limit - (1 + len(str(total + 1)) + 1 + len(str(cap)) + 1)
            j += curr_chunk_len
            total += 1
            if curr_chunk_len <= 0:
                return []

        # format chunks
        i = 1
        j = 0
        arr = []

        while j < len(message):
            curr_chunk_len = limit - (1 + len(str(i)) + 1 + len(str(cap)) + 1)
            arr.append('{}<{}/{}>'.format(message[j:j+curr_chunk_len], i, total))
            j += curr_chunk_len
            i += 1

        return arr
