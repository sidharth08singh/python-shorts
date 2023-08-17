# https://www.youtube.com/shorts/WO4W8F5oC0s
class Player:
    def __init__(self, name: str):
        self.name = name
    
    # def __str__(self) -> str:
    #     return f'Player: {self.name}'

    def __repr__(self) -> str:
        return object.__repr__(self)
    
player1 = Player('Haaland')
print(player1)