class Skill_Tree:
    def __init__(self, name, character_class, skills, layout):
        self.character_class = character_class
        self.name = name
        self.skills = skills
        self.layout = layout

    def __repr__(self):
        skills_repr = ', '.join(f"{skill.name!r}" for skill in self.skills)
        return (f"Skill_Tree(character_class={self.character_class!r}, "
                f"name={self.name!r}, "
                f"skills=[{skills_repr}])")

    def to_dict(self):
        return {
            "character_class": self.character_class,
            "name": self.name,
            "skills": [skill.to_dict() for skill in self.skills],
            "layout": self.layout
        }