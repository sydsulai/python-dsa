class CheckPalindrome():
    def is_palindrome(self, number: int) -> bool:
        n = number
        new_number = 0
        while n > 0:
            last_digit = n % 10
            new_number = new_number * 10 + last_digit
            n = n // 10
        if new_number != number:
            return False

        return True

if __name__ == "__main__":
    palindrome_checker = CheckPalindrome()
    result = palindrome_checker.is_palindrome(12345)
    print(result)