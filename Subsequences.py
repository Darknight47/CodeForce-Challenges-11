"""

-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1557/A ---------------------------------

Ezzat has an array of n integers (maybe negative). He wants to split it into two non-empty subsequences a and b, 
such that every element from the array belongs to exactly one subsequence, and the value of f(a)+f(b) is the maximum possible value, where f(x) is the average of the subsequence x.

A sequence x is a subsequence of a sequence y if x can be obtained from y by deletion of several (possibly, zero or all) elements.

The average of a subsequence is the sum of the numbers of this subsequence divided by the size of the subsequence.

For example, the average of [1,5,6] is (1+5+6)/3=12/3=4, so f([1,5,6])=4.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^3)— the number of test cases. Each test case consists of two lines.

The first line contains a single integer n (2 ≤ n ≤ 10^5).

The second line contains n integers a1,a2,…,an (−10^9 ≤ a(i) ≤ 10^9).

It is guaranteed that the sum of n over all test cases does not exceed 3⋅10^5.

Output
For each test case, print a single value — the maximum value that Ezzat can achieve.

Your answer is considered correct if its absolute or relative error does not exceed 10^−6.

Formally, let your answer be a, and the jury's answer be b. Your answer is accepted if and only if ( |a−b| / max(1,|b|) ) ≤ 10^−6.

Input:
4
3
3 1 2
3
-7 -6 -6
3
2 2 2
4
17 3 5 -3

Output:
4.500000000
-12.500000000
4.000000000
18.666666667
"""


cases = int(input())
for i in range(cases):
    sze = int(input())
    nums = sorted(list(map(int, input().split())))
    first = 0
    for j in range(sze - 1):
        first += nums[j]
    second = nums[sze - 1]
    ans = second + (first / (sze - 1))
    print(ans)