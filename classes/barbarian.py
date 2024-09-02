from skill import Skill
from skill_tree import Skill_Tree

# Warcries
howl = Skill("Howl", [], 1, 0)
find_potion = Skill("Find Potion", [], 1, 0)
taunt = Skill("Taunt", [howl], 6, 0)
shout = Skill("Shout", [howl], 6, 0)
find_item = Skill("Find Item", [find_potion], 12, 0)
battle_cry = Skill("Battle Cry", [taunt], 18, 0)
battle_orders = Skill("Battle Orders", [shout], 24, 0)
grim_ward = Skill("Grim Ward", [find_item], 24, 0)
war_cry = Skill("War Cry", [battle_cry, battle_orders], 30, 0)
battle_command = Skill("Battle Command", [battle_orders], 30, 0)

barbarian_warcries_tree = Skill_Tree(
    "Warcries", 
    "Barbarian", 
    [
        howl, 
        find_potion, 
        taunt, 
        shout, 
        find_item, 
        battle_cry, 
        battle_orders, 
        grim_ward, 
        war_cry, 
        battle_command
    ],
    layout=[[1,0,1],[1,1,0],[0,0,1],[1,0,0],[0,1,1],[1,1,0]]
)

# Combat Masteries
blade_mastery = Skill("Blade Mastery", [], 1, 0)
axe_mastery = Skill("Axe Mastery", [], 1, 0)
mace_mastery = Skill("Mace Mastery", [], 1, 0)
polearm_mastery = Skill("Polearm Mastery", [], 6, 0)
throwing_mastery = Skill("Throwing Mastery", [], 6, 0)
spear_mastery = Skill("Spear Mastery", [], 6, 0)
increased_stamina = Skill("Increased Stamina", [], 12, 0)
iron_skin = Skill("Iron Skin", [], 18, 0)
increased_speed = Skill("Increased Speed", [increased_stamina], 24, 0)
natural_resistance = Skill("Natural Resistance", [iron_skin], 30, 0)

barbarian_combat_masteries_tree = Skill_Tree(
    "Combat Masteries", 
    "Barbarian", 
    [
       blade_mastery, 
       axe_mastery, 
       mace_mastery, 
       polearm_mastery, 
       throwing_mastery, 
       spear_mastery, 
       increased_stamina, 
       iron_skin, 
       increased_speed, 
       natural_resistance
    ],
    layout=[[1,1,1],[1,1,1],[1,0,0],[0,0,1],[1,0,0],[0,0,1]]
)

# Combat Skills
bash = Skill("Bash", [], 1, 0)
leap = Skill("Leap", [], 6, 0)
double_swing = Skill("Double Swing", [bash], 6, 0)
stun = Skill("Stun", [bash], 12, 0)
double_throw = Skill("Double Throw", [double_swing], 12, 0)
leap_attack = Skill("Leap Attack", [leap], 18, 0)
concentrate = Skill("Concentrate", [stun], 18, 0)
frenzy = Skill("Frenzy", [double_throw], 24, 0)
whirlwind = Skill("Whirlwind", [leap_attack, concentrate], 30, 0)
berserk = Skill("Berserk", [concentrate], 30, 0)

barbarian_combat_skills_tree = Skill_Tree(
    "Combat Skills", 
    "Barbarian", 
    [
        bash, 
        leap, 
        double_swing, 
        stun, 
        double_throw, 
        leap_attack, 
        concentrate, 
        frenzy, 
        whirlwind, 
        berserk
    ],
    layout=[[0,1,0],[1,0,1],[0,1,1],[1,1,0],[0,0,1],[1,1,0]]
)
class Barbarian:
    def __init__(self, username, level = 1, strength = 30, dexterity = 20, vitality = 25, energy = 10):
        self.username = username

        self.level = level

        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

        self.skill_tree_1 = barbarian_warcries_tree
        self.skill_tree_2 = barbarian_combat_masteries_tree
        self.skill_tree_3 = barbarian_combat_skills_tree

    def __repr__(self):
        return (f"Barbarian(username={self.username!r}, "
                f"level={self.level}, "
                f"strength={self.strength}, "
                f"dexterity={self.dexterity}, "
                f"vitality={self.vitality}, "
                f"energy={self.energy}, "
                f"skill_tree_1={self.skill_tree_1!r}, "
                f"skill_tree_2={self.skill_tree_2!r}, "
                f"skill_tree_3={self.skill_tree_3!r})")
