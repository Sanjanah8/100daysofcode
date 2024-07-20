#You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string.
If the number of unique strings is less than k, he needs to display an empty string. Considering you are Ashish's best friend can you assist him with this challenge?
Input Format
The first line contains an integer N denoting the number of strings.
The next N lines contain strings.
The next line contains an integer k.
Output Format
The output contains the kth distinct string. If there are less than k unique string display an empty string.#

def kth_unique_string(strings, k):
    # Step 1: Count occurrences of each string
    count = {}
    for string in strings:
        if string in count:
            count[string] += 1
        else:
            count[string] = 1
    
    # Step 2: Collect unique strings in the order they appear
    unique_strings = []
    for string in strings:
        if count[string] == 1:
            unique_strings.append(string)
    
    # Step 3: Return the k-th unique string or empty string if not enough unique strings
    if len(unique_strings) < k:
        return ""
    else:
        return unique_strings[k-1]

# Input
N = int(input().strip())
strings = [input().strip() for _ in range(N)]
k = int(input().strip())

# Find and print the k-th unique string
print(kth_unique_string(strings, k))
