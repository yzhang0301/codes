X, y = load_diamond(mission='regressor', color='E', clarity='SI1', cut='Ideal')
X, y = shuffle(X, y)

train_x = X[:-10]
train_y = y[:-10]
test_x = X[-10:]
test_y = y[-10:]

fig() + scatter(test_x, test_y)

x_100 = train_x[99]
y_100 = train_y[99]
k1 = y_100 / x_100
print(k1)
pred_model1 = linear_function(test_x, k1, 0)
fig() + scatter(test_x, test_y) + scatter(test_x, pred_model1) + line(test_x[:], pred_model1[:], 'r')
MSE = compute_mse(test_y, pred_model1)
print("模型 1 在测试集上的MSE：%f"%MSE)

x_200 = train_x[199]
y_200 = train_y[199]
k2 = y_200 / x_200
print(k2)
pred_model2 = linear_function(test_x, k2, 0)
fig() + scatter(test_x, test_y) + scatter(test_x, pred_model2) + line(test_x[:], pred_model2[:], 'r')
MSE = compute_mse(test_y, pred_model2)
print("模型 2 在测试集上的MSE：%f"%MSE)

model = LinearRegressor()
model.train(train_x, train_y)
pred_model3 = model.predict(test_x)
fig() + scatter(test_x, test_y) + scatter(test_x, pred_model3) + line(test_x[:], pred_model3[:], 'r')
MSE = compute_mse(test_y, pred_model3)
print("模型3在测试集上的MSE：%f"%MSE)

model = LinearRegressor()
model.train(train_x, train_y)
pred_y = model.predict(train_x)
MSE = compute_mse(train_y, pred_y)
print("模型3在训练集上的MSE：%f"%MSE)

model.show()
