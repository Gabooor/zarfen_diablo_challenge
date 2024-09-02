class Skill:
    def __init__(self, name, prerequisites, required_level, base_level):
        self.name = name
        self.prerequisites = prerequisites
        self.required_level = required_level
        self.base_level = base_level

    def __repr__(self):
        return (f"Skill(name={self.name!r}, "
                f"prerequisites={[p.name for p in self.prerequisites]}, "
                f"required_level={self.required_level}, "
                f"base_level={self.base_level})")
