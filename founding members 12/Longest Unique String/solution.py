def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    if n < 2:
        return n
    substr = set()
    l, r = 0, 1
    max_l = 0

    while r < n:
        if s[r] in substr:
            while s[l] != s[r]:
                l += 1
            substr.remove(s[l])
        else:
            substr.add(s[r])
            r += 1

        max_l = max(max_l, len(substr))

    return max_l