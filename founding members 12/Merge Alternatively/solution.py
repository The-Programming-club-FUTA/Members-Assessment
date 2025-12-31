def mergeAlternately(self, word1: str, word2: str) -> str:
    merged = []
    n = len(word1)

    for i in range(n):
        if i < len(word1):
            merged.append(word2[i])
        if i < len(word2):
            merged.append(word2[i])

    return("".join(merged))