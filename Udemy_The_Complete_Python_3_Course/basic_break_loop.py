import random

playerhp = 260
enemy_attack_low = 60
enemy_attack_high = 80
print("You begin with 260HP.")

while playerhp > 0:
    damage = random.randrange(enemy_attack_low, enemy_attack_high)
    playerhp = playerhp - damage

    if playerhp <= 30:
        playerhp = 30

    print("Damage taken", damage, "HP right now", playerhp)

    if playerhp == 30:
        print("You have low health. You've been teleported to the nearest inn.")
        break
    