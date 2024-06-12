"""

--------------------------- Link for the challenge: https://codeforces.com/problemset/problem/1676/C -------------------------------

You are given n words of equal length m, consisting of lowercase Latin alphabet letters. The i-th word is denoted s(i).

In one move you can choose any position in any single word and change the letter at that position to the previous or next letter in alphabetical order. For example:

you can change 'e' to 'd' or to 'f';
'a' can only be changed to 'b';
'z' can only be changed to 'y'.

The difference between two words is the minimum number of moves required to make them equal. For example, the difference between "best" and "cost" is 1+10+0+0=11.

Find the minimum difference of s(i) and s(j) such that (i < j). In other words, find the minimum difference over all possible pairs of the n words.

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The description of test cases follows.

The first line of each test case contains 2 integers n and m (2 ≤ n ≤ 50, 1 ≤ m ≤ 8) — the number of strings and their length respectively.

Then follows n lines, the i-th of which containing a single string s(i) of length m, consisting of lowercase Latin letters.

Output
For each test case, print a single integer — the minimum difference over all possible pairs of the given strings.

Input:
6
2 4
best
cost
6 3
abb
zba
bef
cdu
ooo
zzz
2 7
aaabbbc
bbaezfe
3 2
ab
ab
ab
2 8
aaaaaaaa
zzzzzzzz
3 1
a
u
y

Output:
11
8
35
0
200
4
"""
cases = int(input())
for i in range(cases):
    n, m = map(int, input().split())
    arr = []
    for j in range(n):
        arr.append(input())
    ans = 3000
    for w in range(n):
        word = arr[w]
        for k in range(w + 1, n):
            tempWord = arr[k]
            tempSum = 0
            for c in range(m):
                n1 = ord(word[c]) - 96
                n2 = ord(tempWord[c]) - 96
                tempSum += abs(n1 - n2)
            if(tempSum < ans):
                ans = tempSum
    print(ans)