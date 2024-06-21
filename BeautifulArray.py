"""

------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1929/A ------------------------

Sasha decided to give his girlfriend an array a1,a2,…,an. He found out that his girlfriend evaluates the beauty of the array as the sum of the values (ai−ai−1) for all integers i from 2 to n.

Help Sasha and tell him the maximum beauty of the array a that he can obtain, if he can rearrange its elements in any way.

Input
Each test consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 500) — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer n (2 ≤ n ≤ 100) — the length of the array a.

The second line of each test case contains n integers a1,a2,…,an (1 ≤ a(i) ≤ 10^9) — the elements of the array a.

Output
For each test case, output a single integer — the maximum beauty of the array a that can be obtained.


Input:
5
3
2 1 3
3
69 69 69
5
100 54 80 43 90
4
3 4 3 3
2
2 1

Output:
2
0
57
1
1
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    lst = sorted(list(map(int, input().split())))
    print(lst[sze - 1] - lst[0])