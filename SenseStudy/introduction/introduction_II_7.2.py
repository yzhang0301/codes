from plotlib import fig, plot
img_list = []
label_list = []
feat_list = []

trainset,testset = load_list()
img_list,label_list = trainset
print(len(img_list))
for i in range(5):
    img = load_img(img_list[i])
    fig() + plot(img)
    print(label_list[i])

HF = hogfeature()

def extract_hog(path):
    img = load_img(path)
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img_resize = cv2.resize(img_gray,(100,100))
    return HF.getHog(img_resize,0)

for img in img_list:
    feat = extract_hog(img)
    feat_list.append(feat)
    
model = linear_classifier()
model.train(feat_list,label_list)
pred = model.predict(feat_list)
print(accuracy(pred,label_list))

test_img_list = []
test_label_list = []
test_feat_list = []

test_img_list,test_label_list = testset

for test_img in test_img_list:
    test_feat = extract_hog(test_img)
    test_feat_list.append(test_feat)
    
test_pred = model.predict(test_feat_list)
print(accuracy(test_pred,test_label_list))
