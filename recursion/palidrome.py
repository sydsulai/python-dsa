def check_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return check_palindrome(s, left+1, right-1)


if __name__ == "__main__":
    s ="nitin"
    a = "anbcodcbna"
    print(check_palindrome(a, 0, len(s)-1))
