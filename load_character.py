from classes.sorceress import Sorceress
from classes.druid import Druid
from classes.amazon import Amazon
from classes.paladin import Paladin
from classes.barbarian import Barbarian
from classes.necromancer import Necromancer
from classes.assassin import Assassin

import json

def load_character(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    character_class = data["skill_trees"][0]["character_class"]

    if character_class == "Sorceress":
        character = Sorceress("username")
    if character_class == "Druid":
        character = Druid("username")
    if character_class == "Amazon":
        character = Amazon("username")
    if character_class == "Paladin":
        character = Paladin("username")
    if character_class == "Barbarian":
        character = Barbarian("username")
    if character_class == "Necromancer":
        character = Necromancer("username")
    if character_class == "Assassin":
        character = Assassin("username")

    character.username = data['username']
    character.level = data['level']
    character.strength = data['strength']
    character.dexterity = data['dexterity']
    character.vitality = data['vitality']
    character.energy = data['energy']
    
    # Loop through each skill tree and update the skill's base level
    for tree_data, skill_tree in zip(data['skill_trees'], character.skill_trees):
        for skill_data, skill in zip(tree_data['skills'], skill_tree.skills):
            skill.base_level = skill_data['base_level']
    
    print(character)
    

load_character('dru.json')