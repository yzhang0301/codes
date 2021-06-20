X, y = load_diamond(mission='regressor', color='E', clarity='SI1', cut='Ideal')
X, y = shuffle(X, y)
size = len(X)
print("数据集大小为: %d" % size)
x_try = X[-10:]
y_try = y[-10:]
fig() + scatter(x_try, y_try)

x_5 = x_try[4]
y_5 = y_try[4]
k = y_5/x_5
print("k=",k)

pred_y = linear_function(x_try, k, 0)

fig() + scatter(x_try, y_try) + scatter(x_try, pred_y) + line(x_try[:], pred_y[:], 'r')

model = LinearRegressor()
model.train(x_try, y_try)
model.show()

weights = model.get_weights()
print(weights)
k = weights[0]
b = weights[1]
print("k=",k)
print("b=",b)
