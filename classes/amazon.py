from skill import Skill
from skill_tree import Skill_Tree

# Javelin and Spear
jab = Skill("Jab", [], 1, 0)
power_strike = Skill("Power Strike", [jab], 6, 0)
poison_javelin = Skill("Poison Javelin", [], 6, 0)
impale = Skill("Impale", [jab], 12, 0)
lightning_bolt = Skill("Lightning Bolt", [poison_javelin], 12, 0)
charged_strike = Skill("Charged Strike", [power_strike, poison_javelin], 18, 0)
plague_javelin = Skill("Plague Javelin", [lightning_bolt], 18, 0)
fend = Skill("Fend", [impale], 24, 0)
lightning_strike = Skill("Lightning Strike", [charged_strike], 30, 0)
lightning_fury = Skill("Lightning Fury", [plague_javelin], 30, 0)

amazon_javelin_and_spear_tree = Skill_Tree(
    "Javelin and Spear", 
    "Amazon", 
    [
        jab, 
        power_strike, 
        poison_javelin, 
        impale, 
        lightning_bolt, 
        charged_strike, 
        plague_javelin, 
        fend, 
        lightning_strike, 
        lightning_fury
    ],
    layout=[[1,0,0],[0,1,1],[1,0,1],[0,1,1],[1,0,0],[0,1,1]]
)

# Passive and Magic
inner_sight = Skill("Inner Sight", [], 1, 0)
critical_strike = Skill("Critical Strike", [], 1, 0)
dodge = Skill("Dodge", [], 6, 0)
slow_missiles = Skill("Slow Missiles", [inner_sight], 12, 0)
avoid = Skill("Avoid", [dodge], 12, 0)
penetrate = Skill("Penetrate", [critical_strike, poison_javelin], 18, 0)
decoy = Skill("Decoy", [slow_missiles], 24, 0)
evade = Skill("Evade", [avoid], 24, 0)
valkyrie = Skill("Valkyrie", [decoy], 30, 0)
pierce = Skill("Pierce", [penetrate], 30, 0)

amazon_passive_and_magic_tree = Skill_Tree(
    "Passive and Magic", 
    "Amazon", 
    [
        inner_sight, 
        critical_strike, 
        dodge, 
        slow_missiles, 
        avoid, 
        penetrate, 
        decoy, 
        evade, 
        valkyrie, 
        pierce
    ],
    layout=[[1,0,1],[0,1,0],[1,1,0],[0,0,1],[1,1,0],[1,0,1]]
)

# Bow and Crossbow
magic_arrow = Skill("Magic Arrow", [], 1, 0)
fire_arrow = Skill("Fire Arrow", [], 1, 0)
cold_arrow = Skill("Cold Arrow", [], 6, 0)
multiple_shot = Skill("Multiple Shot", [magic_arrow], 6, 0)
exploding_arrow = Skill("Exploding Arrow", [fire_arrow, multiple_shot], 12, 0)
ice_arrow = Skill("Ice Arrow", [cold_arrow], 18, 0)
guided_arrow = Skill("Guided Arrow", [cold_arrow, multiple_shot], 18, 0)
strafe = Skill("Strafe", [guided_arrow], 24, 0)
immolation_arrow = Skill("Immolation Arrow", [exploding_arrow], 24, 0)
freezing_arrow = Skill("Freezing Arrow", [ice_arrow], 30, 0)
amazon_bow_and_crossbow_tree = Skill_Tree(
    "Bow and Crossbow", 
    "Amazon", 
    [
        magic_arrow, 
        fire_arrow, 
        cold_arrow, 
        multiple_shot, 
        exploding_arrow, 
        ice_arrow, 
        guided_arrow, 
        strafe, 
        immolation_arrow, 
        freezing_arrow
    ],
    layout=[[0,1,1],[1,1,0],[0,0,1],[1,1,0],[0,1,1],[1,0,0]]
)
class Amazon:
    def __init__(self, username, level = 1, strength = 20, dexterity = 25, vitality = 20, energy = 15):
        self.username = username

        self.level = level

        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

        self.skill_trees = [
            amazon_javelin_and_spear_tree,
            amazon_passive_and_magic_tree,
            amazon_bow_and_crossbow_tree    
        ]

        self.skill_tree_dependencies = [
            [[[0, 0], [1, 1]], [[0, 0], [2, 0]], [[1, 1], [3, 1]], [[1, 2], [2, 2]], [[2, 0], [4, 0]], [[2, 2], [3, 1]], [[2, 2], [3, 2]], [[3, 1], [5, 1]], [[3, 2], [5, 2]]],
            [[[0, 0], [2, 0]], [[0, 2], [3, 2]], [[1, 1], [2, 1]], [[2, 0], [4, 0]], [[2, 1], [4, 1]], [[3, 2], [5, 2]], [[4, 0], [5, 0]], [[4, 1], [5, 0]]], 
            [[[0, 1], [1, 1]], [[0, 2], [2, 2]], [[1, 0], [3, 0]], [[1, 0], [3, 1]], [[1, 1], [2, 2]], [[1, 1], [3, 1]], [[2, 2], [4, 2]], [[3, 0], [5, 0]], [[3, 1], [4, 1]]]
        ]

    def __repr__(self):
        return (f"Amazon(username={self.username!r}, "
                f"level={self.level}, "
                f"strength={self.strength}, "
                f"dexterity={self.dexterity}, "
                f"vitality={self.vitality}, "
                f"energy={self.energy}, "
                f"skill_tree_1={self.skill_tree_1!r}, "
                f"skill_tree_2={self.skill_tree_2!r}, "
                f"skill_tree_3={self.skill_tree_3!r})")
