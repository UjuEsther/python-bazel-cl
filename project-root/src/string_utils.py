def reverse_string(s):
    """
    Reverse a string and return it.
    
    Args:
        s: Input string
        
    Returns:
        Reversed string
    """
    return s[::-1]

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    
    Args:
        s: Input string
        
    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Fix the implementation that was incomplete in the homework
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]

def count_vowels(s):
    """
    Count the number of vowels in a string.
    
    Args:
        s: Input string
        
    Returns:
        Number of vowels in the string
    """
    # Fix the implementation that was incomplete in the homework
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)