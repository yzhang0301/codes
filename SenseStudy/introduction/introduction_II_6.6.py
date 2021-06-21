diff_level = load_private("diff_level")
texts1, grades1 = load_engtext(subset='rdtrain')
texts2, grades2 = load_engtext(subset='rdtest')

features = []
labels = []

def get_feats_labels(article_list, grade_list, diff_level):
    features = []
    labels = []
    for text, grade in zip(article_list, grade_list):
        features.append(get_freq_per_grade(text, diff_level))
        labels.append(grade)
    return features, labels

train_feats, train_labels = get_feats_labels(texts1, grades1, diff_level)
print(train_feats[0:5])
print(train_labels[0:5])
save_private([train_feats, train_labels], "train_features")

test_feats, test_labels = get_feats_labels(texts2, grades2, diff_level)
print(test_feats[0:5])
print(test_labels[0:5])
save_private([test_feats, test_labels], "test_features")
