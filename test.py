
class Game:
    var1 = 'Hello'
    var2 = 'world'

class organism:
    name = 'unknown'
    specices ='unknown'
    legs = 0
    arms = None
    dna = 'some'
    origin = 'unknown'
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.specices,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
class Human(organism):
    name = 'unknown'
    species = 'human'
    legs = 2
    arms = 2
    origin = 'earth'

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using paper clips"
        return msg

class Dog(organism):
    name = 'unknown'
    specices ='unknown'
    legs = 4
    arms = None
    dna = 'dog'
    origin = 'earth'

    def bit(self):
        msg = "\nEmits a loug growl and is large"
        return msg

class bacterium(organism):
    name = 'unknown'
    specices ='unknown'
    legs = None
    arms = None
    dna = 'unknown'
    origin = 'mars'

    def replication(self):
        msg = "\nthe cell begins to divide"
        return msg
    





if __name__=="__main__":
    x = Game()
    print("{} {}".format(x.var1,x.var2))
    
    human= Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacteria = bacterium()
    print(bacteria.information())
    print(bacteria.replication())


    
