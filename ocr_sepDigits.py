import cv2 as cv
import pytesseract as pte


img = cv.imread("murt.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


#Detecting individual digits 
hImg, wImg, _ = img.shape
myconfig = r"--oem 3 --psm 6 outputbase digits"

boxes = pte.image_to_boxes(img, config=myconfig)

for b in boxes.splitlines():
    # print(b)
    b = b.split(" ")
    # print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv.rectangle(img, (x, hImg - y), (w, hImg - h), (0,0,255), 3)
    cv.putText(img, b[0], (x, hImg-y+25), cv.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)
cv.imshow("img", img)

cv.waitKey(0)