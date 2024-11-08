class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        numbers = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                   9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                   16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
                   40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'Hundred',
                   1000: 'Thousand', 1000000: 'Million', 1000000: 'Billion'}
        results = []
        n = num
        if n >= 1000000000:
            count = n // 1000000000
            r = self.numberToWords(count)
            output = f"{r} Billion"
            results.append(output)
            n = n%1000000000

        if n >= 1000000:
            count = n // 1000000
            r = self.numberToWords(count)
            output = f"{r} Million"
            results.append(output)
            n = n % 1000000

        if n >= 1000:
            count = n // 1000
            r = self.numberToWords(count)
            output = f"{r} Thousand"
            results.append(output)
            n = n % 1000

        if n >= 100:
            count = n // 100
            r = self.numberToWords(count)
            output = f"{r} Hundred"
            results.append(output)
            n = n % 100

        if n >= 21:
            count = (n//10)*10
            if n-count != 0:
                r = self.numberToWords(n-count)
                output = f"{numbers[count]}"
                n = n % 10
            else:
                output = f"{numbers[count]}"
                n = 0
            results.append(output)


        if n in numbers:
            results.append(numbers[n])
            n = 0


        if n >0:
            output = f'{numbers[n]}'
            results.append(output)

        return " ".join(results)