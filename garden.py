import json
import os
import random

from flowers import (
    COMMON,
    UNCOMMON,
    RARE,
    EPIC,
    LEGENDARY
)

from rewards import XP_VALUES

FILE_NAME = "garden.json"

def load_facts():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
def save_facts(facts):
    with open(FILE_NAME, "w") as file:
        json.dump(facts, file, indent=4)

def get_random_flower():
    roll = random.randint(1, 100)

    if roll <= 60:
        rarity = "Common"
        flower = random.choice(COMMON)

    elif roll <= 85:
        rarity = "Uncommon"
        flower = random.choice(UNCOMMON)

    elif roll <= 95:
        rarity = "Rare"
        flower = random.choice(RARE)

    elif roll <= 99:
        rarity = "Epic"
        flower = random.choice(EPIC)

    else:
        rarity = "Legendary"
        flower = random.choice(LEGENDARY)

    return flower, rarity
def add_fact():
    fact = input("What did you learn today?\n> ")

    flower, rarity = get_random_flower()

    xp = XP_VALUES[rarity]

    facts = load_facts()

    facts.append({
        "fact": fact,
        "flower": flower,
        "rarity": rarity,
        "xp" : xp
    })

    save_facts(facts)

    print(f"\n✨ {rarity} Flower Bloomed!")
    print(f"{flower}")
    print(f"+{xp} XP")
    print("\nAdded to garden.")

def view_garden():
    facts = load_facts()

    if not facts:
        print("\n🌱 Your garden is empty.")
        return

    total_xp = get_total_xp()
    level = get_level(total_xp)

    print("\n🌸 YOUR GARDEN 🌸\n")
    print(f"Level: {level}")
    print(f"XP: {total_xp}")
    print(f"Flowers: {len(facts)}\n")

    for entry in facts:
        print(f"{entry['flower']} [{entry['rarity']}]")
        print(f"   {entry['fact']}")
        print()

def get_total_xp():
    facts = load_facts()

    total_xp = 0

    for entry in facts:
        total_xp += entry.get("xp", 0)

    return total_xp

def get_level(total_xp):
    if total_xp < 100:
        return 1
    elif total_xp < 250:
        return 2
    elif total_xp < 500:
        return 3
    elif total_xp < 1000:
        return 4
    else:
        return 5

while True:
    print("\n🌸 KNOWLEDGE GARDEN 🌸")
    print("1. Add Fact")
    print("2. View Garden")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_fact()

    elif choice == "2":
        view_garden()

    elif choice == "3":
        print("\nGoodbye! 🌷")
        break

    else:
        print("\nPlease enter 1, 2, or 3.")