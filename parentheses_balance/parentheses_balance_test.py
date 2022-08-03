# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from unittest import TestCase
from parentheses_balance import parentheses_balance


class TestParenthesesBalance(TestCase):

    def test_simples_incorrect(self):
        line = "("
        expected = "incorrect"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_simples_correct(self):
        line = "()"
        expected = "correct"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_first_example(self):
        line = "a+(b*c)-2-a"
        expected = "correct"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_second_example(self):
        line = "(a+b*(2-c)-2+a)*2"
        expected = "correct"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_third_example(self):
        line = "(a*b-(2+c)"
        expected = "incorrect"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_fourth_example(self):
        line = "2*(3-a))"
        expected = "incorrect"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)

    def test_fifth_example(self):
        line = ")3+b*(2-c)("
        expected = "incorrect"

        actual = parentheses_balance(line)

        self.assertEqual(expected, actual)
