x = [1,2,3,4,5]
y = [4,8,12,16,20]
fig() + scatter(x, y) + line(x[:], y[:], 'r')

k = (y[3] - y[1]) / (x[3] - x[1])
b = y[1] - k * x[1]
x_test = [3.5, 4.5]
y_pred = linear_function(x_test, k, b)
print(y_pred)
y_test = [14, 19]
print(compute_mse(y_pred.tolist(), y_test))

model = LinearRegressor()
model.train(x, y)
model.show()
weights = model.get_weights()
print(weights[0], weights[1])
y_pred = model.predict(x_test)
print(y_pred)

#-----------------------------------------------------

x = [1,2,3,4,5]
y = [4,9,11.5,16.5,19]
fig() + scatter(x, y)

k = (y[3] - y[1]) / (x[3] - x[1])
b = y[1] - k * x[1]
x_test = [3.5, 4.5]
y_pred = linear_function(x_test, k, b)
print(y_pred)
y_test = [14, 18]
print(compute_mse(y_pred.tolist(), y_test))

model = LinearRegressor()
model.train(x, y)
model.show()
weights = model.get_weights()
print(weights[0], weights[1])
y_pred = model.predict(x_test)
print(y_pred)
print(compute_mse(y_pred, y_test))


# Over-fitting
train_x = [1, 2, 5]
train_y = [1, 4, 25]
test_x = 3
test_y = 12

model = LinearRegressor()
model.train(train_x, train_y)
model.show()
pred_y = model.predict(train_x)
print("If using linear model, the mse on training data is:", compute_mse(pred_y, train_y))
pred_y = model.predict(test_x)
print("The predicted value is:", pred_y)
print("The mse on testing data is:", (pred_y - test_y)**2)

print("If using 2nd-order polynomial model, the mse on training data is 0")
print("The predicted value is:", test_x**2)
print("The mse on testing data is", (test_x**2 - test_y)**2)
