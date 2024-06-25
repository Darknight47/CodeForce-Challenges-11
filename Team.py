"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1611/B ---------------------------

The All-Berland Team Programming Contest will take place very soon. This year, teams of four are allowed to participate.

There are a programmers and b mathematicians at Berland State University. How many maximum teams can be made if:

each team must consist of exactly 4 students,teams of 4 mathematicians or 4 programmers are unlikely to perform well, so the decision was made not to compose such teams.
Thus, each team must have at least one programmer and at least one mathematician.

Print the required maximum number of teams. Each person can be a member of no more than one team.

Input
The first line contains an integer t (1 ≤ t ≤ 10^4) —the number of test cases.

This is followed by descriptions of t sets, one per line. Each set is given by two integers a and b (0 ≤ a, b ≤ 10^9).

Output
Print t lines. Each line must contain the answer to the corresponding set of input data — the required maximum number of teams.


Input:
6
5 5
10 1
2 3
0 0
17 2
1000000000 1000000000

Output:
2
1
1
0
2
500000000
"""
cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    temp1 = min(a, b)
    temp2 = (a + b) // 4
    print(min(temp1, temp2))