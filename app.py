import tkinter as tk
from PIL import Image, ImageTk

from classes.sorceress import Sorceress
from classes.druid import Druid
from classes.amazon import Amazon
from classes.paladin import Paladin
from classes.barbarian import Barbarian
from classes.necromancer import Necromancer

# Create the main window
root = tk.Tk()
root.title("Zarfen Diablo II Challenges")
root.geometry("1280x1000")
root.resizable(False, False)

# Create a frame for the header
header_frame = tk.Frame(root, height=75, bg="lightblue")
header_frame.pack(fill=tk.X, side=tk.TOP)

# Add a title label to the header
image_path = "header.png"  # Path to your image file
image = Image.open(image_path)
image = image.resize((1280, 75), Image.Resampling.LANCZOS)  # Resize the image to fit the frame
header_photo = ImageTk.PhotoImage(image)

# Create a label with the image and add it to the top sub-frame
header_pic = tk.Label(header_frame, image=header_photo)
header_pic.place(relwidth=1, relheight=1)

title_label = tk.Label(header_frame, text="Zarfen Diablo II Challenges", font=("Georgia", 22, "bold"), height=2, bg="#100605", fg="#ffb955")
title_label.pack()

# Create a frame for the side panel
side_panel_frame = tk.Frame(root, width=200, bg="#100605")
side_panel_frame.pack(fill=tk.Y, side=tk.LEFT)

