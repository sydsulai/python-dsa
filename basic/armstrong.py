# github:copilot:disable

import math

class ArmstrongNumber:
    def is_armstrong(self, number: int) -> bool:
        n = number
        count_n = math.floor(math.log10(n)) + 1
        res_sum = 0
        while n > 0:
            res_sum += pow(n % 10, count_n)
            n = n // 10
        if res_sum == number:
            return True
        return False
    
if __name__ == "__main__":
    armstrong_checker = ArmstrongNumber()
    print(armstrong_checker.is_armstrong(153))  # True
    print(armstrong_checker.is_armstrong(9474)) # True
    print(armstrong_checker.is_armstrong(123))  # False
    print(armstrong_checker.is_armstrong(370))  # True