import cv2 as cv
import pytesseract as pte


img = cv.imread("murt.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


# print(pte.image_to_string(img))
# print(pte.image_to_data(img))




# Detecting words
boxes = pte.image_to_data(img)
for x, b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        # print(b)
        if len(b) == 12:
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9]), 
            cv.rectangle(img, (x,  y), (w + x, h + y), (0,0,255), 3)
            cv.putText(img, b[11], (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 2)

cv.imshow("Result", img)
cv.waitKey(0)