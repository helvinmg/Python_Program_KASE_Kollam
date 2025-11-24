class Animal:
    def __init__(self,sound):
        self.sound=sound
    def talk(self):
        print(self.sound*3)

dog=Animal("bow")
cat=Animal("meow")
dog.talk()
cat.talk()
    
