"""

-------------------------- Link for the challenge: https://codeforces.com/contest/1741/problem/B -----------------------------

A sequence of n numbers is called permutation if it contains all numbers from 1 to n exactly once. 
For example, the sequences [3,1,4,2], [1] and [2,1] are permutations, but [1,2,1], [0,1] and [1,3,4] are not.

For a given number n you need to make a permutation p such that two requirements are satisfied at the same time:

For each element p(i), at least one of its neighbors has a value that differs from the value of p(i)
by one. That is, for each element p(i) (1 ≤ i ≤ n), at least one of its neighboring elements (standing to the left or right of pi) must be pi+1, or pi−1.
the permutation must have no fixed points. That is, for every i (1 ≤ i ≤ n), pi≠i must be satisfied.
Let's call the permutation that satisfies these requirements funny.

For example, let n=4. Then [4,3,1,2] is a funny permutation, since:

to the right of p1=4 is p2=p1−1=4−1=3;
to the left of p2=3 is p1=p2+1=3+1=4;
to the right of p3=1 is p4=p3+1=1+1=2;
to the left of p4=2 is p3=p4−1=2−1=1.
for all i is pi≠i.
For a given positive integer n, output any funny permutation of length n, or output -1 if funny permutation of length n does not exist.

Input
The first line of input data contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The description of the test cases follows.

Each test case consists of f single line containing one integer n (2 ≤ n ≤ 2⋅10^5).

It is guaranteed that the sum of n over all test cases does not exceed 2⋅10^5.

Output
For each test case, print on a separate line:

any funny permutation p of length n;
or the number -1 if the permutation you are looking for does not exist.

Input:
5
4
3
7
5
2

Output:
3 4 2 1
-1
6 7 4 5 3 2 1
5 4 1 2 3
2 1
"""

cases = int(input())
for i in range(cases):
    n = int(input())
    if(n == 3):
        print(-1)
    else:
        print(n, n-1,*range(1,n-1))