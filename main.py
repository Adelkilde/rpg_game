import random
import time


characters = {
    "Warrior": {"HP": 20, "Attack": 6},
    "Mage": {"HP": 15, "Attack": 8},
    "Rogue": {"HP": 18, "Attack": 7}
}

enemies = [
    {"name": "Goblin", "HP": 10, "Attack": 4},
    {"name": "Orc", "HP": 14, "Attack": 5}
]


print("Welcome to the Mini RPG Game!")
print("Choose your character:")
for i, char in enumerate(characters.keys(), 1):
    print(f"{i}. {char}")


while True:
    try:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= len(characters):
            break
        else:
            print("Please choose a valid number.")
    except ValueError:
        print("Enter a number, not text!")

character_name = list(characters.keys())[choice - 1]
player = characters[character_name]
print(f"\nYou chose: {character_name}")
print(f"Stats: HP = {player['HP']}, Attack = {player['Attack']}")
time.sleep(1)

print("\nYou enter a dark forest where monsters lurk...")
time.sleep(2)


for enemy in enemies:
    print(f"\nA wild {enemy['name']} appears!")
    enemy_hp = enemy["HP"]

    while enemy_hp > 0 and player["HP"] > 0:
        input("Press Enter to attack...")
        player_damage = random.randint(1, player["Attack"])
        enemy_hp -= player_damage
        print(f"You hit the {enemy['name']} for {player_damage} damage!")

        if enemy_hp <= 0:
            print(f"The {enemy['name']} is defeated!")
            break

        enemy_damage = random.randint(1, enemy["Attack"])
        player["HP"] -= enemy_damage
        print(f"The {enemy['name']} hits you for {enemy_damage} damage!")

        if player["HP"] <= 0:
            print("You have been defeated... Game Over.")
            exit()

    time.sleep(1)


print("\nCongratulations! You defeated all the monsters!")
print("Thanks for playing!")
