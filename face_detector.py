import cv2
# from cv2 import *
import screeninfo


def min_image_resize_ratio(img_height, img_width):
    """ function to work out appropriate resize scale for monitors (alas, could be any monitor on system) """

    screen_width = 1e4  # too large as of 2019...
    screen_height = 1e4  # too large as of 2019...

    # get all monitors for now - end up with smallest of them (never mind for now)
    for monitor in screeninfo.get_monitors():
        current_width = monitor.width
        if current_width < screen_width:
            screen_width = current_width
        current_height = monitor.height
        if current_height < screen_height:
            screen_height = current_height

    min_ratio = min((screen_height / img_height), (screen_width / img_width))

    return min_ratio

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")     # classifier object

# img = cv2.imread('photo.jpg')
img = cv2.imread('news.jpg')

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img, scaleFactor=1.05, minNeighbors=5)

for x, y, width, height in faces:       # NB tuple unpacking (may be more than 1 'face')
    face_img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 3)
    # extract bounding rectangle from image (RGB green 3-pixel rectangle line drawn)

print(type(faces))
print(faces)    # 4 value array - bounding rectangle, from top-left

img_height, img_width = grey_img.shape
min_ratio = min_image_resize_ratio(img_height, img_width)
resized_face_img = cv2.resize(face_img, (int((img_width * min_ratio)), int((img_height * min_ratio))))

# cv2.imshow('Grey', grey_img)
# cv2.imshow('Grey', face_img)
cv2.imshow('Grey', resized_face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()