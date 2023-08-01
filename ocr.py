import cv2 as cv
import pytesseract

myconfig = r"--psm 11 --oem 3"

def ocr_core(img):
    text = pytesseract.image_to_string(img, config=myconfig)
    return text

img =  cv.imread("/home/umi/Music/tesseract/form.png", cv.IMREAD_COLOR)

# function to check which character is read by OCE 

def reading_char(image):
    height, width =  image.shape
    boxes = pytesseract.image_to_boxes(image, config=myconfig)
    for box in boxes.splitlines():
        box = box.split(" ")
        image = cv.rectangle(image, (int(box[1]), height - int(box[2])), (int(box[3]), height - int(box[4])), (0, 255, 0), 2)
    cv.imshow("image", image)
    cv.waitKey(0)
#get grayscale image

def get_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Function to remove noise
def remove_noise(image):
    return cv.medianBlur(image, 5)


# thresholding

def thresholding(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]


img = get_grayscale(img)
# img = thresholding(img)
# img = remove_noise(img)
# boxes = reading_char(img)
# print(reading_char(img))
print(ocr_core(img))
