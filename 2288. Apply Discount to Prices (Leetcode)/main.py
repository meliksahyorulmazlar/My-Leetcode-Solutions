class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        amount = discount / 100
        words = sentence.split(" ")
        valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(len(words)):
            word = words[i]
            valid_word = True
            if word[0] == "$" and word.count("$") == 1 and len(word) > 1:
                for char in word[1:]:
                    if char not in valid_characters:
                        valid_word = False
                if valid_word:
                    new_word = int(word.replace("$", ""))
                    price = new_word - (new_word * amount)
                    price = f"${price:.2f}"
                    words[i] = price
        sentence = " ".join(words)
        return sentence



print(x)