import cv2

path = "images/example.png" #That's an example path. You can change it!

img = cv2.imread(path) #Reading the image file

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Convert image to a gray image

canny = cv2.Canny(img,70,150) #Making the image canny so you can detect the edges easily!

contours, _= cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #Detecting the contours

#Iterating through the contours
for cnt in contours:
    area = cv2.contourArea(cnt)
    #If contour area is greater than 1000 then it will be displayed.
    if area > 1000:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) #Function for detecting the edge count
        cv2.drawContours(img,cnt,-1,(255,0,0),5)
        edgecount = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) #Drawing rectangles over the shapes
        if edgecount > 10:
            cv2.putText(img, "Circle", (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0)) #If edge count is greater than 10 then it will be counted as a circle.
        else:
            cv2.putText(img,str(edgecount),(x+30,y+30),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0))

cv2.imshow("Output",img) #Displaying the image
cv2.waitKey(0)
