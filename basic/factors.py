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

    def get_factors_optimal(self, num: int):
        result = []
        for i in range(1, int(math.sqrt(num))+1): # TC => O(sqrt(N))
            if num % i == 0:
                result.append(i)
                if num // i != i :
                    result.append(num//i)
        return sorted(result) # TC => O(N Log N)
    
if __name__ == "__main__":
    factorsordivisors = FactorsOrDivisors()
    print(factorsordivisors.get_factors(10))
    print(factorsordivisors.get_factors_optimal(15))
    print(factorsordivisors.get_factors_optimal(25))
    print(factorsordivisors.get_factors(7))
    print(factorsordivisors.get_factors(19))