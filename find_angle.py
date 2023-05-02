import math
 
def angle3pt(a, b, c):
    """Counterclockwise angle in degrees by turning from a to c around b
        Returns a float between 180.0 and -180.0"""
    ang = math.degrees(
        math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    ang = ang - 360 if ang > 180 else ang
    return -ang
 
print(angle3pt((2, 2), (2, 4), (4, 2)))
print(angle3pt((2, 2), (2, 4), (4, 6)))
print(angle3pt((2, 2), (2, 4), (2, 6)))
print(angle3pt((2, 2), (2, 4), (0, 6)))
print(angle3pt((2, 2), (2, 4), (0, 2)))