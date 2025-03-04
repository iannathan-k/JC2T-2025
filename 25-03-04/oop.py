class Car: 
    # Constructor - A special function which allows you to construct personalized objects during instantiation
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("The car goes vroom")
    
    def stop(self):
        print("The car goes skrrrt")

car1 = Car("Toyota", "2001", "Red")
car1.start()
car1.stop()