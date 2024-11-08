class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        n = num
        if n >= 1000:
            count = n // 1000
            result += ("M" * count)
            n = (n % 1000)

        if n >= 900:
            result += ("CM")
            n = (n % 900)

        if n >= 500:
            result += ("D")
            n = (n % 500)

        if n >= 400:
            result += ("CD")
            n = (n % 400)

        if n >= 100:
            count = n // 100
            result += ("C" * count)
            n = (n % 100)

        if n >= 90:
            result += ("XC")
            n = (n % 90)

        if n >= 50:
            count = n // 50
            result += ("L")
            n = (n % 50)

        if n >= 40:
            result += ("XL")
            n = (n % 40)

        if n >= 10:
            count = n // 10
            result += ("X" * count)
            n = (n % 10)

        if n == 9:
            result += ("IX")
            n = 0

        if n >= 5:
            result += ("V")
            n = (n % 5)

        if n == 4:
            result += ("IV")
            n = 0

        if n >= 1:
            result += ("I" * n)
            n = (n % 1)

        return result


