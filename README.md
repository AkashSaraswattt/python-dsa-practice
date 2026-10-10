# Python DSA Practice

A small, dependency-free Python interview practice project.

## Requirements and tests

Python 3.9 or newer. From the repository root:

```bash
python -m unittest -v
```

## Problems

| Function | Approach | Time | Extra space |
| --- | --- | --- | --- |
| `word_pattern(pattern, sentence)` | Two dictionaries enforce a character-to-word bijection | O(p + s) | O(p + s) |
| `final_value_after_operations(operations)` | Sum the change for each valid operation | O(n) | O(1) |

Here, p is the pattern length, s is the sentence length, and n is the operation count. Word splitting stores the sentence words; dictionary keys and values reference those words.

### Word pattern

```python
from solutions import word_pattern

print(word_pattern("abba", "dog cat cat dog"))  # True
print(word_pattern("ab", "dog dog"))            # False
```

Every character must map to exactly one word, and every word to exactly one character. The implementation accepts whitespace-separated words, including repeated spaces and tabs. Empty pattern plus empty sentence returns `True`.

### Final value after operations

```python
from solutions import final_value_after_operations

print(final_value_after_operations(["--X", "X++", "X++"]))  # 1
```

The variable starts at zero. `++X` and `X++` increment it; `--X` and `X--` decrement it. Operations are case-sensitive; invalid values raise `ValueError`.

## Test coverage

Includes valid mappings, conflicts in both mapping directions, unequal lengths, empty inputs, repeated words, whitespace handling, all four operations, cancellation, negative results, and invalid operations.
