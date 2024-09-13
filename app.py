import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

import json
import os

from classes.sorceress import Sorceress
from classes.druid import Druid
from classes.amazon import Amazon
from classes.paladin import Paladin
from classes.barbarian import Barbarian
from classes.necromancer import Necromancer
from classes.assassin import Assassin

content_frames = []


def blend_image_with_background(image_path, bg_color=(255, 255, 255), opacity=0.1):
    # Load the image with alpha channel (transparency)
    image = Image.open(image_path).convert("RGBA")

    # Create a background image with the same size and the specified background color
    background = Image.new("RGBA", image.size, bg_color + (255,))

    # Apply alpha blending between the image and the background
    blended = Image.blend(background, image, opacity)

    # Convert the image to a format Tkinter can work with
    return ImageTk.PhotoImage(blended)

def on_class_checkbox_change(is_randomized, combobox, canvas, is_randomized_text):
    if is_randomized.get():
        combobox.config(state="disabled")
        canvas.itemconfig(is_randomized_text, text="Randomizing is enabled")
    else:
        combobox.config(state="enabled")
        canvas.itemconfig(is_randomized_text, text="")

def on_class_combobox_change(combobox, image_label):
    selected_value = combobox.get().lower()

    character_image = Image.open(f"char_images/{selected_value}.png")
    character_image = character_image.resize((239, 590), Image.Resampling.LANCZOS)
    character_photo = ImageTk.PhotoImage(character_image)
    
    image_label.config(image=character_photo)
    image_label.image = character_photo
    image_label.focus_set()

def main_menu(frames, main_menu_screen):
    for frame in frames:
        frame.pack_forget()
    c_width = 1056
    c_height = 926
    cv_menu = tk.Canvas(main_menu_screen, width=c_width, height=c_height, highlightthickness=0)
    cl_background_image_path = "character_load_background.png"
    cl_background_image = Image.open(cl_background_image_path)
    # cl_background_image = cl_background_image.resize((1060, 590), Image.Resampling.LANCZOS)
    cl_photo = ImageTk.PhotoImage(cl_background_image)
    # cl_background_image_path = Image.open("character_load_background.png")
    # cl_photo = ImageTk.PhotoImage(character_load_background)

    cv_menu.create_image(0, 0, image=cl_photo, anchor="nw")
    cv_menu.pack(fill=tk.BOTH, expand=True)
    cv_menu.image = cl_photo
    
    # Main menu text
    cv_menu.create_text(c_width/2 + 4, 54, text="Main menu", font=("Georgia", 30, "bold"), fill="black")
    cv_menu.create_text(c_width/2, 50, text="Main menu", font=("Georgia", 30, "bold"), fill="#b0b0b0")
    
    # Welcome text 1
    cv_menu.create_text(c_width/2 + 4, 104, text="Welcome to Zarfen the Loot Goblin's Diablo II challenge dashboard", font=("Georgia", 18, "bold"), fill="black")
    cv_menu.create_text(c_width/2, 100, text="Welcome to Zarfen the Loot Goblin's Diablo II challenge dashboard", font=("Georgia", 18, "bold"), fill="#b0b0b0")
    # Welcome text 2
    cv_menu.create_text(c_width/2 + 4, 134, text="This project was made mainly for Zarfen for his challenges, but", font=("Georgia", 14, "bold"), fill="black")
    cv_menu.create_text(c_width/2, 130, text="This project was made mainly for Zarfen for his challenges, but", font=("Georgia", 14, "bold"), fill="#b0b0b0")
    # Welcome text 3
    cv_menu.create_text(c_width/2 + 4, 159, text="secondly for the entire Diablo II community to enjoy it", font=("Georgia", 14, "bold"), fill="black")
    cv_menu.create_text(c_width/2, 154, text="secondly for the entire Diablo II community to enjoy it", font=("Georgia", 14, "bold"), fill="#b0b0b0")

    # Zarfen logo
    zarfen_logo_image = Image.open("zarfen.png")
    zarfen_logo_image = zarfen_logo_image.resize((120, 120), Image.Resampling.LANCZOS)
    zarfen_logo_photo = ImageTk.PhotoImage(zarfen_logo_image)

    image_label = tk.Label(main_menu_screen, image=zarfen_logo_photo, highlightthickness=0, bg="#0b0b09")
    cv_menu.create_window(c_width/2, 250, window=image_label)
    image_label.image = zarfen_logo_photo
    
    # Welcome text 4
    cv_menu.create_text(489, 378, text="As time goes by, the project will have more and more challenges. \nCurrent challenges: \n\t- Random build: Create a character and embrace the chaos! Every level-up assigns \n\t\t         random skills and stats, forcing you to adapt your playstyle on the fly.", font=("Georgia", 14, "bold"), fill="black")
    cv_menu.create_text(485, 374, text="As time goes by, the project will have more and more challenges. \nCurrent challenges: \n\t- Random build: Create a character and embrace the chaos! Every level-up assigns \n\t\t         random skills and stats, forcing you to adapt your playstyle on the fly.", font=("Georgia", 14, "bold"), fill="#b0b0b0")

    main_menu_screen.pack(fill=tk.BOTH, expand=True)

