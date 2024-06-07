class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        output = []
        for word in words:
             results = word.split(separator)
             for result in results:
                 if result != '':
                     output.append(result)
        return output


