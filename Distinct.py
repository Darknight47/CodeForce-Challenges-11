"""

------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1909/A ---------------------------

You are located at the point (0,0) of an infinite Cartesian plane. You have a controller with 4 buttons which can perform one of the following operations:

U: move from (x,y) to (x,y+1);
R: move from (x,y) to (x+1,y);
D: move from (x,y) to (x,y−1); 
L: move from (x,y) to (x−1,y).
Unfortunately, the controller is broken. If you press all the 4 buttons (in any order), the controller stops working. It means that, during the whole trip, you can only press at most 3
distinct buttons (any number of times, in any order).

There are n special points in the plane, with integer coordinates (xi,yi).

Can you visit all the special points (in any order) without breaking the controller?

Input
Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 1000). The description of the test cases follows.

The first line of each test case contains a single integer n (1 ≤ n ≤ 100) — the number of special points.

Each of the next n lines contains two integers x(i), y(i) (−100 ≤ x(i), y(i) ≤ 100), which represent the special point (xi,yi).

Note that there are no constraints on the sum of n over all test cases.

Output
For each test case, output "YES" (without quotes), if you can reach all the special points without breaking the controller, and "NO" (without quotes) otherwise.

You may output each letter in any case (for example, "YES", "Yes", "yes", "yEs" will all be recognized as positive answer).

Input:
6
3
1 -1
0 0
1 -1
4
-3 -2
-3 -1
-3 0
-3 1
4
1 1
-1 -1
1 -1
-1 1
6
-4 14
-9 -13
-14 5
14 15
-8 -4
19 9
6
82 64
39 91
3 46
87 83
74 21
7 25
1
100 -100

Output:
YES
YES
NO
NO
YES
YES
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    right = left = up = down = False
    for i in range(sze):
        x, y = map(int, input().split())
        if(x > 0):
            right = True
        elif( x < 0):
            left = True
        
        if(y > 0):
            up = True
        elif(y < 0):
            down = True
    print("NO" if(right and left and up and down) else "YES")