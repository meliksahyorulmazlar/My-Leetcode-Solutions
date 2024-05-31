class Solution:
    def capitalizeTitle(self, title: str):
        output = []
        words = title.split()

        for i in range(len(words)):
            string = words[i]
            if len(string) <3:
                output.append(string.lower())
            else:
                output.append(string.title())
        return " ".join(output)

