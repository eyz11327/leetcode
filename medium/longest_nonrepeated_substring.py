def lengthOfLongestSubstring(s: str) -> int:
    stored_answers: dict[str, int] = {}
    longest: int = 0
    if len(s) == 1:
        return 1
    
    for index, char in enumerate(s):
        unique = dict()
        unique.update({char: 1})
        potential: str = char
        for sequence_char in s[index+1:]:
            if unique.get(sequence_char, None):
                break
            potential += sequence_char
            unique.update({sequence_char: 1})
        stored_answers.update({potential: len(potential)})
        longest = max(longest, len(potential))

    return longest