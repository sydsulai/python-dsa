import math

class FactorsOrDivisors:
    def get_factors(self, num: int):
        n = num
        result = []
        for i in range(1, n//2):
            if num % i == 0:
                result.append(i)
        result.append(num)
        return result
    
if __name__ == "__main__":
    factorsordivisors = FactorsOrDivisors()
    print(factorsordivisors.get_factors(10))
    print(factorsordivisors.get_factors(15))
    print(factorsordivisors.get_factors(25))
    print(factorsordivisors.get_factors(7))
    print(factorsordivisors.get_factors(19))