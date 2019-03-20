import cv2
import screeninfo       # also use screeninfo, for resizing to monitor

img = cv2.imread('galaxy.jpg', 0)      # -1 for colour

img_height, img_width = img.shape

screen_width = 1e4  # too large as of 2019...
screen_height = 1e4  # too large as of 2019...

# get all monitors for now - end up with smallest of them (never mind for now)
for monitor in screeninfo.get_monitors():
    width = monitor.width
    if width < screen_width:
        screen_width = width
    height = monitor.height
    if height < screen_height:
        screen_height = height

min_ratio = min((screen_height / img_height), (screen_width / img_width))



print(type(img))
print(img)
print(img.shape)
print(img.ndim)         # number of array dimensions


print('min_ratio: ' + str(min_ratio))
#resized_image = cv2.resize(img, (1000, 500))
resized_image = cv2.resize(img, (int((img_width * min_ratio)), int((img_height * min_ratio))))
# resize to monitor, retaining aspect ratio


# cv2.imshow('Galaxy', img)
cv2.imshow('Galaxy', resized_image)

cv2.imwrite('Galaxy_resized.jpg', resized_image)

# cv2.waitKey(2000)      # 0 for close only on button press, 2000 for 2000 ms or button press (whichever first)
cv2.waitKey(0)      # 0 for close only on button press, 2000 for 2000 ms or button press (whichever first)
cv2.destroyAllWindows()


print('cv2.IMREAD_COLOR: ' + str(cv2.IMREAD_COLOR))
print('cv2.IMREAD_GRAYSCALE: ' + str(cv2.IMREAD_GRAYSCALE))
print('cv2.IMREAD_UNCHANGED: ' + str(cv2.IMREAD_UNCHANGED))
