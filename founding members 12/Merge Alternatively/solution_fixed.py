def mergeAlternately(self, word1: str, word2: str) -> str:
    merged = []
    n = len(word1) if len(word1) <= len(word2) else len(word2)
    
    for i in range(n):
        merged.append(word1[i])
        merged.append(word2[i])
    # append remaining characters
    if len(word1) > len(word2):
        merged.append(word1[n:])
    if len(word2) > len(word1):
        merged.append(word2[n:])
    
    return ''.join(merged)
print(mergeAlternately(None, word1="abc", word2="pqr"))
print(mergeAlternately(None, word1="ab", word2="pqrs"))
print(mergeAlternately(None, word1="abcd", word2="pq"))