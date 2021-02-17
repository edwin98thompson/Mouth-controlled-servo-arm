from scipy.spatial import distance as dist

# Dimensions
frame_width = 640
frame_height = 360

# Region definitions
servo1_x_min = 0
servo1_x_max = int(frame_width / 3)
servo1_y_min = int(frame_height / 3)
servo1_y_max = int(2 * (frame_height / 3))
servo2_x_min = 2 * servo1_x_max
servo2_x_max = frame_width
servo2_y_min = int(frame_height / 3)
servo2_y_max = int(2 * (frame_height / 3))
servo3_x_min = 0
servo3_x_max = int(frame_width / 3)
servo3_y_min = 0
servo3_y_max = servo1_y_min
servo4_x_min = servo1_x_max
servo4_x_max = servo2_x_min
servo4_y_min = 0
servo4_y_max = servo1_y_min
servo5_x_min = servo2_x_min
servo5_x_max = frame_width
servo5_y_min = 0
servo5_y_max = servo1_y_min
output = ''


def mouth_aspect_ratio(mouth):
    # compute the euclidean distances between the two sets of
    # vertical mouth landmarks (x, y)-coordinates
    A = dist.euclidean(mouth[2], mouth[10])  # 51, 59
    B = dist.euclidean(mouth[4], mouth[8])  # 53, 57

    # compute the euclidean distance between the horizontal
    # mouth landmark (x, y)-coordinates
    C = dist.euclidean(mouth[0], mouth[6])  # 49, 55

    # compute the mouth aspect ratio
    mar = (A + B) / (2.0 * C)

    # return the mouth aspect ratio
    return mar


def mouth_locator(mouth_state, mouth_x, mouth_y):
    if mouth_x < servo1_x_max and servo1_y_min < mouth_y < servo1_y_max:
        if mouth_state == '1':
            servo = '1'
        else:
            servo = '2'
    elif mouth_x > servo2_x_min and servo2_y_min < mouth_y < servo2_y_max:
        if mouth_state == '1':
            servo = '3'
        else:
            servo = '4'
    elif mouth_x < servo3_x_max and mouth_y < servo3_y_max:
        if mouth_state == '1':
            servo = '5'
        else:
            servo = '6'
    elif mouth_y < servo4_y_max and servo4_x_min < mouth_x < servo4_x_max:
        if mouth_state == '1':
            servo = '7'
        else:
            servo = '8'
    elif servo5_x_min < mouth_x and mouth_y < servo5_y_max:
        if mouth_state == '1':
            servo = '9'
        else:
            servo = 'a'
    else:
        servo = '0'

    return servo
