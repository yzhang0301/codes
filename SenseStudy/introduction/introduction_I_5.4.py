def train_by_size(train_x, train_y, train_size):
    model = LinearRegressor()
    model.train(train_x[:train_size], train_y[:train_size])
    weights = model.get_weights()
    k = weights[0]
    b = weights[1]
    return model, k, b

X, y = load_diamond(mission='regressor', color='E', clarity='SI1', cut='Ideal')
X, y = shuffle(X, y)
size = len(X)
print("数据集大小为: %d" % size)
train_x = X[:-10]
train_y = y[:-10]
test_x = X[-10:]
test_y = y[-10:]

x_try = X[:10]
y_try = y[:10]
fig() + scatter(x_try, y_try)
model = LinearRegressor()
model.train(x_try, y_try)
model.show()

y_try[8] = 300000
fig() + scatter(x_try, y_try)
model = LinearRegressor()
model.train(x_try, y_try)
model.show()

size = [10, 100, 300, 400, 500, 600]
for train_size in size:
    model, k, b = train_by_size(train_x, train_y, train_size)
    result = model.predict(train_x[:train_size])
    mse_loss = compute_mse(train_y[:train_size], result)
    fig() + scatter(train_x[:train_size], train_y[:train_size]) + line(train_x[:train_size], result, 'r')+title('train_size:%d mse_loss:%f k:%f b:%f'%(train_size, mse_loss, k, b))
    print("train_mse:", mse_loss)
    result = model.predict(test_x)
    mse_loss = compute_mse(test_y, result)
    print("test_mse:", mse_loss)
