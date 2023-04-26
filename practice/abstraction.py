from abc import ABC, abstractmethod
class dog(ABC):
    def care(self, times):
        print("you should take your dog to the vet every: ",times)

    @abstractmethod
    def appointments(self,times):
        pass

class vet(dog):
    def appointments(self,times):
        print('you have taken your dog to the vet {} times.'.format(times))

obj = vet()
obj.care("year")
obj.appointments("2")
        
