class computer:
    def __init__(self,cpu,ram):
        self.cpu='i5555555'
        self.ram=32
    def config(self):
        print("This is my configuration",self.cpu,self.ram)

com1 = computer('i5',8)
com1.cpu= 'Rayzen3'
com1.ram= 68
com1.config()
com2 = computer('Rayzen 3',16)
com2.cpu='hello'
com2.config()