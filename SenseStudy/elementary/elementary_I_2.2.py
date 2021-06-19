# ---------------- Step 1 -----------------
animal_1 = 'cat'
animal_2 = 'rabbit'
imgs_1 = load_image_folder(animal_1)
imgs_2 = load_image_folder(animal_2)

# ----------------- Step 2 -----------------
feature_net = get_net_handle()
features = []
labels = []

for item in imgs_1:
    img_feature = get_animal_feature(feature_net, item)
    features.append(img_feature)
    labels.append(0) # labelling for cat
    
for item in imgs_2:
    img_feature = get_animal_feature(feature_net, item)
    features.append(img_feature)
    labels.append(1) # labelling for rabbit
    
# ----------------- Step 3 -----------------    
classifier = get_classifier()
train(classifier, features, labels)

# ------------------- Step 4 ----------------
test_imgs = load_image_folder('test')
for img in test_imgs:
    imshow(img)
    feature = get_animal_feature(feature_net, img)
    res = predict(classifier, feature)

    if res == 0:
        print('This is a ', animal_1)
    else:
        print('This is a ', animal_2)
