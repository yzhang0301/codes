train_x, train_y = load_gender()
model = LogisticRegressor()
model.train(train_x, train_y)
model.show()

acc = model.score(metric="accuracy")
print("模型准确率：%f"%acc)
presis = model.score(metric="presision")
print("模型查准率：%f"%presis)
rec= model.score(metric="recall")
print("模型召回率：%f"%rec)

X, y = load_diamond(mission='classify')
train_x = X[:-10]
train_y = y[:-10]
test_x = X[-10:]
test_y = y[-10:]

model = LogisticRegressor()
model.train(train_x, train_y)
model.show()

acc = model.accuracy()
print("模型准确率：%f"%acc)
presis = model.presision()
print("模型查准率：%f"%presis)
rec = model.recall()
print("模型召回率：%f"%rec)

pred_y = model.predict(test_x)
acc = accuracy(test_y, pred_y)
print("模型在测试集上的准确率：%f"%acc)
presis = presision(test_y, pred_y)
print("模型在测试集上的查准率：%f"%presis)
rec = recall(test_y, pred_y)
print("模型在测试集召回率：%f"%rec)
