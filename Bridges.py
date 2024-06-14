"""

------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1944/A -----------------------------------

There are n islands, numbered 1,2,…,n. Initially, every pair of islands is connected by a bridge. Hence, there are a total of n(n−1)/2 bridges.

Everule lives on island 1 and enjoys visiting the other islands using bridges. Dominater has the power to destroy at most k 
bridges to minimize the number of islands that Everule can reach using (possibly multiple) bridges.

Find the minimum number of islands (including island 1) that Everule can visit if Dominater destroys bridges optimally.

Input
Each test contains multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) — the number of test cases. The description of the test cases follows.

The first and only line of each test case contains two integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ n⋅(n−1)/2).

Output
For each test case, output the minimum number of islands that Everule can visit if Dominater destroys bridges optimally.

Input:
6
2 0
2 1
4 1
5 10
5 3
4 4

Output:
2
1
4
1
5
1
"""
cases = int(input())
for i in range(cases):
    n, k = map(int, input().split())
    if(k >= (n - 1)):
        print(1)
    else:
        print(n)