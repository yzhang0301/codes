diff_level = load_private("diff_level")

texts1, grades1 = load_engtext(subset='rdtrain')
pjtrain_texts = texts1[0:6]
pjtrain_grades = grades1[0:6]
print(pjtrain_grades)
train_feats, train_labels = get_feats_labels(pjtrain_texts, pjtrain_grades, diff_level)

texts2, grades2 = load_engtext(subset='rdtest')
pjtest_texts = texts2[0:6]
pjtest_grades = grades2[0:6]
test_feats, test_labels = get_feats_labels(pjtest_texts, pjtest_grades, diff_level)

save_private([train_feats, train_labels], "primary_junior_train_features")
save_private([test_feats, test_labels], "primary_junior_test_features")

model = LogisticRegressor()
model.train(train_feats, train_labels)

pred_y = model.predict(test_feats)
print('Ground Truth is:', test_labels)
print('Prediction is:', pred_y)
acc = accuracy(pred_y, test_labels)
print(acc)
