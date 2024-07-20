#In a magical land, there is a young explorer named Raju who embarks on a thrilling adventure with his enchanted vehicle. This magical vehicle can only move in four directions: right (R), left (L), up (U), and down (D). Raju starts his journey at the heart of the mystical forest, located at coordinates (0, 0).

As Raju follows a sequence of mysterious symbols etched on ancient stones, he maneuvers his magical vehicle accordingly. 'R' guides him to the right, 'L' to the left, 'U' upwards, and 'D' downwards. The direction he faces does not matter; the symbols' magic ensures his vehicle moves in the intended direction.

Your mission is to help Raju determine whether he will return to the enchanted forest's center (0,0) after completing all his moves. If he successfully navigates back to the starting point, the forest's magic will protect him, and he will be able to continue his adventure. If not, he might be lost in the mystical realm forever.

Can you assist Raju in deciphering his fate? If he ends up back at the starting point, please say YES; otherwise, say NO.

Input Format
The first line of the input contains an integer n  — the size of string moves
The second line contains the string moves
Output Format
Raju needs to print ”YES” if car returns to origin, else “NO”.

Constraints
1 <= moves.length <= 2 * 104
moves only contains the characters 'U', 'D', 'L' and 'R'.#

def will_return_to_origin(n, moves):
    x, y = 0, 0  # starting coordinates

    for move in moves:
        if move == 'R':
            x += 1
        elif move == 'L':
            x -= 1
        elif move == 'U':
            y += 1
        elif move == 'D':
            y -= 1

    # Check if we are back at the origin
    if x == 0 and y == 0:
        return "YES"
    else:
        return "NO"

# Read input
n = int(input().strip())
moves = input().strip()

# Print the result
print(will_return_to_origin(n, moves))


