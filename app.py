import tkinter as tk
from PIL import Image, ImageTk
from classes.sorceress import Sorceress
from classes.druid import Druid
from classes.amazon import Amazon
from classes.paladin import Paladin
from classes.barbarian import Barbarian
from classes.necromancer import Necromancer
from classes.assassin import Assassin

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
ashlin = Assassin("Ashlin")

character = adam
# Add a widget that spans across the top 3 columns
merged_label = tk.Label(top_subframe, text=f"Your current {character.__class__.__name__} skill tree", bg="lightgreen", font=("Georgia", 16))
merged_label.grid(row=0, column=0, columnspan=3, pady=10)

# Add a 3x6 grid in each cell of the second row of the top_subframe

layouts = [
    character.skill_trees[0].layout,
    character.skill_trees[1].layout,
    character.skill_trees[2].layout
]

image_paths = []

for i in range(3):
    sub_image_paths = []
    for j in range(10):
        formatted_name = character.skill_trees[i].skills[j].name.lower().replace(" ", "_")
        path = f"skills/{character.skill_trees[i].character_class}/{character.skill_trees[i].name}/{formatted_name}.png"
        sub_image_paths.append(path)
    image_paths.append(sub_image_paths)

images = [[],[],[]]

for i in range(3):
    for path in image_paths[i]:
        skill_image = Image.open(path)
        skill_image = skill_image.resize((70, 70), Image.Resampling.LANCZOS)
        skill_photo = ImageTk.PhotoImage(skill_image)
        images[i].append(skill_photo)

# Define specific connections between buttons using pairs of coordinates

lines_path = "skill_tree_background.png"  # Path to your image file
lines_image = Image.open(lines_path)
# lines_image = lines_image.resize((318, 627), Image.Resampling.LANCZOS)  # Resize the image to fit the frame
lines_photo = ImageTk.PhotoImage(lines_image)

skill_positions = []
skill_tree_canvases = []
skill_level_rectangles = [[],[],[]]
skill_level_texts = [[],[],[]]

# Add skill trees with canvas and draw specific lines
for col in range(3):
    skill_count = 0
    
    # Create a canvas directly on the top_subframe instead of using a Label and inner_frame
    canvas_width, canvas_height = 318, 619
    canvas = tk.Canvas(top_subframe, width=canvas_width, height=canvas_height, bg="white")
    skill_tree_canvases.append(canvas)
    canvas.grid(row=1, column=col, pady=10, padx=15)

    # Determine the total content size (based on 3x6 grid and button size)
    content_width, content_height = 3 * 80, 6 * 80  # Each button is 80x80 including padding

    # Calculate the offset for centering the content within the canvas
    x_offset = (canvas_width - content_width) // 2
    y_offset = (canvas_height - content_height) // 2

    # Add background image to the canvas, centered
    canvas.create_image(0, 0, image=lines_photo, anchor="nw")

    # Store button positions and references
    skill_image_positions = {}

    # First pass: Determine button positions based on layout, apply offset
    for r in range(6):
        for c in range(3):
            if layouts[col][r][c] == 1:
                # Calculate the position for the button with offset
                x, y = x_offset + 15 + c * 80, y_offset + 15 + r * 80
                # Store button positions (center of the button) using the grid position as the key
                skill_image_positions[(r, c)] = (x + 35, y + 35)  # Adding 35 to get the center of the button (70/2)

    # Draw lines between specific buttons according to the variable 'lines_to_draw'
    for connection in character.skill_tree_dependencies[col]:
        start_row, start_col = connection[0]
        end_row, end_col = connection[1]
        if (start_row, start_col) in skill_image_positions and (end_row, end_col) in skill_image_positions:
            x1, y1 = skill_image_positions[(start_row, start_col)]
            x2, y2 = skill_image_positions[(end_row, end_col)]
            canvas.create_line(x1, y1, x2, y2, fill="#aca186", width=8)

    skill_positions.append(skill_image_positions)

    # Second pass: Draw skill images (buttons) on top of the lines and background, centered
    skill_count = 0
    for r in range(6):
        for c in range(3):
            if layouts[col][r][c] == 1:
                # Create skill button (image) on the canvas with offset
                x, y = x_offset + 15 + c * 80, y_offset + 15 + r * 80
                canvas.create_image(x, y, image=images[col][skill_count], anchor="nw")
                rectangle = canvas.create_rectangle(0, 0, 0, 0, width=10, fill="black")
                text = canvas.create_text(0, 0, font=("Courier New", 14, "bold"), fill="#cfc8b8")
                # rectangle = canvas.create_rectangle(x+54, y+54, x+64, y+64, width=10, fill="black")
                # text = canvas.create_text(x+60, y+60, text="+", font=("Courier New", 14), fill="#cfc8b8")
                skill_level_rectangles[col].append(rectangle)
                skill_level_texts[col].append(text)
                skill_count += 1

    canvas.create_text(canvas_width // 2, y_offset - 40, text=character.skill_trees[col].name, font=("Georgia", 20, "bold"), fill="#cfc8b8")

import random
for i in range(3): # skill trees
    for j, skill in enumerate(character.skill_trees[i].skills):
        character.skill_trees[i].skills[j].base_level = random.randint(0, 99)

for i in range(3): # skill trees
    for j, skill in enumerate(character.skill_trees[i].skills):
        if skill.base_level > 0:
            position = list(skill_positions[i].items())[j]
            _, (a, b) = position
            skill_tree_canvases[i].itemconfig(skill_level_texts[i][j], text=skill.base_level)
            if skill.base_level < 10:
                skill_tree_canvases[i].coords(skill_level_texts[i][j], a+25, b+25)
                skill_tree_canvases[i].coords(skill_level_rectangles[i][j], a+22, b+20, a+30, b+30)
            else:
                skill_tree_canvases[i].coords(skill_level_texts[i][j], a+20, b+25)
                skill_tree_canvases[i].coords(skill_level_rectangles[i][j], a+10, b+20, a+30, b+30)
        

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

# Add additional buttons (unchanged)
new_char_image = Image.open("button_300.png")
new_char_image = new_char_image.resize((230, 40), Image.Resampling.LANCZOS)
new_char_photo = ImageTk.PhotoImage(new_char_image)
new_char_btn = tk.Button(bottom_subframe, text="New character", image=new_char_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=230, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")

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