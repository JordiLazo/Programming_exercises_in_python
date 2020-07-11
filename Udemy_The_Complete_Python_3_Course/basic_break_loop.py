import random

playerhp = 260
enemy_attack_low = 60
enemy_attack_high = 80
print("You begin with 260HP.")
while playerhp > 0:
    damage = random.randrange(enemy_attack_low, enemy_attack_high)
    playerhp = playerhp - damage
    print("Damage taken", damage, "HP right now", playerhp)