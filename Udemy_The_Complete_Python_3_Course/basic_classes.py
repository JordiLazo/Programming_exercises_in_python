class Enemy:
    
    hp = 200
    def __init__(self, attack_low, attack_high):
        self.attack_low = attack_low
        self.attack_high = attack_high
        

    def getAtk(self):
        print("low attack is ",self.attack_low)
        print("high attack is ",self.attack_high)

    def gethp(self):
        print("Hp is",self.hp)

enemy1 = Enemy(40,49).getAtk()
enemy2 = Enemy(75,90)
enemy2.getAtk()
enemy2.gethp()
