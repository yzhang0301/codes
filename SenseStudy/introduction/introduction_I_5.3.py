import random

x, y = load_spring_dataset()
train_x = x[:-10]
train_y = y[:-10]
test_x = x[-10:]
test_y = y[-10:]
fig() + scatter(test_x, test_y)

model = LinearRegressor(bias=False)
model.train(train_x, train_y)
weights = model.get_weights()
print(weights[0])

mse_error_list = []
step = 60
k = 0.1
learning_rate = 0.02

for i in range(step):
    index = random.randint(0, len(train_x)-1)
    x = train_x[index]
    y = train_y[index]    
    error = y - k*x   
    k = k + learning_rate * error  
    pred_y = linear_function(train_x, k, 0)
    mse_error = compute_mse(train_y, pred_y)
    mse_error_list.append(mse_error)

print(k)
fig() + line(mse_error_list)
