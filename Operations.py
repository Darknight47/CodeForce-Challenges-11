"""
--------------------- Link for the challenge: https://codeforces.com/problemset/problem/2020/A ----------------------------

You are given two integers n and k.

In one operation, you can subtract any power of k from n. Formally, in one operation, you can replace n by (n−k^x) for any non-negative integer x.

Find the minimum number of operations required to make n equal to 0.

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). The description of the test cases follows.

The only line of each test case contains two integers n and k (1 ≤ n,k ≤ 10^9).

Output
For each test case, output the minimum number of operations on a new line.

Input:
6
5 2
3 5
16 4
100 3
6492 10
10 1

Output:
2
3
1
4
21
10
"""
cases = int(input())
for i in range(cases):
    n, k = map(int, input().split())
    steps = 0
    if(k > 1):
        while n > 0:
            steps += n % k
            n //= k 
        print(steps)
    else:
        print(n)