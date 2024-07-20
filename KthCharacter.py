#One day jack finds a string of characters. He is very keen to arrange the characters in reverse order, i.e., first characters become the last characters, second characters become the second-last characters, and so on.
Now he wants your help  to find the kth character from the new string formed after reverse the original string.
Note: String contain only lowercase Latin letters.
Input Format
The first line contains two integers n, k — the length of array and the value of k respectively.
The second line contains a string containing n characters.
Output Format
Print a single line containing the kth character of the string.
Constraints
1 ≤ k ≤ n≤ 10^6#


n, k = map(int, input().strip().split())
s = input().strip()
reversed_s = s[::-1]
print(reversed_s[k-1])
