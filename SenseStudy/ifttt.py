import requests

#img = load_image('example.jpg')
img = load_image_url('http://sensestudy-server/api/resource/public/accountstorage-objs/18ff97da-ead9-439d-82b5-deebcc29502a/zy1.jpeg')
imshow(img)
detector = get_emotion_recognizer()
res = recognize_emotion(detector, img)
print(res)

url = 'https://maker.ifttt.com/trigger/happy_or_sad/with/key/dof684nStwOEkDTj5ffSAc'
value = {'value1': res}
x = requests.post(url, data = value)
print(x)
