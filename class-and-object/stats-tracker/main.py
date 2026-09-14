class GameCharacter:
    def __init__(self,name):
        self._name = name
        self.health = 100
        self._mana = 50
        self._level = 1
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, points):
        if points < 0: 
            self._health = 0

        elif points > 100:
            self._health = 100
        else:
            self._health = points
    @property      
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, points):
        if points < 0:
            self._mana = 0
        elif points > 50:
            self._mana = 50
        else:
            self._mana = points
            
    @property
    def level(self):
        return self._level
    def level_up(self):
        self._level += 1
        self.mana = 50
        self.health = 100
        print(f"{self.name} leveled up to {self.level}!")
    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"


npc = GameCharacter("kratos")
print(npc.mana)
npc.mana -= 20
print(npc.mana)
npc.level_up()
print(npc.mana)
print(npc)