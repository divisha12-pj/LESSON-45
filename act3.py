class parrot:
    species="bird"

    def __init__(self,name,age):
      self.name=name
      self.age=age

p1=parrot("Blu",10)
print(" I am a",p1.species)
print("my name is {} and i am {} years old".format(p1.name,p1.age))

p2=parrot("bella",11)
print(" I am a",p2.species)
print("my name is{} and i am {} years old".format(p2.name,p2.age))