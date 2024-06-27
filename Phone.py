"""

------------------------------ Link for the challenge: https://codeforces.com/problemset/problem/1974/A ------------------------

Little Rosie has a phone with a desktop (or launcher, as it is also called). The desktop can consist of several screens. 
Each screen is represented as a grid of size 5×3, i.e., five rows and three columns.

There are x applications with an icon size of 1×1 cells; such an icon occupies only one cell of the screen. 
There are also y applications with an icon size of 2×2 cells; such an icon occupies a square of 4 cells on the screen. Each cell of each screen can be occupied by no more than one icon.

Rosie wants to place the application icons on the minimum number of screens. Help her find the minimum number of screens needed.

Input
The first line of the input contains t (1 ≤ t ≤ 10^4) — the number of test cases.

The first and only line of each test case contains two integers x and y (0 ≤ x, y ≤ 99) — 
the number of applications with a 1×1 icon and the number of applications with a 2×2 icon, respectively.

Output
For each test case, output the minimal number of required screens on a separate line.

Input:
11
1 1
7 2
12 4
0 3
1 0
8 1
0 0
2 0
15 0
8 2
0 9

Output:
1
1
2
2
1
1
0
1
1
2
5
"""
import math
cases = int(input())
for _ in range(cases):
    x, y = map(int, input().split())
    screens_for_2x2 = math.ceil(y / 2)
    remaining_cells_in_screens_for_2x2 = (screens_for_2x2 * 15) - (y * 4)
    x -= remaining_cells_in_screens_for_2x2
    if x <= 0:
        print(screens_for_2x2)
    else:
        # Number of additional screens needed for remaining 1x1 apps
        additional_screens_for_1x1 = math.ceil(x / 15)
        print(screens_for_2x2 + additional_screens_for_1x1)