from classes.character_class import CharacterClass
from skill import Skill
from skill_tree import SkillTree

# Cold Spells
ice_bolt = Skill("Ice Bolt", [], 1, 0)
frozen_armor = Skill("Frozen Armor", [], 1, 0)
frost_nova = Skill("Frost Nova", [], 6, 0)
ice_blast = Skill("Ice Blast", [ice_bolt], 6, 0)
shiver_armor = Skill("Shiver Armor", [frozen_armor, ice_blast], 12, 0)
glacial_spike = Skill("Glacial Spike", [ice_blast], 18, 0)
blizzard = Skill("Blizzard", [frost_nova, glacial_spike], 24, 0)
chilling_armor = Skill("Chilling Armor", [shiver_armor], 24, 0)
frozen_orb = Skill("Frozen Orb", [blizzard], 30, 0)
cold_mastery = Skill("Cold Mastery", [], 30, 0)

sorceress_cold_spells_tree = SkillTree(
    "Cold Spells",
    "Sorceress",
    [
        ice_bolt,
        frozen_armor,
        frost_nova,
        ice_blast,
        shiver_armor,
        glacial_spike,
        blizzard,
        chilling_armor,
        frozen_orb,
        cold_mastery,
    ],
    layout=[[0, 1, 1], [1, 1, 0], [0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0]],
)

# Lightning Spells
charged_bolt = Skill("Charged Bolt", [], 1, 0)
static_field = Skill("Static Field", [], 6, 0)
telekinesis = Skill("Telekinesis", [], 6, 0)
nova = Skill("Nova", [static_field], 12, 0)
lightning = Skill("Lightning", [charged_bolt], 12, 0)
chain_lightning = Skill("Chain Lightning", [lightning], 18, 0)
teleport = Skill("Teleport", [telekinesis], 18, 0)
thunder_storm = Skill("Thunder Storm", [nova, chain_lightning], 24, 0)
energy_shield = Skill("Energy Shield", [teleport], 24, 0)
lightning_mastery = Skill("Lightning Mastery", [], 30, 0)

sorceress_lightning_spells_tree = SkillTree(
    "Lightning Spells",
    "Sorceress",
    [
        charged_bolt,
        static_field,
        telekinesis,
        nova,
        lightning,
        chain_lightning,
        teleport,
        thunder_storm,
        energy_shield,
        lightning_mastery,
    ],
    layout=[[0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 1], [0, 1, 0]],
)

# Fire Spells
fire_bolt = Skill("Fire Bolt", [], 1, 0)
warmth = Skill("Warmth", [], 1, 0)
inferno = Skill("Inferno", [], 6, 0)
blaze = Skill("Blaze", [inferno], 12, 0)
fire_ball = Skill("Fire Ball", [fire_bolt], 12, 0)
fire_wall = Skill("Fire Wall", [blaze], 18, 0)
enchant = Skill("Enchant", [warmth, fire_ball], 18, 0)
meteor = Skill("Meteor", [fire_ball, fire_wall], 24, 0)
fire_mastery = Skill("Fire Mastery", [], 30, 0)
hydra = Skill("Hydra", [enchant], 30, 0)

sorceress_fire_spells_tree = SkillTree(
    "Fire Spells",
    "Sorceress",
    [fire_bolt, warmth, inferno, blaze, fire_ball, fire_wall, enchant, meteor, fire_mastery, hydra],
    layout=[[0, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 0], [0, 1, 1]],
)


class Sorceress(CharacterClass):
    def __init__(
        self,
        username: str,
        level: int = 1,
        strength: int = 10,
        dexterity: int = 25,
        vitality: int = 10,
        energy: int = 35,
    ):
        super().__init__("Sorceress", username, level, strength, dexterity, vitality, energy)

    @property
    def skill_trees(self):
        return [sorceress_cold_spells_tree, sorceress_lightning_spells_tree, sorceress_fire_spells_tree]

    @property
    def skill_tree_dependencies(self):
        return [
            [
                [[0, 1], [1, 1]],
                [[0, 2], [2, 2]],
                [[1, 0], [4, 0]],
                [[1, 1], [2, 2]],
                [[1, 1], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 1], [4, 0]],
                [[4, 0], [5, 0]],
            ],
            [
                [[0, 1], [2, 1]],
                [[1, 0], [2, 0]],
                [[1, 2], [3, 2]],
                [[2, 0], [4, 0]],
                [[2, 1], [3, 1]],
                [[3, 1], [4, 0]],
                [[3, 1], [4, 2]],
                [[3, 2], [4, 2]],
            ],
            [
                [[0, 1], [2, 1]],
                [[0, 2], [3, 2]],
                [[1, 0], [2, 0]],
                [[2, 0], [3, 0]],
                [[2, 1], [3, 2]],
                [[2, 1], [4, 1]],
                [[3, 0], [4, 1]],
                [[3, 2], [5, 2]],
            ],
        ]
