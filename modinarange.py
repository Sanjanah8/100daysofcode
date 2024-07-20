#In a game, there are 2 queens which are to be placed on 2 mats. The mats are arranged with orders specified with numbers on them. The placement of the queen is to be done in such a manner that when one of the orders of the mat, when divided with the other order, gives the maximum possible value. The order of the mats is between the two integers denoted by l and r.

Find the order of mats on which the two queens can be placed.

Input Format
The first line contains one positive integer t (1 ≤ t ≤ 104), denoting the number of test cases.

The only line of each test case contains two integers l, r.

Output Format
For every test case, output the largest possible value of a % b over all pairs (a, b denoting the order of mats) for which l <= b <= a <= r.

Constraints
1 <= t <= 104

1 <= l <= r <= 109#

def max_mod_value(l, r):
    if r // 2 + 1 >= l:
        return r % (r // 2 + 1)
    else:
        return r % l

# Read number of test cases
t = int(input().strip())

results = []

# Process each test case
for _ in range(t):
    l, r = map(int, input().strip().split())
    results.append(max_mod_value(l, r))

# Print the results for each test case
for result in results:
    print(result)
