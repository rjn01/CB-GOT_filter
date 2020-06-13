


import cv2

#CLASSIFIERS
eye_cascade = cv2.CascadeClassifier('frontalEyes35x16.xml')
nose_cascade = cv2.CascadeClassifier('Nose18x15.xml') 

#READNG THE IMAGES
glass =cv2.imread('glasses.png',cv2.IMREAD_UNCHANGED)
much = cv2.imread('mustache.png',cv2.IMREAD_UNCHANGED)
pic = cv2.imread('Jamie_Before.jpg')

gray = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
eyes= eye_cascade.detectMultiScale(gray)
nose=nose_cascade.detectMultiScale(gray)


x,y,w,h=eyes[0]

glass = cv2.cvtColor(glass,cv2.COLOR_BGR2RGBA)
glass=cv2.resize(glass,(h,w))


for i in range(glass.shape[0]):
    for j in range(glass.shape[1]):
        if(glass[i,j,3]>0):#opacity for white color is 0. 
            pic[y+i,x+j,:]=glass[i,j,:-1]

a,b,c,d=nose[0]

much = cv2.cvtColor(much,cv2.COLOR_BGR2RGBA)
much=cv2.resize(much,(d,c))


for u in range(much.shape[0]):
    for v in range(much.shape[1]):
        if(much[u,v,3]>0):#opacity for white color is 0. 
            pic[b+u,a+v,:]=much[u,v,:-1]


          

cv2.imshow("frame",pic)
cv2.imshow("much",much)
cv2.imshow('glass',glass)

cv2.waitKey(0)
cv2.destroyAllWindows()
















