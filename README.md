# python-dsa
This repository contains the python-dsa and system designing. Started on 2026.

# Notes
Basic Python Operations and Time Complexity: [https://wiki.python.org/moin/TimeComplexity](https://wiki.python.org/moin/TimeComplexity)

1. If your iteration is based on fixed number like (n//10), then time complexity = O(log10(N)) [While Loop]

1. Slicing works first at row level, You cannot take first column in all rows like below
a[i+1:9][0], It needs to be done like [a[row][j] for row in range(1, 9)]