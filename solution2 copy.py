# Interview question: Euclidean Distance
# On the Cartesian coordinate system (2-D plane), we have coordinates (x,y) that make up lines.
# Write python code that uses the coordinates to calculate the euclidean distance for each line
# and then outputs a dictionary in order of the smallest distance to the largest distance.
# note: for measuring the distance between two points ((x1, y1) and (x2,y2)), you can use the following formula:
# distance = sqrt((x2-x1)**2 + (y2-y1)**2))
# Input Format: a list of x,y coordinates forming lines. Coordinates are real numbers.
# Output Format: euclidean distance for each line and a dictionary of lines in order of the line with the
# smallest distance to the largest distance.
import time
import math

start = time.time()


# Function to work out euclidean distance using built in math.dist function which takes in two points.
def euclidean_distance(point1, point2):
    distance = math.dist(point1, point2)
    return distance


# Function to get the coordinates and insert them into the euclidean distance function as well as return the distances.
def get_points():
    # Empty dictionary to store the distances.
    distances = {}
    # For loop to ask user to input x,y co-ordinates for 3 lines.
    for i in range(2):
        point1 = tuple(map(float, input(f'Enter the coordinates for point 1 of line {i+1} (x, y) : ').split(',')))
        point2 = tuple(map(float, input(f'Enter the coordinates for point 2 of line {i+1} (x, y): ').split(',')))
        distances[f'line_{i+1}_distance'] = euclidean_distance(point1, point2)

    # For loop to print each lines distance separately from the distances dictionary.
    for i, distance in distances.items():
        print(f'{i}: {distance:.2f}')

    # Bubble sort function to sort the distances dictionary.
    def bubble_sort(distances):
        bubble_sorted_distances = distances
        v = len(bubble_sorted_distances)
        for n in range(v):
            for s in range(v - n - 1):
                if bubble_sorted_distances[f'line_{s + 1}_distance'] > bubble_sorted_distances[f'line_{s + 2}_distance']:
                    bubble_sorted_distances[f'line_{s + 1}_distance'], bubble_sorted_distances[f'line_{s + 2}_distance'] = \
                        bubble_sorted_distances[f'line_{s + 2}_distance'], bubble_sorted_distances[f'line_{s + 1}_distance']
        return bubble_sorted_distances

    bubble_sorted_distances = bubble_sort(distances)
    print('sorted distances from smallest to largest:', bubble_sorted_distances)

    return distances


if __name__ == '__main__':
    get_points()


print('the time taken is', time.time()-start, 'seconds.')
