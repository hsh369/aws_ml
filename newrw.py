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

    # Set the thresholds based your action space
    DIRECTION_THRESHOLD = 10.0
    SPEED_THRESHOLD = 4.0
    ABS_STEERING_THRESHOLD = 15.0
    TOTAL_NUM_STEPS = 300

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

    if tw/8 >= dfc:
        reward *= 1.5
    elif tw/4 >= dfc > tw/8:
        reward *= 0.4
    elif tw/2 >= dfc > tw/4:
        reward *= 0.1
    else:
        return float(1e-3)

    if direction_diff > DIRECTION_THRESHOLD or abs_steering > ABS_STEERING_THRESHOLD or speed < SPEED_THRESHOLD:
        reward *= 0.7
    else:
        reward *= 1.2

    if (steering_angle < 0 and is_left_of_center) or (steering_angle > 0 and not is_left_of_center):
        reward *= 1.1
    else:
        reward *= 0.9

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
        reward += 10.0

    return float(reward)
