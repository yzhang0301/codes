train_x = [60,56,60,55,60,57,65,60,62,59,43,52,41,45,43,50,46,52,56,56]
train_y = [1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]
def h_function(x, k, b):
    res = (x * k + b) / 6.0 + 0.5
    return bound(res, 0, 1)

acc_list = []

step = 400
k = 0.1
b = -0.5
learning_rate = 0.0001

for i in range(step):
    index = i % len(train_x)
    x = train_x[index]
    y = train_y[index]
    h = h_function(x, k, b)
    error = y - h
    k = k + learning_rate * error * x
    b = b + learning_rate * error
    
    acc = linear_accuracy(train_x, train_y, k, b)
    acc_list.append(acc)
    
    if acc > 0.8:
        break

print("k=",k)
print("b=",b)
fig() + line(acc_list)

model = LogisticRegressor()
model.train(train_x, train_y)
weights = model.get_weights()
print(weights)
model.show()

y1 = linear_function(train_x, k, b)
y2 = linear_function(train_x, weights[0], weights[1])
fig() + scatter(train_x, train_y) + line(train_x[:], y1[:], 'r') + line(train_x[:], y2[:], 'b')
