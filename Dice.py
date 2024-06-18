"""

---------------------------- Link for the challenge: https://codeforces.com/problemset/problem/378/A -------------------------------

Two players are playing a game. First each of them writes an integer from 1 to 6, and then a dice is thrown. The player whose written number got closer to the number on the dice wins. 
If both payers have the same difference, it's a draw.

The first player wrote number a, the second player wrote number b. How many ways to throw a dice are there, at which the first player wins, or there is a draw, or the second player wins?

Input
The single line contains two integers a and b (1 ≤ a, b ≤ 6) — the numbers written on the paper by the first and second player, correspondingly.

Output
Print three integers: the number of ways to throw the dice at which the first player wins, the game ends with a draw or the second player wins, correspondingly.

Input:
2 5

Output:
3 0 3
"""
a, b = map(int, input().split())
aa = bb = dd = 0
for i in range(1, 7):
    adiff = abs(a - i)
    bdiff = abs(b - i)
    if(adiff < bdiff):
        aa += 1
    elif(adiff > bdiff):
        bb += 1
    else:
        dd += 1
print(aa, dd, bb)