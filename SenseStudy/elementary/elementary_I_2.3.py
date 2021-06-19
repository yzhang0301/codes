animal_1 = 'dog'
animal_2 = 'panda'
imgs_1 = load_image_folder(animal_1)
imgs_2 = load_image_folder(animal_2)
#imshow(imgs_2[5])

feature_net = get_net_handle()
features = []
labels = []
for item in imgs_1:
    img_feature = get_animal_feature(feature_net, item)
    features.append(img_feature)
    labels.append(0)
for item in imgs_2:
    img_feature = get_animal_feature(feature_net, item)
    features.append(img_feature)
    labels.append(1)

classifier = get_classifier()
train(classifier, features, labels)

test_imgs = []
for i in range(1, 9):
   test_imgs.append(load_image_url('http://sensestudy-server/api/resource/public/accountstorage-objs/18ff97da-ead9-439d-82b5-deebcc29502a/test_panda/'+str(i)+'.jpg'))

for item in test_imgs:
    imshow(item)
    img_feature = get_animal_feature(feature_net, item)
    res = predict(classifier, img_feature)
    if res == 0:
        print('This is a', animal_1)
    else:
        print('This is a', animal_2)
