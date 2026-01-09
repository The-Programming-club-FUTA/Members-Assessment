def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    if n < 2:
        return n

    substr = set()
    l, r = 0, 0   # start both at 0
    max_l = 0

    while r < n:
        if s[r] in substr:
            # shrink window until duplicate is removed
            while s[l] != s[r]:
                substr.remove(s[l])
                l += 1
            substr.remove(s[l])
            l += 1
        else:
            substr.add(s[r])
            r += 1
            max_l = max(max_l, len(substr))

    return max_l