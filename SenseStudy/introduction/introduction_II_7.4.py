from introai_chap7.cv import show_img
from introai.image import imread

trainset,testset = load_face_sample_dataset('gender')
imgs,labels = trainset
features = extract(imgs)

model = linear_classifier()
model.train(features,labels)

imgs,labels = testset
features = extract(imgs)
pred = model.predict(features)
acc = accuracy(pred,labels)
print(acc)

img_test = imgs[2]
#img_test = imread('http://sensestudy-server/api/resource/public/accountstorage-objs/18ff97da-ead9-439d-82b5-deebcc29502a/chow.jpg')
show_img(img_test)
result=model.predict(extract(img_test))
if result == 1:
    print('男性')
else:
    print('女性')