# Add multiple buttons to the side panel
buttons = ["Random Build", "Challenge 2", "Challenge 3", "Challenge 4", "Challenge 5", "Challenge 6", "Challenge 7"]
button_image = tk.PhotoImage(file="button.png")
for btn_text in buttons:
    button = tk.Button(side_panel_frame, text=btn_text, image=button_image, compound="center", fg="#cfc8b8", bg="#100605", font=("Georgia", 14, "bold"), borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    button.pack(fill=tk.X, pady=1, padx=10)

# Create a frame for the main content area
main_content_frame = tk.Frame(root)
main_content_frame.pack(fill=tk.BOTH, expand=True)

# Create two sub-containers within the main content area
top_subframe = tk.Frame(main_content_frame)
top_subframe.pack(fill=tk.BOTH, expand=True)

# Configure grid layout (3 columns)
for i in range(3):
    top_subframe.grid_columnconfigure(i, weight=1)

maya = Sorceress("Maya")
adam = Druid("Adam")
mia = Amazon("mia")
paul = Paladin("Paul")
bryan = Barbarian("Bryan")
nimrod = Necromancer("Nimrod")

character = nimrod
# Add a widget that spans across the top 3 columns
merged_label = tk.Label(top_subframe, text=f"Your current {character.skill_tree_1.character_class} skill tree", bg="lightgreen", font=("Georgia", 16))
merged_label.grid(row=0, column=0, columnspan=3, pady=10)

# Add a 3x6 grid in each cell of the second row of the top_subframe

skill_tree_names = [character.skill_tree_1.name, character.skill_tree_2.name, character.skill_tree_3.name]
layouts = [
    character.skill_tree_1.layout,
    character.skill_tree_2.layout,
    character.skill_tree_3.layout
]

image_paths = []

for i in range(3):
    sub_image_paths = []
    for j in range(10):
        if i == 0:
            formatted_name = character.skill_tree_1.skills[j].name.lower().replace(" ", "_")
            path = f"skills/{character.skill_tree_1.character_class}/{character.skill_tree_1.name}/{formatted_name}.png"
        elif i == 1:
            formatted_name = character.skill_tree_2.skills[j].name.lower().replace(" ", "_")
            path = f"skills/{character.skill_tree_2.character_class}/{character.skill_tree_2.name}/{formatted_name}.png"
        if i == 2:
            formatted_name = character.skill_tree_3.skills[j].name.lower().replace(" ", "_")
            path = f"skills/{character.skill_tree_3.character_class}/{character.skill_tree_3.name}/{formatted_name}.png"
        sub_image_paths.append(path)
    image_paths.append(sub_image_paths)

# image_paths = [
#     ["skills/ice_bolt.png", "skills/frozen_armor.png", "skills/frost_nova.png", "skills/ice_blast.png", "skills/shiver_armor.png", "skills/glacial_spike.png", "skills/blizzard.png", "skills/chilling_armor.png", "skills/frozen_orb.png", "skills/cold_mastery.png", ],
#     ["skills/charged_bolt.png", "skills/static_field.png", "skills/telekinesis.png", "skills/nova.png", "skills/lightning.png", "skills/chain_lightning.png", "skills/teleport.png", "skills/thunder_storm.png", "skills/energy_shield.png", "skills/lightning_mastery.png", ],
#     ["skills/fire_bolt.png", "skills/warmth.png", "skills/inferno.png", "skills/blaze.png", "skills/fire_ball.png", "skills/fire_wall.png", "skills/enchant.png", "skills/meteor.png", "skills/fire_mastery.png", "skills/hydra.png"]    
# ]
images = [[],[],[]]

for i in range(3):
    for path in image_paths[i]:
        skill_image = Image.open(path)
        skill_image = skill_image.resize((70, 70), Image.Resampling.LANCZOS)
        skill_photo = ImageTk.PhotoImage(skill_image)
        images[i].append(skill_photo)


for col in range(3):
    skill_count = 0
    inner_frame = tk.Frame(top_subframe, bg="white", relief="solid", borderwidth=1)
    inner_frame.grid(row=1, column=col, pady=10)

    # Configure the 3x6 grid inside the inner_frame
    for r in range(7):
        inner_frame.grid_rowconfigure(r, weight=1)
    for c in range(3):
        inner_frame.grid_columnconfigure(c, weight=1)

    # Populate the 3x6 grid with labels (or other widgets)
    merged_inner_label = tk.Label(inner_frame, text=skill_tree_names[col], bg="lightgreen", font=("Georgia", 16))
    merged_inner_label.grid(row=0, column=0, columnspan=3, sticky="nsew")
    for r in range(6):
        for c in range(3):
            if layouts[col][r][c] == 1:
                cell_button = tk.Button(inner_frame, image=images[col][skill_count], bg="lightgray", relief="ridge", width=70, height=70)
                # cell_label = tk.Label(inner_frame, text=r, font=("Arial", 20, "bold"), fg="white", bg="#3d3021")
                
                skill_count += 1
                cell_button.grid(row=r+1, column=c, pady=10, padx=15)
                # cell_label.grid(row=r+1, column=c, pady=10, padx=15)
            else:
                cell_button = tk.Button(inner_frame, bg="lightgray", relief="ridge", width=70, height=70)
                cell_button.grid(row=r+1, column=c, pady=10, padx=15)
                cell_button.grid_forget()

# Bottom Subframe Configuration (unchanged)
bottom_subframe = tk.Frame(main_content_frame, bg="grey", height=350)
bottom_subframe.pack(fill=tk.X)

bottom_subframe.grid_rowconfigure(0, weight=1)
bottom_subframe.grid_rowconfigure(1, weight=1)
bottom_subframe.grid_rowconfigure(2, weight=1)
bottom_subframe.grid_columnconfigure(0, weight=1)
bottom_subframe.grid_columnconfigure(1, weight=0)
bottom_subframe.grid_columnconfigure(2, weight=1)

# Add buttons to the bottom_subframe (unchanged)
lvl_up_image = Image.open("button.png")
lvl_up_image = lvl_up_image.resize((200, 40), Image.Resampling.LANCZOS)
lvl_up_photo = ImageTk.PhotoImage(lvl_up_image)
level_up_btn = tk.Button(bottom_subframe, text="Level up", image=lvl_up_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=200, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
add_skill_btn = tk.Button(bottom_subframe, text="Add one skill", image=lvl_up_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=200, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")

undo_image = Image.open("button_110.png")
undo_image = undo_image.resize((100, 40), Image.Resampling.LANCZOS)
undo_photo = ImageTk.PhotoImage(undo_image)
undo_btn = tk.Button(bottom_subframe, text="Undo", image=undo_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=100, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")

new_char_image = Image.open("button_300.png")
new_char_image = new_char_image.resize((280, 40), Image.Resampling.LANCZOS)
new_char_photo = ImageTk.PhotoImage(new_char_image)
new_char_btn = tk.Button(bottom_subframe, text="Create new character", image=new_char_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=280, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")

import_char_image = Image.open("button_300.png")
import_char_image = import_char_image.resize((230, 40), Image.Resampling.LANCZOS)
import_char_photo = ImageTk.PhotoImage(import_char_image)
import_char_btn = tk.Button(bottom_subframe, text="Import character", image=import_char_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=230, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")

# Place buttons in the bottom_subframe (unchanged)
level_up_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")
add_skill_btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")
undo_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

new_char_btn.grid(row=0, column=2, padx=10, pady=10, sticky="e")
import_char_btn.grid(row=1, column=2, padx=10, pady=10, sticky="e")

next_stats_label = tk.Label(bottom_subframe, text="Lv. 3 stats:\n1 strength\n3 dexterity\n0 vitality\n1 energy\n\nLv. 3 skill:\nIce Bolt", font=("Georgia", 10, "bold"), height=2, bg="grey", fg="white")
next_stats_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")

# Run the Tkinter event loop
root.mainloop()
