train_x, train_y = load_gender()
model = LogisticRegressor()
model.train(train_x, train_y)
model.show()

x = 40
pred_y = model.predict(x)
print(pred_y)

weights = model.get_weights()
print(weights)
k = weights[0]
b = weights[1]
print("k=",k)
print("b=",b)

model2 = LinearRegressor()
model2.train(train_x, train_y)
model2.show()
