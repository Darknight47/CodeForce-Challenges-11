"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1895/A ---------------------------

Monocarp has found a treasure map. The map represents the treasure location as an OX axis. Monocarp is at 0, the treasure chest is at x, the key to the chest is at y.

Obviously, Monocarp wants to open the chest. He can perform the following actions:

go 1 to the left or 1 to the right (spending 1 second);
pick the key or the chest up if he is in the same point as that object (spending 0 seconds);
put the chest down in his current point (spending 0 seconds);
open the chest if he's in the same point as the chest and has picked the key up (spending 0 seconds).
Monocarp can carry the chest, but the chest is pretty heavy. He knows that he can carry it for at most k seconds in total (putting it down and picking it back up doesn't reset his stamina).

What's the smallest time required for Monocarp to open the chest?

Input
The first line contains a single integer t (1 ≤ t ≤ 100) — the number of testcases.

The only line of each testcase contains three integers x,y and k (1 ≤ x, y ≤ 100; x ≠ y; 0 ≤ k ≤ 100) — the initial point of the chest, 
the point where the key is located, and the maximum time Monocarp can carry the chest for.

Output
For each testcase, print a single integer — the smallest time required for Monocarp to open the chest.

Input:
3
5 7 2
10 5 0
5 8 2

Output:
7
10
9
"""
cases = int(input())
for i in range(cases):
    x, y, k = map(int, input().split())
    if(x >= y):
        print(x)
    else:
        diff = y - x
        if(diff <= k):
            print(y)
        else:
            temp = x + k
            td = abs(y - temp) * 2
            print(temp + td)