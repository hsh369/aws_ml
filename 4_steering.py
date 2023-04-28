# AWS DeepRacer Student User Guidesteering_angle
# Example: A reward function using the steering_angle parameter

def reward_function(params):
    '''     Example of using steering angle     '''
    # Read input variable
    abs_steering = abs(params['steering_angle'])
    # We don't care whether it is left or  right steering
    # # Initialize the reward with typical value
    reward = 1.0
    
    # Penalize if car steer too much to prevent zigzag
    ABS_STEERING_THRESHOLD = 20.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
        
    return float(reward)
