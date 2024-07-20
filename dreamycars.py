#In a lively car showroom, an array of cars awaits, each with its distinctive features. Picture yourself mixing and matching these cars in unique combinations to create dream blends which has a fscore equal to the XOR value of the combination. 

Your mission: compute the blend score, which is the XOR of the fscore values for all these dreamy combinations. 

Now, it's time to reveal the grand total!

Input Format
The first line of input consists of the integer n – representing the number of cars in the showroom.

The second line consists of n integers - representing the features of the car. 

Output Format
Print the sum of fscore obtained.

Constraints
1 <= n<= 10^4

0 <= fi <= 10^4.#

def compute_blend_score(features):
    n = len(features)
    # Total number of times each feature is included in the XOR sum
    times_included = 1 << (n - 1)
    
    # If times_included is even, the XOR will be zero because each feature will cancel out
    if times_included % 2 == 0:
        return 0
    
    # If times_included is odd, the result is the XOR of all features
    result = 0
    for feature in features:
        result ^= feature
    
    return result

# Read input
n = int(input().strip())
features = list(map(int, input().strip().split()))

# Compute and print the blend score
print(compute_blend_score(features))
