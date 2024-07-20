#Once upon a time, a city biker embarked on an exciting road trip. This journey was laid out across a sequence of n+1 points, each with varying altitudes. The biker's adventure commenced at point 0, where the altitude was a humble 0 meters above sea level.
During his expedition, he encountered different terrains. For every segment between points i and i+1, where 0≤i<n, the biker faced varying challenges in altitude. Each segment was represented by an integer array called gain of length n, where gain[i] denoted the net gain in altitude between points i and i+1.
The biker's goal was to find the highest altitude he reached during his journey. This altitude was determined by the net gain in altitude at each point along the way. It could be a thrilling peak or a serene valley, depending on the varying gains between consecutive points.

Input Format
The first line of the input contains an integer n  - the number of elements.
The next  line contains n space-separated integers.
Output Format
City Biker needs to return the highest altitude of a point.

Constraints
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100#

# Read the number of elements in the gain array
n = int(input().strip())

# Read the gain array
gain = list(map(int, input().strip().split()))

# Initialize starting altitude
current_altitude = 0

# Initialize the highest altitude to the starting point
highest_altitude = current_altitude

# Calculate altitudes and find the highest one
for g in gain:
    current_altitude += g
    if current_altitude > highest_altitude:
        highest_altitude = current_altitude

# Print the highest altitude
print(highest_altitude)
