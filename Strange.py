"""

--------------------- Link for the challenge: https://codeforces.com/problemset/problem/1455/A ----------------------

Let's define a function f(x) (x is a positive integer) as follows: write all digits of the decimal representation of x 
backwards, then get rid of the leading zeroes. For example, f(321)=123, f(120)=21, f(1000000)=1, f(111)=111.

Let's define another function g(x)= x f(f(x)) (x is a positive integer as well).

Your task is the following: for the given positive integer n, calculate the number of different values of g(x) among all numbers x such that 1 ≤ x ≤ n.

Input
The first line contains one integer t (1 ≤ t ≤ 100) — the number of test cases.

Each test case consists of one line containing one integer n (1 ≤ n < 10^100). This integer is given without leading zeroes.

Output
For each test case, print one integer — the number of different values of the function g(x), if x can be any integer from [1,n]

Input:
5
4
37
998244353
1000000007
12345678901337426966631415

Output:
1
2
9
10
26
"""
cases = int(input())
for i in range(cases):
    s = input()
    print(len(s))