import unittest

from solutions import final_value_after_operations, word_pattern


class WordPatternTests(unittest.TestCase):
    def test_bijection_and_edge_cases(self):
        cases = [
            ("abba", "dog cat cat dog", True),
            ("abba", "dog cat cat fish", False),
            ("ab", "dog dog", False),
            ("aaaa", "dog cat cat dog", False),
            ("ab", "dog", False),
            ("a", "dog cat", False),
            ("", "", True),
            ("a", "", False),
            ("", "dog", False),
            ("aaa", "dog dog dog", True),
            ("abba", "  dog  cat\tcat dog  ", True),
        ]
        for pattern, sentence, expected in cases:
            with self.subTest(pattern=pattern, sentence=sentence):
                self.assertEqual(word_pattern(pattern, sentence), expected)


class FinalValueTests(unittest.TestCase):
    def test_supported_operations(self):
        cases = [
            ([], 0),
            (["--X", "X++", "X++"], 1),
            (["++X", "X++"], 2),
            (["--X", "X--"], -2),
            (["++X", "X++", "--X", "X--"], 0),
        ]
        for operations, expected in cases:
            with self.subTest(operations=operations):
                self.assertEqual(final_value_after_operations(operations), expected)

    def test_invalid_operations_raise(self):
        for operation in ["++x", "X", "X+X", "", " X++"]:
            with self.subTest(operation=operation):
                with self.assertRaises(ValueError):
                    final_value_after_operations([operation])


if __name__ == "__main__":
    unittest.main()
