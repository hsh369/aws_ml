import math


def reward_function(params):

   # Read input variables
    speed = params['speed']
    tw = params['track_width']
    steering_angle = params['steering_angle']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    dfc = params['distance_from_center']
    heading = params['heading']
    abs_steering = abs(params['steering_angle'])
    is_left_of_center = params['is_left_of_center']

    steps = params['steps']
    progress = params['progress']

    # Initialize the reward with typical value
    reward = 1.0
    speed = 1.0

    # Set the thresholds based your action space
    DIRECTION_THRESHOLD = 15.0
    SPEED_THRESHOLD = 1.0
    ABS_STEERING_THRESHOLD = 15.0
    TOTAL_NUM_STEPS = 400

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

    if tw/6 >= dfc:
        reward *= 1.5
    elif tw/4 >= dfc > tw/6:
        reward *= 0.8
    elif tw/2 >= dfc > tw/4:
        reward *= 0.2
    else:
        return float(1e-3)

    if direction_diff < DIRECTION_THRESHOLD or abs_steering < ABS_STEERING_THRESHOLD:
        reward *= 1.3
    else:
        reward *= 0.6

    if speed > SPEED_THRESHOLD:
        reward *= 1.4
    elif 0.9 < speed < SPEED_THRESHOLD:
        reward *= 0.8
    else:
        reward *= 0.5

    if (steering_angle < 0 and is_left_of_center) or (steering_angle > 0 and not is_left_of_center):
        reward *= 1.3
    else:
        reward *= 0.8

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
        reward *= 2.0
    else:
        reward *= 0.5

    return float(reward)
