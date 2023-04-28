# Place import statement outside of function (supported libraries: math, random, numpy, scipy, and shapely)# Example imports of available libraries##
import math
import random
import numpy
import scipy
# import shapely
# import mathdef


def reward_function(params):
    ''' Example of using waypoints and heading to make the car point in the right direction '''
    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    # Initialize the reward with typical value
    reward = 1.0

    # Calculate the direction of the centerline based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(
        next_point[1] - prev_point[1], next_point[0] - prev_point[0])

    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)

    if direction_diff > 180:
        # Penalize the reward if the difference is too large
        direction_diff = 360 - direction_diff
        
    DIRECTION_THRESHOLD = 10.0
    
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= 0.5
        
    return float(reward)
