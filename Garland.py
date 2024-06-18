"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1809/A -----------------------------

You have a garland consisting of 4 colored light bulbs, the color of the i-th light bulb is s(i).

Initially, all the light bulbs are turned off. Your task is to turn all the light bulbs on. You can perform the following operation any number of times: 
select a light bulb and switch its state (turn it on if it was off, and turn it off if it was on). The only restriction on the above operation is that 
you can apply the operation to a light bulb only if the previous operation was applied to a light bulb of a different color (the first operation can be applied to any light bulb).

Calculate the minimum number of operations to turn all the light bulbs on, or report that this is impossible.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The single line of each test case contains s — a sequence of 4 characters, where each character is a decimal digit. The i-th character denotes the color of the i-th light bulb.

Output
For each test case, print one integer — the minimum number of operations to turn all the light bulbs on. If it is impossible to turn all the bulbs on, print -1.

Input:
3
9546
0000
3313

Output:
4
-1
6
"""
cases = int(input())
for i in range(cases):
    numStr = input()
    if(numStr[0] == numStr[1] == numStr[2] == numStr[3]):
        print(-1)
    elif(numStr[0] != numStr[1] != numStr[2] != numStr[3]):
        print(4)
    elif((numStr[0] == numStr[1] == numStr[2] and numStr[0] != numStr[3]) or
         (numStr[0] == numStr[1] == numStr[3] and numStr[0] != numStr[2]) or
         (numStr[0] == numStr[2] == numStr[3] and numStr[0] != numStr[1]) or
         (numStr[1] == numStr[2] == numStr[3] and numStr[1] != numStr[0])):
        print(6)
    else:
        print(4)