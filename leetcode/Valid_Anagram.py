class Solution:
    def isAnagram(s: str, t: str) -> bool:
        from collections import Counter

        print(sorted(s))
        print(sorted(t))

        for word in s:
            if word in t:
                t = t.replace(word, "", 1)
            else:
                return False

        if len(t) == 0:
            return True

    print(isAnagram("anagram", "nagaram"))
    print(isAnagram("rat", "car"))