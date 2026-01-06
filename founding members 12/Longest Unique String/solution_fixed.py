# Thought Process: This problem is a sliding window one with auxiliary data structure (familiar with dictionaries though
# but will have to work with set since that's what the solution used)

# First fix: redundant self parameter, should be used with classes

# Second fix: right pointer set to 1, should be set to 0 instead (both l and r should start out at the same index)

# Third fix: compare indexes not strings in while loop (while l != r)

# Fourth fix: we want to move the left index to the character just after the earliest occurrence of the duplicate character
# (which is what the if guard in the nested while loop does)

# Fifth fix: move line (substr.remove(s[l])) into nested while loop (to delete characters outside the window frame)

# Sixth fix: Added documentation

# Seventh fix: Improper naming convention for a function (NOT REALLY AN ISSUE)


def length_of_longest_substring(s: str) -> int:
    """
    function to find length of longest unique substring in a parent string

    :param s: input string

    :return: length of substring
    """

    n = len(s)

    if n < 2:
        return n

    substr = set()

    l, r = 0, 0
    max_l = 0

    while r < n:
        if s[r] in substr:
            track_left = s.index(s[r], l)

            while l != r:
                if l > s.index(s[r], track_left):
                    break

                substr.remove(s[l])
                l += 1

        else:
            substr.add(s[r])
            r += 1

        max_l = max(max_l, len(substr))

    return max_l

# This solves the problem without changing too much of the original code logic
