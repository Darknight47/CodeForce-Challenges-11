"""

----------------- Link for the challenge: https://codeforces.com/problemset/problem/1974/B -----------------------

Polycarp has a string s, which consists of lowercase Latin letters. He encodes this string using the following algorithm:

first, he constructs a new auxiliary string r, which consists of all distinct letters of the string s, written in alphabetical order;
then the encoding happens as follows: each character in the string s is replaced by its symmetric character from the string r
(the first character of the string r will be replaced by the last, the second by the second from the end, and so on).
For example, encoding the string s ="codeforces" happens as follows:

the string r is obtained as "cdefors";
the first character s1 ='c' is replaced by 's';
the second character s2 ='o' is replaced by 'e';
the third character s3 ='d' is replaced by 'r';
...
the last character s10 ='s' is replaced by 'c'.

Thus, the result of encoding the string s="codeforces" is the string "serofedsoc".

Write a program that performs decoding — that is, restores the original string s from the encoding result.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases.

The first line of each test case contains a single integer n (1 ≤ n ≤ 2⋅10^5) — the length of the string b.

The second line of each test case contains a string b of length n, consisting of lowercase Latin letters — the result of encoding the original string s.

It is guaranteed that the sum of the values of n over all test cases in the test does not exceed 2⋅10^5.

Output
For each test case, output the string s from which the encoding result b was obtained.

Input:
5
10
serofedsoc
3
ttf
9
tlrhgmaoi
1
w
15
hnndledmnhlttin

Output:
codeforces
fft
algorithm
w
meetinthemiddle
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    stemp = sorted(set(s))
    char_dict = {char: stemp[-i - 1] for i, char in enumerate(stemp)}
    ans = ""
    for ch in s:
        tempChar = char_dict[ch]
        ans += tempChar
    print(ans)