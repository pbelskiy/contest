class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        category = []

        if length >= 10**4 or width >= 10**4 or height >= 10**4 or volume >= 10**9:
            category.append("Bulky")

        if mass >= 100:
            category.append("Heavy")

        if "Bulky" in category and "Heavy" in category:
            return "Both"

        if not category:
            return "Neither"

        return category[0]
