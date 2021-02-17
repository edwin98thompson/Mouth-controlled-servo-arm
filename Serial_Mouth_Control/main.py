import serial
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread

from Bluetooth_handler import bluetooth_handler
from Mouth_analyser import mouth_aspect_ratio, mouth_locator
from Serial_handler import serial_handler
from Draw_region import regions
import argparse
import imutils
import dlib
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=False, default='shape_predictor_68_face_landmarks.dat',
                help="path to facial landmark predictor")
ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
args = vars(ap.parse_args())

# define one constants, for mouth aspect ratio to indicate open mouth
MOUTH_AR_THRESH = 0.69

# initialize dlib's face detector (HOG-based) and then create and facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# grab the indexes of the facial landmarks for the mouth
(mStart, mEnd) = (49, 68)

# start the video stream thread
print("[INFO] starting video stream thread...")
vs = VideoStream(src=args["webcam"]).start()
frame_width = 640
frame_height = 360

while True:

    # grab the frame from the threaded video file stream, resize and convert to grayscale
    servo = '0'
    mouth_state = '0'
    frame = vs.read()
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    regions(frame, frame_width, frame_height)

    # detect faces in the grayscale frame
    rects = detector(gray, 0)
    # loop over the face detections
    for rect in rects:
        # determine the facial landmarks for the face region, then convert the facial (x, y)-coordinates to array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # extract the mouth coordinates, then use the coordinates to compute the mouth aspect ratio
        mouth = shape[mStart:mEnd]
        mouthMAR = mouth_aspect_ratio(mouth)
        mar = mouthMAR

        # compute the convex hull for the mouth, then visualize the mouth
        if mar > MOUTH_AR_THRESH:
            mouth_state = '1'
            cv2.putText(frame, "Mouth is Open!", (460, 310),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            mouth_state = '0'

        mouthHull = cv2.convexHull(mouth)
        cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
        cv2.putText(frame, "MAR: {:.2f}".format(mar), (500, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        mouth_x = mouthHull[0][0][0]
        mouth_y = mouthHull[0][0][1]
        # print(mouth_x, mouth_y)

        servo_cmd = mouth_locator(mouth_state, mouth_x, mouth_y)
        print(servo_cmd)
        bluetooth_handler('COM9', servo_cmd)
        # serial_handler(servo_cmd)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
