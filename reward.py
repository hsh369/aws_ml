import math


def reward_function(params):

   # Read input variables
    speed = params['speed']
    track_width = params['track_width']
    steering_angle = params['steering_angle']
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    distance_from_center = params['distance_from_center']
    

    reward = 1.0
    speed = 5.0
    steering_angle = 0.0

    # Set the speed threshold based your action space
    SPEED_THRESHOLD = 4.0

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.5 * track_width

    # Calculate the direction of the centerline based on the closest waypoints
    c = waypoints[closest_waypoints[2]]
    b = waypoints[closest_waypoints[1]]
    a = waypoints[closest_waypoints[0]]

    road_ang = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    road_ang = road_ang - 360 if road_ang > 180 else road_ang

    if 180-abs(road_ang) <= 30:
        steering_angle = 180 - \
            abs(road_ang) if road_ang < 0 else -(180-abs(road_ang))
    else:
        steering_angle = 30.0 if road_ang < 0 else -30.0

    if distance_from_center > marker_3:
        reward = 1e-3
    elif speed > SPEED_THRESHOLD and distance_from_center <= marker_2:
        reward = 1.0

    elif speed < SPEED_THRESHOLD and distance_from_center <= marker_2 and steering_angle <= 10.0:
        reward = 0.9
        speed = 5.0
    
    elif speed < SPEED_THRESHOLD and distance_from_center <= marker_2 and steering_angle > 10.0:
        reward = 0.8
        speed = 3.0

    elif speed < SPEED_THRESHOLD and distance_from_center <= marker_3 and steering_angle <= 10.0:
        reward = 0.7
        speed = 3.5
    
    elif speed < SPEED_THRESHOLD and distance_from_center <= marker_3 and steering_angle > 10.0:
        reward = 0.5
        speed = 2.0

    else:
        reward = 0.3

    return float(reward)
