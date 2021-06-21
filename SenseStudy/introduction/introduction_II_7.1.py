data,test_data = load_face_sample_dataset('face')
imgs = data[0]
labels = data[1]
#labels = [1]*(len(labels)-1)+[0]

imgs_f = flatten(imgs)

model = linear_classifier()
model.train(imgs_f,labels)
pred = model.predict(imgs_f)

acc = accuracy(pred,labels)
print('训练集准确率为：',acc)

test_imgs = test_data[0]
test_labels = test_data[1]
test_imgs_f = flatten(test_imgs)
test_pred = model.predict(test_imgs_f)
test_acc = accuracy(test_pred,test_labels)
print('测试集准确率为：',test_acc)

print('测试图片总数：',len(test_pred))

for i in range(20):
    show_img(test_imgs[i])
    if test_labels[i]==0:
        print('Ground Truth: It has NO face in the image.')
    else:
        print('Ground Truth: It has a face in the image.')
    if test_pred[i]==0:
        print('Prediction: It has NO face in the image.')
    else:
        print('Prediction: It has a face in the image.')
