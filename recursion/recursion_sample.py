def print_n_times(x, n):
    if n == 0:
        return
    print(x)
    print_n_times(x, n-1)

if __name__ == "__main__":
    print_n_times(15, 3)