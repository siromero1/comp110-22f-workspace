def vowels_and_threes(words: str) -> str:
    """Finding vowels in a list or at an index of 3s."""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    result: str = ""
    is_vowel: bool = False
    i: int = 0
    idx: int = 0
    while i < len(words):
        is_vowel = False
        idx = 0
        while idx < len(vowels):
            if vowels[idx] == words[i]:
                is_vowel = True
            idx += 1
        if i % 3 == 0 and is_vowel:
            result += ""
        elif i % 3 == 0:
            result += words[i]
        elif is_vowel:
            result += words[i]
        i += 1
    return result