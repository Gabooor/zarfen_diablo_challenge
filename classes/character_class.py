from abc import abstractmethod
from typing import Any

from skill_tree import SkillTree


class CharacterClass:
    def __init__(
        self, character_class: str, username: str, level: int, strength: int, dexterity: int, vitality: int, energy: int
    ):
        self.character_class = character_class
        self.username = username

        self.level = level

        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.energy = energy

    @property
    @abstractmethod
    def skill_trees(self) -> list[SkillTree]:
        return []

    @property
    @abstractmethod
    def skill_tree_dependencies(self) -> list[list[list[list[int]]]]:
        return []

    def __repr__(self):
        return (
            f"{self.character_class}(username={self.username!r}, "
            f"level={self.level}, "
            f"strength={self.strength}, "
            f"dexterity={self.dexterity}, "
            f"vitality={self.vitality}, "
            f"energy={self.energy}, "
            f"skill_trees={self.skill_trees!r}"
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "username": self.username,
            "level": self.level,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "vitality": self.vitality,
            "energy": self.energy,
            "skill_trees": [st.to_dict() for st in self.skill_trees],
            "skill_tree_dependencies": self.skill_tree_dependencies,
        }
