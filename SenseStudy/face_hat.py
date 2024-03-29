import cv2
import dlib
import imutils
from matplotlib import pyplot as plt

detector = dlib.get_frontal_face_detector()

img = load_image_url('http://sensestudy-server/api/resource/public/accountstorage-objs/18ff97da-ead9-439d-82b5-deebcc29502a/zy1.jpeg')

print(img[0,0,0])

for i in range(100):
    for j in range(100):
        img[i,j,:] = 0

plt.imshow(img)
plt.show()
img = img[:,:,::-1]
img = imutils.resize(img, width = 200)
print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)
plt.imshow(img)
plt.show()
plt.imshow(gray,plt.cm.gray)
plt.show()


rects = detector(gray, 0)
for rect in rects:
    print(rect)
    cv2.rectangle(img, (rect.left(),rect.top()), (rect.right(),rect.bottom()), (0,255,0), 1)
            
plt.imshow(img)
plt.show()

overlay = load_image_url('https://raw.githubusercontent.com/yzhang0301/codes/master/hat.png')
plt.imshow(overlay)
plt.show()

overlay = imutils.resize(overlay, width = 50)
mask = overlay / 255

background = img
x = rect.left() + 12
y = rect.top() -20
h, w = overlay.shape[0], overlay.shape[1]
print(h,w)
background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay
#background[y:y+h, x:x+w] = overlay
plt.imshow(background)
plt.show()
