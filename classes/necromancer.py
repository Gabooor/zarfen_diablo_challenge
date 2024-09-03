from skill import Skill
from skill_tree import Skill_Tree

# Summoning
raise_skeleton = Skill("Raise Skeleton", [], 1, 0)
skeleton_mastery = Skill("Skeleton Mastery", [raise_skeleton], 1, 0)
clay_golem = Skill("Clay Golem", [], 6, 0)
golem_mastery = Skill("Golem Mastery", [clay_golem], 12, 0)
raise_skeletal_mage = Skill("Raise Skeletal Mage", [raise_skeleton], 12, 0)
blood_golem = Skill("Blood Golem", [clay_golem], 18, 0)
summon_resist = Skill("Summon Resist", [golem_mastery], 24, 0)
iron_golem = Skill("Iron Golem", [blood_golem], 24, 0)
fire_golem = Skill("Fire Golem", [iron_golem], 30, 0)
revive = Skill("Revive", [raise_skeletal_mage, iron_golem], 30, 0)


necromancer_summoning_tree = Skill_Tree(
    "Summoning", 
    "Necromancer", 
    [
        skeleton_mastery,  
        raise_skeleton, 
        clay_golem, 
        golem_mastery, 
        raise_skeletal_mage, 
        blood_golem, 
        summon_resist, 
        iron_golem, 
        fire_golem, 
        revive
    ],
    layout=[[1,0,1],[0,1,0],[1,0,1],[0,1,0],[1,1,0],[0,1,1]]
)

# Poison and Bone
teeth = Skill("Teeth", [], 1, 0)
bone_armor = Skill("Bone Armor", [], 1, 0)
poison_dagger = Skill("Poison Dagger", [], 6, 0)
corpse_explosion = Skill("Corpse Explosion", [teeth], 6, 0)
bone_wall = Skill("Bone Wall", [bone_armor], 12, 0)
poison_explosion = Skill("Poison Explosion", [poison_dagger, corpse_explosion], 18, 0)
bone_spear = Skill("Bone Spear", [corpse_explosion], 18, 0)
bone_prison = Skill("Bone Prison", [bone_wall, bone_spear], 24, 0)
poison_nova = Skill("Poison Nova", [poison_explosion], 30, 0)
bone_spirit = Skill("Bone Spirit", [bone_spear], 30, 0)

necromancer_poison_and_bone_tree = Skill_Tree(
    "Poison and Bone", 
    "Necromancer", 
    [
        teeth,  
        bone_armor, 
        poison_dagger, 
        corpse_explosion, 
        bone_wall, 
        poison_explosion, 
        bone_spear, 
        bone_prison, 
        poison_nova, 
        bone_spirit
    ],
    layout=[[0,1,1],[1,1,0],[0,0,1],[1,1,0],[0,0,1],[1,1,0]]
)

# Curses
amplify_damage = Skill("Amplify Damage", [], 1, 0)
dim_vision = Skill("Dim Vision", [], 6, 0)
weaken = Skill("Weaken", [amplify_damage], 6, 0)
iron_maiden = Skill("Iron Maiden", [amplify_damage], 12, 0)
terror = Skill("Terror", [weaken], 12, 0)
confuse = Skill("Confuse", [dim_vision], 18, 0)
life_tap = Skill("Life Tap", [iron_maiden], 18, 0)
attract = Skill("Attract", [confuse], 24, 0)
decrepify = Skill("Decrepify", [terror], 24, 0)
lower_resist = Skill("Lower Resist", [life_tap, terror], 30, 0)


necromnacer_curses_tree = Skill_Tree(
    "Curses", 
    "Necromancer", 
    [
        amplify_damage, 
        dim_vision, 
        weaken, 
        iron_maiden, 
        terror, 
        confuse, 
        life_tap, 
        attract, 
        decrepify, 
        lower_resist
    ],
    layout=[[0,1,0],[1,0,1],[0,1,1],[1,1,0],[1,0,1],[0,1,0]]
)
class Necromancer:
    def __init__(self, username, level = 1, strength = 15, dexterity = 25, vitality = 15, energy = 25):
        self.username = username

        self.level = level

        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

        self.skill_tree_1 = necromancer_summoning_tree
        self.skill_tree_2 = necromancer_poison_and_bone_tree
        self.skill_tree_3 = necromnacer_curses_tree

    def __repr__(self):
        return (f"Necromancer(username={self.username!r}, "
                f"level={self.level}, "
                f"strength={self.strength}, "
                f"dexterity={self.dexterity}, "
                f"vitality={self.vitality}, "
                f"energy={self.energy}, "
                f"skill_tree_1={self.skill_tree_1!r}, "
                f"skill_tree_2={self.skill_tree_2!r}, "
                f"skill_tree_3={self.skill_tree_3!r})")
