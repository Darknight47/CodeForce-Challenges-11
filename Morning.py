"""

--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1883/A -----------------

You are given a four-digit pin code consisting of digits from 0 to 9 that needs to be entered. Initially, the cursor points to the digit 1. 
In one second, you can perform exactly one of the following two actions:

Press the cursor to display the current digit,
Move the cursor to any adjacent digit.

1234567890

The image above shows the device you are using to enter the pin code. For example, for the digit 5 , 
the adjacent digits are 4and 6, and for the digit 0, there is only one adjacent digit, 9.

Determine the minimum number of seconds required to enter the given four-digit pin code.

Input
Each test consists of multiple test cases. The first line contains a single integer t
(1 ≤ t ≤ 10^4) - the number of the test cases. This is followed by their description.

The single line of each test case describes the pin code as a string of length 4, consisting of digits from 0 to 9.

Output
For each test case, output the minimum number of seconds required to enter the given pin code.

Input:
10
1111
1236
1010
1920
9273
0000
7492
8543
0294
8361

Output:
4
9
31
27
28
13
25
16
33
24
"""
cases = int(input())
for i in range(cases):
    pins = input()
    current = 1
    ans = 0
    for d in pins:
        dig = int(d)
        if(dig == current):
            ans += 1
            current = dig
        else:
            if(dig == 0):
                ans += abs(current - 10) + 1
                current = 10
            else:
                ans += abs(dig - current) + 1
                current = dig
    print(ans)                