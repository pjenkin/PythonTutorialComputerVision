import cv2, time, numpy as np

# setx  OPENCV_VIDEOIO_PRIORITY_MSMF 0
# setx OPENCV_VIDEOIO_DEBUG 1
np.set_printoptions(threshold=np.inf)       # print out all of numpy array


print(cv2.__version__)
video = cv2.VideoCapture(0)     # 0 for first camera

count = 1

while True:
    count = count + 1
    check, frame = video.read()     # check is boolean, frame is a numpy array

    # time.sleep(3)


    print(check)
    print(frame)


    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # dilemma - whether to call var 'grey' or 'gray' ...?
    #time.sleep(3)
    # cv2.imshow('Capturing', frame)
    cv2.imshow('Capturing', grey)

    print('Grey following:')
    print(grey)
    # NB more frames if no huge arrays printed


    # cv2.waitKey(0)
    key = cv2.waitKey(1000)

    if key == ord('q'):
        break

print(str(count) + ' frames')

video.release()

cv2.destroyAllWindows()
