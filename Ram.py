"""

---------------------- Link for the challenge: https://codeforces.com/problemset/problem/1629/A -----------------------------------

Did you know you can download more RAM? There is a shop with n different pieces of software that increase your RAM. 
The i-th RAM increasing software takes ai GB of memory to run (temporarily, once the program is done running, you get the RAM back), 
and gives you an additional bi GB of RAM (permanently). Each software can only be used once. Your PC currently has k GB of RAM.

Note that you can't use a RAM-increasing software if it takes more GB of RAM to use than what you currently have.

Since RAM is the most important thing in the world, you wonder, what is the maximum possible amount of RAM achievable?

Input
The first line of the input contains a single integer t (1 ≤ t ≤ 100) — the number of test cases. The description of test cases follows.

The first line of each test case contains the integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 1000). 
Then two lines follow, each containing n integers describing the arrays a and b (1 ≤ a(i), b(i) ≤ 1000).

Output
For each test case, output a single line containing the largest amount of RAM you can achieve.

Input:
4
3 10
20 30 10
9 100 10
5 1
1 1 5 1 1
1 1 1 1 1
5 1
2 2 2 2 2
100 100 100 100 100
5 8
128 64 32 16 8
128 64 32 16 8

Output:
29
6
1
256
"""

cases = int(input())
for i in range(cases):
    n, currentRam = map(int, input().split())
    softwares = list(map(int, input().split()))
    rams = list(map(int, input().split()))
    tuples = [(software, ram) for software, ram in zip(softwares, rams)]
    sorted_tuples = sorted(tuples, key=lambda x: x[0])
    for tt in sorted_tuples:
        if(tt[0] <= currentRam):
            currentRam += tt[1]
        else:
            break
    print(currentRam)