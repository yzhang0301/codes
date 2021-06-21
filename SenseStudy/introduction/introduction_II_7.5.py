import numpy as np
net = load_model(MODEL_PATH)
img = Image.open(DATA_PATH+'/5/1.jpg')
array = np.array(img) 
show_img(array)

size = 250

imgs = []
for i in range(0,img.size[0]-size,10):
    for j in range(0,img.size[1]-size,10):
        img_crop = img.crop((i,j,i+size,j+size))
        b = transfer(img_crop)
        b = b.unsqueeze(0)
        predicted = deep_predict(net,b)
        if predicted:
            imgs.append(img_crop)
            
print(len(imgs))

for i in range(len(imgs)-1):
    array = np.array(imgs[i])
    show_img(array)
