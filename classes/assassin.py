from classes.character_class import CharacterClass

from skill import Skill
from skill_tree import SkillTree

# Martial Arts
tiger_strike = Skill("Tiger Strike", [], 1, 0)
dragon_talon = Skill("Dragon Talon", [], 1, 0)
fists_of_fire = Skill("Fists of Fire", [], 6, 0)
dragon_claw = Skill("Dragon Claw", [dragon_talon], 6, 0)
cobra_strike = Skill("Cobra Strike", [tiger_strike], 12, 0)
claws_of_thunder = Skill("Claws of Thunder", [fists_of_fire], 18, 0)
dragon_tail = Skill("Dragon Tail", [dragon_claw], 18, 0)
blades_of_ice = Skill("Blades of Ice", [claws_of_thunder], 24, 0)
dragon_flight = Skill("Dragon Flight", [dragon_tail], 24, 0)
phoenix_strike = Skill("Phoenix Strike", [cobra_strike], 30, 0)

assassin_martial_arts_tree = SkillTree(
    "Martial Arts",
    "Assassin",
    [
        tiger_strike,
        dragon_talon,
        fists_of_fire,
        dragon_claw,
        cobra_strike,
        claws_of_thunder,
        dragon_tail,
        blades_of_ice,
        dragon_flight,
        phoenix_strike,
    ],
    layout=[[0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1], [1, 0, 1], [0, 1, 0]],
)

# Shadow Disciplines
claw_mastery = Skill("Claw Mastery", [], 1, 0)
psychic_hammer = Skill("Psychic Hammer", [], 1, 0)
burst_of_speed = Skill("Burst of Speed", [claw_mastery], 6, 0)
weapon_block = Skill("Weapon Block", [claw_mastery], 12, 0)
cloak_of_shadows = Skill("Cloak of Shadows", [psychic_hammer], 12, 0)
fade = Skill("Fade", [burst_of_speed], 18, 0)
shadow_warrior = Skill("Shadow Warrior", [weapon_block, cloak_of_shadows], 18, 0)
mind_blast = Skill("Mind Blast", [cloak_of_shadows], 24, 0)
venom = Skill("Venom", [fade], 30, 0)
shadow_master = Skill("Shadow Master", [shadow_warrior], 30, 0)

assassin_shadow_disciplines_tree = SkillTree(
    "Shadow Disciplines",
    "Assassin",
    [
        claw_mastery,
        psychic_hammer,
        burst_of_speed,
        weapon_block,
        cloak_of_shadows,
        fade,
        shadow_warrior,
        mind_blast,
        venom,
        shadow_master,
    ],
    layout=[[0, 1, 1], [1, 0, 0], [0, 1, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]],
)

# Traps
fire_blast = Skill("Fire Blast", [], 1, 0)
shock_web = Skill("Shock Web", [fire_blast], 6, 0)
blade_sentinel = Skill("Blade Sentinel", [], 6, 0)
charged_bolt_sentry = Skill("Charged Bolt Sentry", [shock_web], 12, 0)
wake_of_fire = Skill("Wake of Fire", [fire_blast], 12, 0)
blade_fury = Skill("Blade Fury", [blade_sentinel, wake_of_fire], 18, 0)
lightning_sentry = Skill("Lightning Sentry", [charged_bolt_sentry], 24, 0)
wake_of_inferno = Skill("Wake of Inferno", [wake_of_fire], 24, 0)
death_sentry = Skill("Death Sentry", [lightning_sentry], 30, 0)
blade_shield = Skill("Blade Shield", [blade_fury], 30, 0)

assassin_traps_tree = SkillTree(
    "Traps",
    "Assassin",
    [
        fire_blast,
        shock_web,
        blade_sentinel,
        charged_bolt_sentry,
        wake_of_fire,
        blade_fury,
        lightning_sentry,
        wake_of_inferno,
        death_sentry,
        blade_shield,
    ],
    layout=[[0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0], [1, 0, 1]],
)


class Assassin(CharacterClass):
    def __init__(
        self,
        username: str,
        level: int = 1,
        strength: int = 20,
        dexterity: int = 20,
        vitality: int = 20,
        energy: int = 25,
    ):
        super().__init__("Assassin", username, level, strength, dexterity, vitality, energy)

    @property
    def skill_trees(self):
        return [assassin_martial_arts_tree, assassin_shadow_disciplines_tree, assassin_traps_tree]

    @property
    def skill_tree_dependencies(self):
        return [
            [
                [[0, 1], [2, 1]],
                [[0, 2], [1, 2]],
                [[1, 0], [3, 0]],
                [[1, 2], [3, 2]],
                [[2, 1], [5, 1]],
                [[3, 0], [4, 0]],
                [[3, 2], [4, 2]],
                [[4, 0], [5, 1]],
            ],
            [
                [[0, 1], [1, 0]],
                [[0, 1], [2, 1]],
                [[0, 2], [2, 2]],
                [[1, 0], [3, 0]],
                [[2, 1], [3, 1]],
                [[2, 2], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 0], [5, 0]],
                [[3, 1], [5, 1]],
            ],
            [
                [[0, 1], [1, 0]],
                [[0, 1], [2, 1]],
                [[1, 0], [2, 0]],
                [[1, 2], [3, 2]],
                [[2, 0], [4, 0]],
                [[2, 1], [3, 2]],
                [[2, 1], [4, 1]],
                [[3, 2], [5, 2]],
                [[4, 0], [5, 0]],
            ],
        ]
