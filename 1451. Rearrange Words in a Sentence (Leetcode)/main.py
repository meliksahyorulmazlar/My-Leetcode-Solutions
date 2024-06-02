class Solution(object):
    def arrangeWords(self, text):
        lengths = {}
        sizes = []
        words = text.split()
        for word in words:
            length = len(word)
            if length in lengths:
                lengths[length].append(word)
            else:
                lengths[length] = [word]
                sizes.append(length)
        output = []
        sizes.sort()
        for length in sizes:
            length_words = lengths[length]
            for word in length_words:
                output.append(word.lower())
        string = " ".join(output)
        first_char = string[0].upper()
        output = first_char + string[1:]
        return output

