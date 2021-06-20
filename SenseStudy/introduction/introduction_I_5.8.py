class Dog():
    def __init__(self, tall, sound, old):
        self.tall = tall
        self.sound = sound
        self.old = old
        self.__owner = "sense"
    def callout(self):
        print(self.sound,self.sound)
    def run(self):
        print("run run run……")
    def get_owner(self):
        print("my owner is: %s"%self.__owner)

taidi = Dog(28, "汪汪", 2)
print("泰迪的肩高：", taidi.tall)
print("泰迪的叫声：",  taidi.sound)
taidi.callout()
taidi.run()

hashiqi = Dog(80, "嗷嗷", 3)
hashiqi.callout()
hashiqi.run()
hashiqi.get_owner()

class Linear_Classify():
    def __init__(self, x, y, test_size):
        self.train_x = x[:-test_size]
        self.train_y = y[:-test_size]
        self.test_x = x[-test_size:]
        self.test_y = y[-test_size:]
        self.model = LogisticRegressor()
        
    def show_classify(self):
        self.model.show()

    def train_model(self):
        self.model.train(self.train_x, self.train_y)
        
    def predict_model(self):
        pred_y = self.model.predict(self.test_x)
        return pred_y

X, y = load_diamond(mission='classify')
diamond_class = Linear_Classify(X, y, 10)
diamond_class.train_model()
diamond_class.predict_model()
diamond_class.show_classify()
