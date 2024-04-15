import cv2
#data set
traineddata=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#read img
img=cv2.imread('images/engineers.jpg')
#convert
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=traineddata.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,114,120),2)

cv2.imshow('st',img)
cv2.waitKey()