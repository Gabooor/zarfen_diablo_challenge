from skill import Skill
from skill_tree import Skill_Tree

# Defensive Auras
prayer = Skill("Prayer", [], 1, 0)
resist_fire = Skill("Resist Fire", [], 1, 0)
defiance = Skill("Defiance", [], 6, 0)
resist_cold = Skill("Resist Cold", [], 6, 0)
cleansing = Skill("Cleansing", [prayer], 12, 0)
resist_lightning = Skill("Resist Lightning", [], 12, 0)
vigor = Skill("Vigor", [defiance, cleansing], 18, 0)
meditation = Skill("Meditation", [cleansing], 24, 0)
redemption = Skill("Redemption", [vigor], 30, 0)
salvation = Skill("Salvation", [], 30, 0)

paladin_defensive_auras_tree = Skill_Tree(
    "Defensive Auras", 
    "Paladin", 
    [
        prayer, 
        resist_fire, 
        defiance, 
        resist_cold, 
        cleansing, 
        resist_lightning, 
        vigor, 
        meditation, 
        redemption, 
        salvation
    ],
    layout=[[1,0,1],[0,1,1],[1,0,1],[0,1,0],[1,0,0],[0,1,1]]
)

# Offensive Auras
might = Skill("Might", [], 1, 0)
holy_fire = Skill("Holy Fire", [might], 6, 0)
thorns = Skill("Thorns", [], 6, 0)
blessed_aim = Skill("Blessed Aim", [might], 12, 0)
concentration = Skill("Concentration", [blessed_aim], 18, 0)
holy_freeze = Skill("Holy Freeze", [holy_fire], 18, 0)
holy_shock = Skill("Holy Shock", [holy_freeze], 24, 0)
sanctuary = Skill("Sanctuary", [thorns, holy_freeze], 24, 0)
fanaticism = Skill("Fanaticism", [concentration], 30, 0)
conviction = Skill("Conviction", [sanctuary], 30, 0)

paladin_offensive_auras_tree = Skill_Tree(
    "Offensive Auras", 
    "Paladin", 
    [
        might, 
        holy_fire, 
        thorns, 
        blessed_aim, 
        concentration, 
        holy_freeze, 
        holy_shock, 
        sanctuary, 
        fanaticism, 
        conviction
    ],
    layout=[[1,0,0],[0,1,1],[1,0,0],[1,1,0],[0,1,1],[1,0,1]]
)

# Combat Skills
sacrifice = Skill("Sacrifice", [], 1, 0)
smite = Skill("Smite", [], 1, 0)
holy_bolt = Skill("Holy Bolt", [], 6, 0)
zeal = Skill("Zeal", [sacrifice], 12, 0)
charge = Skill("Charge", [smite], 12, 0)
vengeance = Skill("Vengeance", [zeal], 18, 0)
blessed_hammer = Skill("Blessed Hammer", [holy_bolt], 18, 0)
conversion = Skill("Conversion", [vengeance], 24, 0)
holy_shield = Skill("Holy Shield", [charge, blessed_hammer], 24, 0)
fist_of_the_heavens = Skill("Fist of the Heavens", [blessed_hammer, conversion], 30, 0)

paladin_combat_skills_tree = Skill_Tree(
    "Combat Skills", 
    "Paladin", 
    [
        sacrifice, 
        smite, 
        holy_bolt, 
        zeal, 
        charge, 
        vengeance, 
        blessed_hammer, 
        conversion, 
        holy_shield, 
        fist_of_the_heavens
    ],
    layout=[[1,0,1],[0,1,0],[1,0,1],[1,1,0],[1,0,1],[0,1,0]]
)
class Paladin:
    def __init__(self, username, level = 1, strength = 25, dexterity = 20, vitality = 25, energy = 15):
        self.username = username

        self.level = level

        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

        self.skill_trees = [
            paladin_defensive_auras_tree,
            paladin_offensive_auras_tree,
            paladin_combat_skills_tree    
        ]

        self.skill_tree_dependencies = [
            [[[0, 0], [2, 0]], [[1, 1], [3, 1]], [[2, 0], [3, 1]], [[2, 0], [4, 0]], [[3, 1], [5, 1]]], 
            [[[0, 0], [1, 1]], [[0, 0], [2, 0]], [[1, 1], [3, 1]], [[1, 2], [4, 2]], [[2, 0], [3, 0]], [[3, 0], [5, 0]], [[3, 1], [4, 1]], [[3, 1], [4, 2]], [[4, 2], [5, 2]]], 
            [[[0, 0], [2, 0]], [[0, 2], [2, 2]], [[1, 1], [3, 1]], [[2, 0], [3, 0]], [[2, 2], [4, 2]], [[3, 0], [4, 0]], [[3, 1], [4, 2]], [[3, 1], [5, 1]],[[4, 0], [5, 1]]]
        ]

    def __repr__(self):
        return (f"Paladin(username={self.username!r}, "
                f"level={self.level}, "
                f"strength={self.strength}, "
                f"dexterity={self.dexterity}, "
                f"vitality={self.vitality}, "
                f"energy={self.energy}, "
                f"skill_tree_1={self.skill_tree_1!r}, "
                f"skill_tree_2={self.skill_tree_2!r}, "
                f"skill_tree_3={self.skill_tree_3!r})")
