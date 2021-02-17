import cv2


def regions(frame, frame_width, frame_height):
    cv2.line(frame, (0, int(frame_height / 3)), (frame_width, int(frame_height / 3)), (0, 0, 255), 1, 1)
    cv2.line(frame, (0, int(2 * (frame_height / 3))), (frame_width, int(2 * (frame_height / 3))), (0, 0, 255), 1, 1)
    cv2.line(frame, (int(frame_width / 3), 0), (int(frame_width / 3), int(2 * (frame_height / 3))), (0, 0, 255), 1, 1)
    cv2.line(frame, (int(2 * (frame_width / 3)), 0), (int(2 * (frame_width / 3)), int(2 * (frame_height / 3))),
             (0, 0, 255), 1, 1)
