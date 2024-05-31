class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        categories = []
        if length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or (length * width * height) >= 10 ** 9:
            categories.append("Bulky")
        if mass >= 100:
            categories.append("Heavy")

        if len(categories) == 0:
            return "Neither"
        elif len(categories) == 1:
            if categories[0] == "Bulky":
                return "Bulky"
            else:
                return "Heavy"
        else:
            return "Both"
