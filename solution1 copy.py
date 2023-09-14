# Interview question: Euclidean Distance
# On the Cartesian coordinate system (2-D plane), we have coordinates (x,y) that make up lines.
# Write python code that uses the coordinates to calculate the euclidean distance for each line
# and then outputs a dictionary in order of the smallest distance to the largest distance.
# note: for measuring the distance between two points ((x1, y1) and (x2,y2)), you can use the following formula:
# distance = sqrt((x2-x1)**2 + (y2-y1)**2))
# Input Format: a list of x,y coordinates forming lines. Coordinates are real numbers.
# Output Format: euclidean distance for each line and a dictionary of lines in order of the line with the
# smallest distance to the largest distance.
import math
import time

start = time.time()


# Function that takes in co-ordinates of a line to work out euclidean distance.
def euclidean_distance(x1, y1, x2, y2):
    # Equation to calculate euclidean distance.
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


# Function that asks the user for the coordinates and applies them into the euclidean distance function,
# as well as sorting the distances from smallest to largest.
def get_coordinates():
    no_of_lines = int(input('Enter the number of lines: '))
    # Empty dictionary to store the euclidean distances of each line.
    distances = {}
    # For loop to ask user to input x,y co-ordinates for each line.
    for line in range(no_of_lines):
        # Assign co-ordinates for each x and y.
        x1 = float(input(f'Enter the x1 co-ordinate for line {line + 1}: '))
        y1 = float(input(f'Enter the y1 co-ordinate for line {line + 1}: '))
        x2 = float(input(f'Enter the x2 co-ordinate for line {line + 1}: '))
        y2 = float(input(f'Enter the y2 co-ordinates for line {line + 1}: '))
        distances[f'line_{line+1}_distance'] = euclidean_distance(x1, y1, x2, y2)

    # For loop to print the distance of each line in the 'distances' dictionary, using format function.
    for line, distance in distances.items():
        print(f'{line}: {distance:.2f}')

# Python built-in sorted function which uses timsort to order the distances from smallest to largest distance.
    sorted_distances = sorted(distances.items(), key=lambda x:x[1])
    print('shortest distance to longest distance:', sorted_distances)
    return distances


get_coordinates()

# Calculates and displays the time it takes to run the functions using time module.
print('the time taken is', time.time()-start, 'seconds.')
