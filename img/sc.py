import cv2

img = cv2.imread("3.png")
print(img.shape)
img2 = cv2.resize(img, (1280,960))

cv2.imwrite("test2.png", img2)