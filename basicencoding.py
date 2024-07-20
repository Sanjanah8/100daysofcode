#You are given a series of queries of the form (a, b), where:

a represents the count of the number b.
For example, the query (3, 5) means the number 5 appears 3 times.

Your task is to compute the absolute difference between the numbers which has the highest and lowest frequencies (least number of times must be atleast once).

If there are multiple possible answers, you should return the maximum possible absolute difference.

Input Format
First line contains a single integer denoting the number of queries.
Second line onwards: two space separated integers denoting the queries
Output Format
Output the maximum possible absolute difference between the numbers which has the highest and lowest frequencies. If there are only two numbers with the same occurrence, the output should be 0.

Constraints
1<=q<=100000.
1<=a,b<=100000.#


def max_absolute_difference(queries):
    from collections import defaultdict
    
    frequency = defaultdict(int)
    
    for a, b in queries:
        frequency[b] += a
    
    if len(frequency) == 1:
        return 0
    
    max_freq = max(frequency.values())
    min_freq = min(frequency.values())
    
    max_freq_numbers = [num for num, freq in frequency.items() if freq == max_freq]
    min_freq_numbers = [num for num, freq in frequency.items() if freq == min_freq]
    
    max_num = max(max_freq_numbers)
    min_num = min(min_freq_numbers)
    
    return abs(max_num - min_num)

# Read input
q = int(input().strip())
queries = [tuple(map(int, input().strip().split())) for _ in range(q)]

# Compute and print the result
print(max_absolute_difference(queries))
