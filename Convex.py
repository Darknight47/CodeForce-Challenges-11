"""

------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1768/A ------------------------

You are given an integer k. Find the largest integer x, where 1 ≤ x < k, such that x!+(x−1)! † is a multiple of ‡ k, or determine that no such x exists.

† y! denotes the factorial of y, which is defined recursively as y!=y⋅(y−1)! for y ≥ 1 with the base case of 0!=1. For example, 5!=5⋅4⋅3⋅2⋅1⋅0!=120.

‡ If a and b are integers, then a is a multiple of b if there exists an integer c such that a=b⋅c. 
For example, 10 is a multiple of 5 but 9 is not a multiple of 6.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The description of test cases follows.

The only line of each test case contains a single integer k (2 ≤ k ≤ 10^9).

Output
For each test case output a single integer — the largest possible integer x that satisfies the conditions above.

If no such x exists, output −1.

Input:
4
3
6
8
10

Output:
2
5
7
9
"""
cases = int(input())
for i in range(cases):
    n = int(input())
    print(n - 1)