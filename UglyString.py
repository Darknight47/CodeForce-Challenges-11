"""

-------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1941/C -----------------------------

Rudolf has a string s of length n. 
Rudolf considers the string s to be ugly if it contains the substring† "pie" or the substring "map", otherwise the string s will be considered beautiful.

For example, "ppiee", "mmap", "dfpiefghmap" are ugly strings, while "mathp", "ppiiee" are beautiful strings.

Rudolf wants to shorten the string s by removing some characters to make it beautiful.

The main character doesn't like to strain, so he asks you to make the string beautiful by removing the minimum number of characters. 
He can remove characters from any positions in the string (not just from the beginning or end of the string).

† String a is a substring of b if there exists a consecutive segment of characters in string b equal to a.

Input
The first line contains a single integer t (1 ≤ t ≤ 10^4) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n (1 ≤ n ≤ 10^6) — the length of the string s.

The next line of each test case contains the string s of length n. The string s consists of lowercase Latin letters.

The sum of n over all test cases does not exceed 10^6.

Output
For each test case, output a single integer — the minimum number of characters that need to be deleted to make the string s beautiful. 
If the string is initially beautiful, then output 0.

Input:
6
9
mmapnapie
9
azabazapi
8
mappppie
18
mapmapmapmapmapmap
1
p
11
pppiepieeee

Output:
2
0
2
6
0
2
"""
cases = int(input())
for i in range(cases):
    sze = int(input())
    s = input()
    ans = 0
    indx = 0
    while True:
        temp = ""
        if(indx + 3 <= sze):
            temp = s[indx:indx + 3]
            if(temp == 'map' or temp == 'pie'):
                ans += 1
                indx += 3
            else:
                indx += 1
        else:
            break
    print(ans)