from leetcode.palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome("lagerregal") == True
    assert is_palindrome("lagerregala") == False
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("lagerrega l") == False
    assert is_palindrome("lagerRegal") == True
