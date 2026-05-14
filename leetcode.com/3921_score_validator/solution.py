class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            if counter == 10:
                break

            if event == 'W':
                counter += 1
            elif event in ('WD', 'NB'):
                score += 1
            else:
                score += int(event)

        return [score, counter]

