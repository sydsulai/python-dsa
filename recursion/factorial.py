def get_factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * get_factorial(n-1)

if __name__ == "__main__":
    print(get_factorial(5))