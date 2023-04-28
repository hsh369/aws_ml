import math
def reward_function(params):

   # Read input variables
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    abs_steering = abs(params['steering_angle'])
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']
    
    reward = 1.0

    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 3.0
    ABS_STEERING_THRESHOLD = 20.0
    DIRECTION_THRESHOLD = 10.0
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
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
       
        
    if speed > SPEED_THRESHOLD or distance_from_center <= marker_1 or abs_steering < ABS_STEERING_THRESHOLD:
        # # High reward if the car stays on track and goes fast
        reward = 1.0

    elif SPEED_THRESHOLD-2.0 < speed < SPEED_THRESHOLD or distance_from_center <= marker_2 or abs_steering > ABS_STEERING_THRESHOLD or direction_diff > DIRECTION_THRESHOLD:
        reward = 0.5

    elif speed < SPEED_THRESHOLD-2.0 or distance_from_center <= marker_3:
        # # Penalize if the car goes too slow
        reward = 0.1

    else:
        # Penalize if the car goes off track
        reward = 1e-3

    return float(reward)