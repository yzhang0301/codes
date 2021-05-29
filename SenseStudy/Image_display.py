import cv2
import dlib
import imutils
from matplotlib import pyplot as plt
from plotlib import fig, plot

detector = dlib.get_frontal_face_detector()

img = load_image_url('http://sensestudy-server/api/resource/public/accountstorage-objs/18ff97da-ead9-439d-82b5-deebcc29502a/zy1.jpeg')

img = img[:,:,::-1]
print(img.shape)
plt.imshow(img)
plt.axis('off')
plt.show()         # Download as SVG format

img = imutils.resize(img, width = 400)
fig() + plot(img)  # Download as PNG format
