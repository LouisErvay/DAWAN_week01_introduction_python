class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def emettre_son(self):
        print(f"{self.name} émet un son")


class Lion(Animal):

    def __init__(self, name, age, son):
        super().__init__(name, age)
        self.son = son

    def emettre_son(self):
        print(f"{self.name} {self.son}")

a = Animal('animal', 20)
a.emettre_son()

l = Lion(name='lion', age=20, son='rugit')
l.emettre_son()