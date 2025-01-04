from classes.character_class import CharacterClass
from skill import Skill
from skill_tree import SkillTree

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


necromancer_summoning_tree = SkillTree(
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
        revive,
    ],
    layout=[[1, 0, 1], [0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 1, 0], [0, 1, 1]],
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

necromancer_poison_and_bone_tree = SkillTree(
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
        bone_spirit,
    ],
    layout=[[0, 1, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0], [0, 0, 1], [1, 1, 0]],
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


necromnacer_curses_tree = SkillTree(
    "Curses",
    "Necromancer",
    [amplify_damage, dim_vision, weaken, iron_maiden, terror, confuse, life_tap, attract, decrepify, lower_resist],
    layout=[[0, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 0]],
)


class Necromancer(CharacterClass):
    def __init__(
        self,
        username: str,
        level: int = 1,
        strength: int = 15,
        dexterity: int = 25,
        vitality: int = 15,
        energy: int = 25,
    ):
        super().__init__("Necromancer", username, level, strength, dexterity, vitality, energy)

    @property
    def skill_trees(self):
        return [necromancer_summoning_tree, necromancer_poison_and_bone_tree, necromnacer_curses_tree]

    @property
    def skill_tree_dependencies(self):
        return [
            [
                [[0, 2], [0, 0]],
                [[0, 2], [2, 2]],
                [[1, 1], [2, 0]],
                [[1, 1], [3, 1]],
                [[2, 0], [4, 0]],
                [[2, 2], [5, 2]],
                [[3, 1], [4, 1]],
                [[4, 1], [5, 1]],
                [[4, 1], [5, 2]],
            ],
            [
                [[0, 1], [1, 1]],
                [[0, 2], [2, 2]],
                [[1, 0], [3, 0]],
                [[1, 1], [3, 0]],
                [[1, 1], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 0], [5, 0]],
                [[3, 1], [4, 2]],
                [[3, 1], [5, 1]],
            ],
            [
                [[0, 1], [1, 2]],
                [[0, 1], [2, 1]],
                [[1, 0], [3, 0]],
                [[1, 2], [2, 2]],
                [[2, 1], [3, 1]],
                [[2, 2], [4, 2]],
                [[3, 0], [4, 0]],
                [[3, 1], [5, 1]],
                [[4, 2], [5, 1]],
            ],
        ]
