class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname=surname
        self.age=age
    def edication(self):
        return f'{self.name} - {self.surname} - {self.age}'
    def isswimming(self):
        result = None
        if self.age < 15:
            result = f'{self.name} - умееть плавать'
        else:
            result= f'{self.name} - не умеет плавать'
        return result
adxam = Person(name='adxam',surname='kazakbaev',age=15)
print(f'(The person is {adxam.edication()} u {adxam.isswimming()}')
ernazar= Person(name='adxam',surname='Jumaniyazov',age=15)
print(f'(The person is {ernazar.edication()} u {ernazar.isswimming()}')
alibek = Person(name='adxam',surname='Djoldasov',age=15)
print(f'(The person is {alibek.edication()} u {alibek.isswimming()}')