import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("Madam") == True  # Case insensitive
    assert is_palindrome("A man, a plan, a canal: Panama") == True  # Ignoring spaces and punctuation
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True  # Empty string is a palindrome

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5  # Case insensitive
    assert count_vowels("bcdfg") == 0  # No vowels
    assert count_vowels("") == 0  # Empty string