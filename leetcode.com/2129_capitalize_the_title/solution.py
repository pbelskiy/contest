class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join([w.capitalize() if len(w) > 2 else w.lower() for w in title.split(' ')])
