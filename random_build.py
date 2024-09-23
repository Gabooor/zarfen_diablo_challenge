from classes.amazon import Amazon
from classes.sorceress import Sorceress
from classes.druid import Druid

import random

def write_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content + '\n')

def level_up(character):
    # --- Increase player level --- #
    character.level += 1

    # --- 5 random stat points' allocation --- #
    # List of stat names for easier reference
    stat_names = ['strength', 'dexterity', 'vitality', 'energy']
    
    # Initialize points distribution dictionary
    points_distribution = {stat: 0 for stat in stat_names}
    
    # Randomly distribute 5 points
    for _ in range(5):
        chosen_stat = random.choice(stat_names)
        points_distribution[chosen_stat] += 1

    # Update the character's attributes
    for stat, points in points_distribution.items():
        if points > 0:
            setattr(character, stat, getattr(character, stat) + points)
    

    # --- 1 random skill point's allocation --- #
    # 1. collect possible skills based on level: if player_level >= skill.required_level + skill.base_level
    # 2. check pre reqs for each possible skill - if any pre req's base level is 0, remove it from possible skills
    # 3. check if skill's base level is 20

    available_skills = []

    # skill_trees = [character.skill_trees[0], character.skill_trees[1], character.skill_trees[2]]

    # Get every skill that is available based on the character level vs the skill's level requirement. If player_level >= skill.required_level + skill.base_level, it is available.
    temp_skill_list = []
    for skill_tree in character.skill_trees:
        for skill in skill_tree.skills:
            if character.level >= skill.required_level + skill.base_level:
                temp_skill_list.append(skill)
    available_skills = temp_skill_list

    # Get every skill that is available based on pre requisites. If the skill has a pre requisite that is not yet unlocked, it is not available yet.
    temp_skill_list = []
    for skill in available_skills:
        if len(skill.prerequisites) == 0:
            temp_skill_list.append(skill)
        else:
            available = True
            for prereq_skill in skill.prerequisites:
                if prereq_skill.base_level == 0:
                    available = False
            if available == True:
                temp_skill_list.append(skill)

    available_skills = temp_skill_list
    
    # Get every skill that is available based on skill level. If the skill's base_level is below 20, it is available.
    temp_skill_list = []
    for skill in available_skills:
        if skill.base_level < 20:
            temp_skill_list.append(skill)
    available_skills = temp_skill_list



    # for available_skill in available_skills:
    #     print(available_skill)
    chosen_skill = random.choice(available_skills)

    for skill_tree in character.skill_trees:
        for skill in skill_tree.skills:
            if skill.name == chosen_skill.name:
                skill.base_level += 1

    return points_distribution, chosen_skill
    
mayazon = Druid("Mayazon")
# print(amazon.skill_tree_3.name)
# for skill in amazon.skill_tree_3.skills:
#     print(f"{skill.name}: {len(skill.prerequisites)}")
# # print(mayazon)
# for i in range(25):
#     stats_to_upgrade, skill_to_upgrade = level_up(mayazon)
    
#     content = (f"-----------------------------------------------------------------------------\n"
#                f"Stat and skill distribution for level {mayazon.level}\n"
#                f"Stats to upgrade: {stats_to_upgrade}\n"
#                f"Skill to upgrade: {skill_to_upgrade}\n"
#                f"---------------- Current skill setup ----------------\n")
    
#     # Add the skill information
#     for skill in mayazon.skill_tree_1.skills:
#         content += f"{skill.name}: {skill.base_level}\n"
#     for skill in mayazon.skill_tree_2.skills:
#         content += f"{skill.name}: {skill.base_level}\n"
#     for skill in mayazon.skill_tree_3.skills:
#         content += f"{skill.name}: {skill.base_level}\n"

#     content += f"{mayazon.strength}|{mayazon.dexterity}|{mayazon.vitality}|{mayazon.energy}\n"
    
#     content += (f"-----------------------------------------------------------------------------")
    
#     # Write to the file
#     write_to_file('amazon_log.txt', content)


open("log.txt", 'w')

for i in range(99):
    stats_to_upgrade, skill_to_upgrade = level_up(mayazon)
    content = (f"Level {mayazon.level}: Skill to upgrade: {skill_to_upgrade}")
    
    write_to_file('log.txt', content)
