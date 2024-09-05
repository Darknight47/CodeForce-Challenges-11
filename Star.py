"""
------------------- Link for the challenge: https://codeforces.com/problemset/problem/1950/A -----------------------

You are given three digits a, b, and c. Determine whether they form a stair, a peak, or neither.

A stair satisfies the condition a < b < c.
A peak satisfies the condition a < b > c.
Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases.

The only line of each test case contains three digits a, b, c (0 ≤ a, b, c ≤9).

Output
For each test case, output "STAIR" if the digits form a stair, "PEAK" if the digits form a peak, and "NONE" otherwise (output the strings without quotes).

Implementation:
7
1 2 3
3 2 1
1 5 3
3 4 1
0 0 0
4 1 7
4 5 7

Output:
STAIR
NONE
PEAK
PEAK
NONE
NONE
STAIR
"""
cases = int(input())
for i in range(cases):
    a, b, c = map(int, input().split())
    if(a < b  and b < c):
        print('STAIR')
    elif(a < b and b > c):
        print('PEAK')
    else:
        print('NONE')