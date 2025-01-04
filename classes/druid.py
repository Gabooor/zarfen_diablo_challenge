from classes.character_class import CharacterClass
from skill import Skill
from skill_tree import SkillTree

# Elemental
firestorm = Skill("Firestorm", [], 1, 0)
molten_boulder = Skill("Molten Boulder", [firestorm], 6, 0)
arctic_blast = Skill("Arctic Blast", [], 6, 0)
fissure = Skill("Fissure", [molten_boulder], 12, 0)
cyclone_armor = Skill("Cyclone Armor", [arctic_blast], 12, 0)
twister = Skill("Twister", [cyclone_armor], 18, 0)
volcano = Skill("Volcano", [fissure], 24, 0)
tornado = Skill("Tornado", [cyclone_armor], 24, 0)
armageddon = Skill("Armageddon", [volcano], 30, 0)
hurricane = Skill("Hurricane", [tornado], 30, 0)

druid_elemental_tree = SkillTree(
    "Elemental",
    "Druid",
    [firestorm, molten_boulder, arctic_blast, fissure, cyclone_armor, twister, volcano, tornado, armageddon, hurricane],
    layout=[[1, 0, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 1, 0], [1, 1, 0]],
)

# Shape Shifting
werewolf = Skill("Werewolf", [], 1, 0)
lycanthropy = Skill("Lycanthropy", [werewolf], 1, 0)
werebear = Skill("Werebear", [], 6, 0)
feral_rage = Skill("Feral Rage", [werewolf], 12, 0)
maul = Skill("Maul", [werebear], 12, 0)
rabies = Skill("Rabies", [feral_rage], 18, 0)
fire_claws = Skill("Fire Claws", [feral_rage, maul], 18, 0)
hunger = Skill("Hunger", [fire_claws], 24, 0)
shock_wave = Skill("Shock Wave", [maul], 24, 0)
fury = Skill("Fury", [rabies], 30, 0)

druid_shape_shifting_tree = SkillTree(
    "Shape Shifting",
    "Druid",
    [werewolf, lycanthropy, werebear, feral_rage, maul, rabies, fire_claws, hunger, shock_wave, fury],
    layout=[[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0]],
)

# Summoning
raven = Skill("Raven", [], 1, 0)
poison_creeper = Skill("Poison Creeper", [], 1, 0)
oak_sage = Skill("Oak Sage", [], 6, 0)
summon_spirit_wolf = Skill("Summon Spirit Wolf", [raven], 6, 0)
carrion_vine = Skill("Carrion Vine", [poison_creeper], 12, 0)
heart_of_wolverine = Skill("Heart of Wolverine", [oak_sage], 18, 0)
summon_dire_wolf = Skill("Summon Dire Wolf", [oak_sage, summon_spirit_wolf], 18, 0)
solar_creeper = Skill("Solar Creeper", [carrion_vine], 24, 0)
spirit_of_barbs = Skill("Spirit of Barbs", [heart_of_wolverine], 30, 0)
summon_grizzly = Skill("Summon Grizzly", [summon_dire_wolf], 30, 0)

druid_summoning_tree = SkillTree(
    "Summoning",
    "Druid",
    [
        raven,
        poison_creeper,
        oak_sage,
        summon_spirit_wolf,
        carrion_vine,
        heart_of_wolverine,
        summon_dire_wolf,
        solar_creeper,
        spirit_of_barbs,
        summon_grizzly,
    ],
    layout=[[0, 1, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]],
)


class Druid(CharacterClass):
    def __init__(
        self,
        username: str,
        level: int = 1,
        strength: int = 15,
        dexterity: int = 20,
        vitality: int = 25,
        energy: int = 20,
    ):
        super().__init__("Druid", username, level, strength, dexterity, vitality, energy)

    @property
    def skill_trees(self):
        return [druid_elemental_tree, druid_shape_shifting_tree, druid_summoning_tree]

    @property
    def skill_tree_dependencies(self):
        return [
            [
                [[0, 0], [1, 0]],
                [[1, 0], [2, 0]],
                [[1, 2], [2, 2]],
                [[2, 0], [4, 0]],
                [[2, 2], [3, 1]],
                [[3, 1], [4, 1]],
                [[4, 0], [5, 0]],
                [[4, 1], [5, 1]],
                [[5, 1], [5, 0]],
            ],
            [
                [[0, 0], [0, 1]],
                [[0, 0], [2, 0]],
                [[1, 2], [2, 2]],
                [[2, 0], [3, 0]],
                [[2, 0], [3, 1]],
                [[2, 2], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 0], [5, 0]],
                [[3, 1], [4, 1]],
            ],
            [
                [[0, 1], [1, 1]],
                [[0, 2], [2, 2]],
                [[1, 0], [3, 0]],
                [[1, 0], [3, 1]],
                [[1, 1], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 0], [5, 0]],
                [[3, 1], [5, 1]],
            ],
        ]
