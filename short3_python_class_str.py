class Player:
    def __init__(self, name, age, position, club):
        self.name = name
        self.age = age
        self.position = position
        self.club = club

    def method1(self):
        ...

    def method2(self):
        ...
    
    def __str__(self):
        return f'{self.name}, age:{self.age}, plays as a {self.position} for {self.club}'
    

kane = Player('Harry Kane', 30, 'Forward', 'Spurs')
salah = Player('Mo Salah', 29, 'Forward', 'Liverpool')

print(kane)
print(salah)