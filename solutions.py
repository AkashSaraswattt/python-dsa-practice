"""Small Python solutions for common interview problems."""


def word_pattern(pattern: str, sentence: str) -> bool:
    """Check a bijection between pattern characters and whitespace-separated words."""
    words = sentence.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}
    for char, word in zip(pattern, words):
        if char in char_to_word and char_to_word[char] != word:
            return False
        if word in word_to_char and word_to_char[word] != char:
            return False
        char_to_word[char] = word
        word_to_char[word] = char
    return True


def final_value_after_operations(operations: list[str]) -> int:
    """Start at zero; reject operations outside the four supported forms."""
    changes = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
    value = 0
    for operation in operations:
        if operation not in changes:
            raise ValueError(f"Unsupported operation: {operation!r}")
        value += changes[operation]
    return value