def open_file():
    # Define the initial directory
    initial_dir = 'characters'  # Change this to your desired directory

    # Open a file dialog to select a JSON file
    file_path = filedialog.askopenfilename(
        initialdir=initial_dir,  # Set the initial directory
        title="Select a JSON File",
        filetypes=(("JSON Files", "*.json"), ("All Files", "*.*"))
    )
    if file_path:
        load_character(file_path)

def load_character(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    
    character_class = data["skill_trees"][0]["character_class"]

    if character_class == "Sorceress":
        character = Sorceress("username")
    if character_class == "Druid":
        character = Druid("username")
    if character_class == "Amazon":
        character = Amazon("username")
    if character_class == "Paladin":
        character = Paladin("username")
    if character_class == "Barbarian":
        character = Barbarian("username")
    if character_class == "Necromancer":
        character = Necromancer("username")
    if character_class == "Assassin":
        character = Assassin("username")

    character.username = data['username']
    character.level = data['level']
    character.strength = data['strength']
    character.dexterity = data['dexterity']
    character.vitality = data['vitality']
    character.energy = data['energy']
    
    # Loop through each skill tree and update the skill's base level
    for tree_data, skill_tree in zip(data['skill_trees'], character.skill_trees):
        for skill_data, skill in zip(tree_data['skills'], skill_tree.skills):
            skill.base_level = skill_data['base_level']
    
    random_build(content_frames, ch1_main_top_screen, ch1_main_bottom_screen, character)

def create_new_character(character_class, is_randomized, name, canvas, error_text):
    if name == "":
        canvas.itemconfig(error_text, text="You must provide a character name!")
        canvas.itemconfig(error_text, fill="red")
        return
    if os.path.exists(f"characters/{name}.json"):
        canvas.itemconfig(error_text, text="You already have a character with that name!")
        canvas.itemconfig(error_text, fill="red")
        return
    if character_class == "Sorceress":
        character = Sorceress(name)
    if character_class == "Druid":
        character = Druid(name)
    if character_class == "Amazon":
        character = Amazon(name)
    if character_class == "Paladin":
        character = Paladin(name)
    if character_class == "Barbarian":
        character = Barbarian(name)
    if character_class == "Necromancer":
        character = Necromancer(name)
    if character_class == "Assassin":
        character = Assassin(name)
    with open(f"characters/{name}.json", 'w') as file:
        json.dump(character.to_dict(), file, indent=2)
    canvas.itemconfig(error_text, text="Successfully created character")
    canvas.itemconfig(error_text, fill="green")

    random_build(content_frames, ch1_main_top_screen, ch1_main_bottom_screen, character)

# lambda: random_build(content_frames, top_subframe, bottom_subframe)
def show_ch1_character_creation_screen(frames, screen):
    for frame in frames:
        frame.pack_forget()

    c_width = 1056
    c_height = 926
    cv = tk.Canvas(screen, width=c_width, height=c_height, highlightthickness=0)
    # cv.create_text(0, 0, text="TESTING", font=("Georgia", 20, "bold"), fill="black")
    # cv.create_image(x, y, image=images[col][skill_count], anchor="nw")
    # cv.create_rectangle(0, 0, 30, 30, width=10, fill="black")

    # path = "char_images/sorceress.png"
    # character_image = Image.open(path)
    # character_image = character_image.resize((239, 590), Image.Resampling.LANCZOS)
    # character_photo = ImageTk.PhotoImage(character_image)
    # 0b0b09
    cl_background_image_path = "character_load_background.png"
    cl_background_image = Image.open(cl_background_image_path)
    # cl_background_image = cl_background_image.resize((1060, 590), Image.Resampling.LANCZOS)
    cl_photo = ImageTk.PhotoImage(cl_background_image)
    # cl_background_image_path = Image.open("character_load_background.png")
    # cl_photo = ImageTk.PhotoImage(character_load_background)

    cv.create_image(0, 0, image=cl_photo, anchor="nw")
    cv.pack(fill=tk.BOTH, expand=True)
    cv.image = cl_photo
    
    
    # # Class setup
    # class_frame = tk.Frame(random_build_screen_1, bg="yellow")
    # class_frame.pack(padx=20, pady=20)
    # content_frames.append(class_frame)

    # class_left_frame = tk.Frame(class_frame, bg="purple")
    # class_left_frame.pack(side=tk.LEFT)
    # content_frames.append(class_left_frame)

    # class_right_frame = tk.Frame(class_frame, bg="pink")
    # class_right_frame.pack(side=tk.RIGHT)
    # content_frames.append(class_right_frame)

    # Class setup - Right
    character_image = Image.open("char_images/sorceress.png")
    character_image = character_image.resize((239, 590), Image.Resampling.LANCZOS)
    character_photo = ImageTk.PhotoImage(character_image)
    
    image_label = tk.Label(screen, image=character_photo, highlightthickness=0, bg="#0b0b09")
    cv.create_window(815, 400, window=image_label)
    image_label.image = character_photo

    # Character creation row
    cv.create_text(354, 124, text="Create character", font=("Georgia", 30, "bold"), fill="black")
    cv.create_text(350, 120, text="Create character", font=("Georgia", 30, "bold"), fill="#b0b0b0")


    # Enter character name row
    cv.create_text(223, 223, text="Enter character name:", font=("Georgia", 20, "bold"), fill="black")
    cv.create_text(220, 220, text="Enter character name:", font=("Georgia", 20, "bold"), fill="#918e89")
    create_character_entry = tk.Entry(screen, width=18, font=("Georgia", 16), bg="#222222", fg="#b0b0b0")
    cv.create_window(520, 220, window=create_character_entry)

    # Select a class row
    cv.create_text(284, 273, text="Select a class:", font=("Georgia", 20, "bold"), fill="black")
    cv.create_text(281, 270, text="Select a class:", font=("Georgia", 20, "bold"), fill="#918e89")

    classes = ["Sorceress", "Druid", "Amazon", "Paladin", "Barbarian", "Necromancer", "Assassin"]
    class_combobox = ttk.Combobox(screen, values=classes, state="readonly", font=("Georgia", 16), cursor="hand2")
    class_combobox.current(0)
    class_combobox.bind("<<ComboboxSelected>>", lambda event, c=class_combobox, i=image_label, : on_class_combobox_change(c, i))
    cv.create_window(501, 270, window=class_combobox, width=200)

    # Randomize class row
    button_image = Image.open("button.png")
    button_image = button_image.resize((220, 50), Image.Resampling.LANCZOS)
    button_photo = ImageTk.PhotoImage(button_image)
    
    cv.create_text(473, 403, text="If you want an absolutely random\nexperience,let the class to be\nrandomized as well", font=("Georgia", 16, "bold"), fill="black")
    cv.create_text(470, 400, text="If you want an absolutely random\nexperience,let the class to be\nrandomized as well.", font=("Georgia", 16, "bold"), fill="#b0b0b0")
    is_randomized_text = cv.create_text(160, 440, text="", font=("Georgia", 14, "bold"), fill="#07da63")
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(screen, text="Randomize class", font=("Georgia", 16, "bold"), variable=checkbox_var, command=lambda: on_class_checkbox_change(checkbox_var, class_combobox, cv, is_randomized_text), cursor="hand2", bg="#222222", fg="#b0b0b0")
    checkbox.image = button_photo
    cv.create_rectangle(49,378, 271, 422, fill="black")
    cv.create_window(160, 400, window=checkbox)
    
    # Create character button
    create_character_button = tk.Button(screen, image=button_photo, compound="center", fg="#cfc8b8", bg="#100605", text="Create character", font=("Georgia", 14, "bold"),  borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", cursor="hand2", command=lambda: create_new_character(class_combobox.get(), checkbox_var.get(), create_character_entry.get(), cv, error_text))
    create_character_button.image = button_photo
    cv.create_window(350, 500, window=create_character_button)
    error_text = cv.create_text(350, 550, text="", font=("Georgia", 18, "bold"), fill="red")

    cv.create_rectangle(60, 580, 633, 583, fill="black")
    
    cv.create_text(354, 624, text="Load character", font=("Georgia", 30, "bold"), fill="black")
    cv.create_text(350, 620, text="Load character", font=("Georgia", 30, "bold"), fill="#b0b0b0")
    

    # Enter character name row
    # cv.create_text(263, 723, text="Character name:", font=("Georgia", 20, "bold"), fill="black")
    # cv.create_text(260, 720, text="Character name:", font=("Georgia", 20, "bold"), fill="#918e89") #720
    # load_character_entry = tk.Entry(random_build_screen_1, width=18, font=("Georgia", 16), bg="#222222", fg="#b0b0b0")
    # cv.create_window(520, 720, window=load_character_entry)

    cv.create_text(353, 703, text="You can load a character that was already created \nbefore in the app. Choose the JSON file that \nrepresents the character you want to upload", font=("Georgia", 16, "bold"), fill="black")
    cv.create_text(350, 700, text="You can load a character that was already created \nbefore in the app. Choose the JSON file that \nrepresents the character you want to upload", font=("Georgia", 16, "bold"), fill="#b0b0b0")
    # Load character button
    load_character_button = tk.Button(screen, image=button_photo, compound="center", fg="#cfc8b8", bg="#100605", text="Load character", font=("Georgia", 14, "bold"),  borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", cursor="hand2", command=open_file)
    load_character_button.image = button_photo
    cv.create_window(350, 797, window=load_character_button)

    screen.pack(fill=tk.BOTH, expand=True)

# def show_ch1_main_screen(frames, screen):
#     print("HI")
#     random_build(frames, ch1_main_top_screen, ch1_main_bottom_screen, character)


skill_tree_background_photo = None
images = None
top_subframe_background_photo = None

def random_build(frames, top_subframe, bottom_subframe, character):

    # Configure grid layout (3 columns)
    for i in range(3):
        top_subframe.grid_columnconfigure(i, weight=1)

    # Add a widget that spans across the top 3 columns
    merged_label = tk.Label(top_subframe, text=f"Your current {character.__class__.__name__} skill tree", bg="black", fg="#b0b0b0", font=("Georgia", 18, "bold"))
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
    global images
    images = [[],[],[]]

    for i in range(3):
        for path in image_paths[i]:
            skill_image = Image.open(path)
            skill_image = skill_image.resize((70, 70), Image.Resampling.LANCZOS)
            skill_photo = ImageTk.PhotoImage(skill_image)
            # skill_photo.image = skill_image
            images[i].append(skill_photo)

    # Define specific connections between buttons using pairs of coordinates

    skill_tree_background_path = "skill_tree_background.png"  # Path to your image file
    skill_tree_background_image = Image.open(skill_tree_background_path)
    # lines_image = lines_image.resize((318, 627), Image.Resampling.LANCZOS)  # Resize the image to fit the frame
    global skill_tree_background_photo
    skill_tree_background_photo = ImageTk.PhotoImage(skill_tree_background_image)

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
        canvas.create_image(0, 0, image=skill_tree_background_photo, anchor="nw")
            
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

                    # skill_image_label = tk.Label(top_subframe, image=images[col][skill_count], highlightthickness=0, bg="#0b0b09")
                    # canvas.create_window(x, y, window=skill_image_label, anchor="nw")
                    # skill_image_label.image = images[col][skill_count]
                    image_object = canvas.create_image(x, y, image=images[col][skill_count], anchor="nw")
                    # image_object.image = images[col][skill_count]
                    # skill_image_objects[col].append(image_object)
                    rectangle = canvas.create_rectangle(0, 0, 0, 0, width=10, fill="black")
                    text = canvas.create_text(0, 0, font=("Courier New", 14, "bold"), fill="#cfc8b8")
                    # rectangle = canvas.create_rectangle(x+54, y+54, x+64, y+64, width=10, fill="black")
                    # text = canvas.create_text(x+60, y+60, text="+", font=("Courier New", 14), fill="#cfc8b8")
                    skill_level_rectangles[col].append(rectangle)
                    skill_level_texts[col].append(text)
                    skill_count += 1
        # for r in range(6):
        #     for c in range(3):
        #         print(skill_image_objects[col][skill_count])
        #     print("")
        canvas.create_text(canvas_width // 2+3, y_offset - 40 + 3, text=character.skill_trees[col].name, font=("Georgia", 20, "bold"), fill="black")
        canvas.create_text(canvas_width // 2, y_offset - 40, text=character.skill_trees[col].name, font=("Georgia", 20, "bold"), fill="#918e89")

    # import random
    # for i in range(3): # skill trees
    #     for j, skill in enumerate(character.skill_trees[i].skills):
    #         character.skill_trees[i].skills[j].base_level = random.randint(0, 99)

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
    # bottom_subframe.pack(fill=tk.X)

    bottom_subframe.grid_rowconfigure(0, weight=1)
    bottom_subframe.grid_rowconfigure(1, weight=1)
    bottom_subframe.grid_rowconfigure(2, weight=1)
    bottom_subframe.grid_columnconfigure(0, weight=1)
    bottom_subframe.grid_columnconfigure(1, weight=0)
    bottom_subframe.grid_columnconfigure(2, weight=0)
    bottom_subframe.grid_columnconfigure(3, weight=1)

    # Add buttons to the bottom_subframe (unchanged)
    lvl_up_image = Image.open("button.png")
    lvl_up_image = lvl_up_image.resize((200, 40), Image.Resampling.LANCZOS)
    lvl_up_photo = ImageTk.PhotoImage(lvl_up_image)
    level_up_btn = tk.Button(bottom_subframe, text="Level up", image=lvl_up_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=200, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    level_up_btn.image = lvl_up_photo
    add_skill_btn = tk.Button(bottom_subframe, text="Add one skill", image=lvl_up_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=200, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    add_skill_btn.image = lvl_up_photo
    
    undo_image = Image.open("button_110.png")
    undo_image = undo_image.resize((100, 40), Image.Resampling.LANCZOS)
    undo_photo = ImageTk.PhotoImage(undo_image)
    undo_btn = tk.Button(bottom_subframe, text="Undo", image=undo_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=100, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    undo_btn.image = undo_photo

    # Add additional buttons (unchanged)
    new_char_image = Image.open("button_300.png")
    new_char_image = new_char_image.resize((230, 40), Image.Resampling.LANCZOS)
    new_char_photo = ImageTk.PhotoImage(new_char_image)
    new_char_btn = tk.Button(bottom_subframe, text="New character", image=new_char_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=230, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    new_char_btn.image = new_char_photo

    import_char_image = Image.open("button_300.png")
    import_char_image = import_char_image.resize((230, 40), Image.Resampling.LANCZOS)
    import_char_photo = ImageTk.PhotoImage(import_char_image)
    import_char_btn = tk.Button(bottom_subframe, text="Import character", image=import_char_photo, font=("Georgia", 10, "bold"), compound="center", fg="#cfc8b8", bg="#100605", width=230, height=40, borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken")
    import_char_btn.image = import_char_photo

    # Place buttons in the bottom_subframe (unchanged)
    level_up_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    add_skill_btn.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    undo_btn.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    new_char_btn.grid(row=0, column=3, padx=10, pady=10, sticky="e")
    import_char_btn.grid(row=1, column=3, padx=10, pady=10, sticky="e")

    # next_stats_label = tk.Label(bottom_subframe, text=f"Current stats\n\n{character.strength} strength\n{character.dexterity} dexterity\n{character.vitality} vitality\n{character.energy} energy", font=("Georgia", 10, "bold"), height=2, bg="grey", fg="white")
    # next_stats_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky="nsew")


    # ----
    canvas_width, canvas_height = 185, 275
    level_up_canvas = tk.Canvas(bottom_subframe, width=canvas_width, height=canvas_height, bg="white")
    level_up_canvas.grid(row=0, column=2, rowspan=3, pady=10, padx=10)

    # Determine the total content size (based on 3x6 grid and button size)
    content_width, content_height = 3 * 80, 6 * 80  # Each button is 80x80 including padding

    # Calculate the offset for centering the content within the canvas
    x_offset = (canvas_width - content_width) // 2
    y_offset = (canvas_height - content_height) // 2

    # Add background image to the canvas, centered

    level_up_image = Image.open("character_load_background.png")
    level_up_image = level_up_image.resize((185, 275), Image.Resampling.LANCZOS)
    global level_up_photo
    level_up_photo = ImageTk.PhotoImage(level_up_image)
    level_up_canvas.create_image(0, 0, image=level_up_photo, anchor="nw")
    level_up_canvas_width = level_up_canvas.winfo_reqwidth()
    # Lv. X stats
    offset = 19
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 15 + 3 + offset, text="Lv. 3 stats", font=("Georgia", 14, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 15 + offset, text="Lv. 3 stats", font=("Georgia", 14, "bold"), fill="#918e89")
    # Strength
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 35 + 3 + offset, text="1 strength", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 35 + offset, text="1 strength", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Dexterity
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 55 + 3 + offset, text="2 dexterity", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 55 + offset, text="2 dexterity", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Vitality
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 75 + 3 + offset, text="0 vitality", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 75 + offset, text="0 vitality", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Energy
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 95 + 3 + offset, text="2 energy", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 95 + offset, text="2 energy", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Lv. X skill
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 135 + 3 + offset, text="Lv. 3 skill", font=("Georgia", 14, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 135 + offset, text="Lv. 3 skill", font=("Georgia", 14, "bold"), fill="#918e89")
    # Skill name
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 155 + 3 + offset, text="Leap", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 155 + offset, text="Leap", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # ---- 
    # ----
    canvas_width, canvas_height = 185, 275
    level_up_canvas = tk.Canvas(bottom_subframe, width=canvas_width, height=canvas_height, bg="white")
    level_up_canvas.grid(row=0, column=1, rowspan=3, pady=10, padx=10)

    # Determine the total content size (based on 3x6 grid and button size)
    content_width, content_height = 3 * 80, 6 * 80  # Each button is 80x80 including padding

    # Calculate the offset for centering the content within the canvas
    x_offset = (canvas_width - content_width) // 2
    y_offset = (canvas_height - content_height) // 2

    # Add background image to the canvas, centered

    level_up_canvas.create_image(0, 0, image=level_up_photo, anchor="nw")
    level_up_canvas_width = level_up_canvas.winfo_reqwidth()
    # Lv. X stats
    offset = 47
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 15 + 3 + offset, text="Current stats", font=("Georgia", 14, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 15 + offset, text="Current stats", font=("Georgia", 14, "bold"), fill="#918e89")
    # Strength
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 35 + 3 + offset, text=f"{character.strength} strength", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 35 + offset, text=f"{character.strength} strength", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Dexterity
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 55 + 3 + offset, text=f"{character.dexterity} dexterity", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 55 + offset, text=f"{character.dexterity} dexterity", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Vitality
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 75 + 3 + offset, text=f"{character.vitality} vitality", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 75 + offset, text=f"{character.vitality} vitality", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # Energy
    level_up_canvas.create_text(level_up_canvas_width / 2 + 3, 95 + 3 + offset, text=f"{character.energy} energy", font=("Georgia", 12, "bold"), fill="black")
    level_up_canvas.create_text(level_up_canvas_width / 2, 95 + offset, text=f"{character.energy} energy", font=("Georgia", 12, "bold"), fill="#b0b0b0")
    # ----
    
    # TODO: create normal background texture for the current stats and level up stats canvases

    # current_stats_label = tk.Label(bottom_subframe, text="Lv. 3 stats:\n1 strength\n3 dexterity\n0 vitality\n1 energy\n\nLv. 3 skill:\nIce Bolt", font=("Georgia", 10, "bold"), height=2, bg="grey", fg="white")
    # current_stats_label.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")
    for frame in frames:
        frame.pack_forget()
    top_subframe.pack(fill=tk.BOTH, expand=True)
    bottom_subframe.pack(fill=tk.BOTH)

# --- Main Window --- #
root = tk.Tk()
root.title("Zarfen Diablo II Challenges")
root.geometry("1280x1000")
root.resizable(False, False)

# --- Header --- #
header_frame = tk.Frame(root, height=75)
header_frame.pack(fill=tk.X, side=tk.TOP)

image_path = "header.png"
image = Image.open(image_path)
image = image.resize((1280, 75), Image.Resampling.LANCZOS)
header_photo = ImageTk.PhotoImage(image)

header_pic = tk.Label(header_frame, image=header_photo)
header_pic.place(relwidth=1, relheight=1)

title_label = tk.Label(header_frame, text="Zarfen Diablo II Challenges", font=("Georgia", 22, "bold"), height=2, bg="#100605", fg="#ffb955")
title_label.pack()


# --- Side Panel --- #
side_panel_frame = tk.Frame(root, width=200, bg="#100605")
side_panel_frame.pack(fill=tk.Y, side=tk.LEFT)

# --- Main Menu --- #
main_menu_frame = tk.Frame(root, bg="yellow")
content_frames.append(main_menu_frame)

# --- Random Build --- #
ch1_character_creation_screen = tk.Frame(root, bg="red")
content_frames.append(ch1_character_creation_screen)

ch1_main_top_screen = tk.Frame(root, bg="black")
content_frames.append(ch1_main_top_screen)

ch1_main_bottom_screen = tk.Frame(root, bg="black", height=350)
content_frames.append(ch1_main_bottom_screen)

main_menu(content_frames, main_menu_frame)

buttons = ["Main Menu", "Random Build"]
functions = [
    lambda: main_menu(content_frames, main_menu_frame), 
    lambda: show_ch1_character_creation_screen(content_frames, ch1_character_creation_screen)
]
button_image = tk.PhotoImage(file="button.png")
for i in range(len(buttons)):
    button = tk.Button(side_panel_frame, text=buttons[i], image=button_image, compound="center", fg="#cfc8b8", bg="#100605", font=("Georgia", 14, "bold"), borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken", command=functions[i], cursor="hand2")
    button.pack(fill=tk.X, pady=1, padx=10)

# Run the Tkinter event loop
root.mainloop()