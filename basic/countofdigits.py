import math

class CountOfDigits:
    def count_digits(self, number: int):
        n = number
        count = 0
        while n > 0:
            count += 1
            n = n // 10

        return count
    
    def count_digits_math(self, number: int):
        if number == 0:
            return 1
        return math.floor(math.log10(number)) + 1
    
if __name__ == "__main__":
    count_of_digits = CountOfDigits()
    result = count_of_digits.count_digits(12345)
    print(result)
    result_math = count_of_digits.count_digits_math(12345)
    print(result_math)
