class dogs:
    def __init__(self):
        self.__breed='borderCollie'
        self.__age= 3
        self._name = 'Bailey'

    def getbreed(self):
        print(self.__breed)

    def setage(self, age):
        self.__age = age

    def getage(self):
        print(self.__age)
   

    def getname(self):
        print(self._name)

obj = dogs()
obj.getbreed()
obj.getage()
obj.setage(4)
obj.getage()
obj.getname()
        
