"""

----------------------- Link for the challenge: https://codeforces.com/problemset/problem/1976/A ----------------------------

Monocarp is working on his new site, and the current challenge is to make the users pick strong passwords.

Monocarp decided that strong passwords should satisfy the following conditions:

password should consist only of lowercase Latin letters and digits;
there should be no digit that comes after a letter (so, after each letter, there is either another letter or the string ends);
all digits should be sorted in the non-decreasing order;
all letters should be sorted in the non-decreasing order.
Note that it's allowed for the password to have only letters or only digits.

Monocarp managed to implement the first condition, but he struggles with the remaining ones. Can you help him to verify the passwords?

Input
The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of testcases.

The first line of each testcase contains a single integer n (1 ≤ n ≤ 20) — the length of the password.

The second line contains a string, consisting of exactly n characters. Each character is either a lowercase Latin letter or a digit.

Output
For each testcase, print "YES" if the given password is strong and "NO" otherwise.


Input:
5
4
12ac
5
123wa
9
allllmost
5
ac123
6
011679

Output:
YES
NO
YES
NO
YES
"""


cases = int(input())
for i in range(cases):
    sze = int(input())
    password = input()
    ok = True
    for j in range(sze - 1):
        firstChar = password[j]
        secondChar = password[j + 1]
        if(not firstChar.isdigit() and secondChar.isdigit()):
            ok = False
            break
        elif(firstChar.isdigit() and secondChar.isdigit()):
            if(ord(firstChar) > ord(secondChar)):
                ok = False
                break
        elif(firstChar.isupper() or secondChar.isupper()):
            ok = False
            break
        elif(not firstChar.isdigit() and not secondChar.isdigit()):
            if(ord(firstChar) > ord(secondChar)):
                ok = False
                break
    print("YES" if ok else "NO")        