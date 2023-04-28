import cv2
# read image
img = cv2.imread("resources/lena.png")
# preparation for clahe
clahe = cv2.createCLAHE()
# convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# applyng enhancement
enh_img = clahe.apply(gray_img)
# saving to a file
cv2.imwrite('resources/enhanced.png', enh_img)
