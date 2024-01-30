def is_palindrome(s: str) -> bool:
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
