trainloader,testloader = load_deep_data(DATA_PATH)
net = LeNet()
train_deep_net(trainloader,testloader,net,max_epoch = 8)

for i in range(20):
    test_img = get_test_img(DATA_PATH,i)
    show_deep_img(test_img)
    result = deep_predict(net,test_img)
    print(result)
