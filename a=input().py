class Player:
    health = 0
    revives =3


def revive(self):
    
      if self.health > 0:
         print("Player has health , they do not need to be revieved!")
         return
      elif self.revives <= 3:
         print("This player is out of revives")
         return
      self.revives =self.revives - 1
      self.health = 10

revive(Player)