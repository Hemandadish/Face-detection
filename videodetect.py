import cv2

traineddata=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

vedio=cv2.VideoCapture('videos/messi.mp4')
while True:
 success,frame=vedio.read()
 if success==True:
  gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  faces=traineddata.detectMultiScale(gray)
  for x,y,w,h in faces:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

  cv2.imshow('pes',frame)
  cv2.waitKey(1)
 else:
  print("vedio completed")
  break

