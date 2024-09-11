import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
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

def on_class_checkbox_change(is_randomized, combobox):
    if is_randomized.get():
        combobox.config(state="disabled")
    else:
        combobox.config(state="enabled")

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

# lambda: random_build(content_frames, top_subframe, bottom_subframe)
def random_build_load_screen(frames, random_build_screen_1):
    for frame in frames:
        frame.pack_forget()

    c_width = 1056
    c_height = 926
    cv = tk.Canvas(random_build_screen_1, width=c_width, height=c_height, highlightthickness=0)
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
    
    image_label = tk.Label(random_build_screen_1, image=character_photo, highlightthickness=0, bg="#0b0b09")
    cv.create_window(815, 400, window=image_label)
    image_label.image = character_photo

    # Character creation row
    cv.create_text(354, 124, text="Create character", font=("Georgia", 30, "bold"), fill="black")
    cv.create_text(350, 120, text="Create character", font=("Georgia", 30, "bold"), fill="#b0b0b0")
    text_entry = tk.Entry(random_build_screen_1, width=18, font=("Georgia", 16))
    cv.create_window(520, 220, window=text_entry)


    # Enter character name row
    cv.create_text(223, 223, text="Enter character name:", font=("Georgia", 20, "bold"), fill="black")
    cv.create_text(220, 220, text="Enter character name:", font=("Georgia", 20, "bold"), fill="#918e89")
    text_entry = tk.Entry(random_build_screen_1, width=18, font=("Georgia", 16), bg="#222222", fg="#b0b0b0")
    cv.create_window(520, 220, window=text_entry)

    # Select a class row
    cv.create_text(284, 273, text="Select a class:", font=("Georgia", 20, "bold"), fill="black")
    cv.create_text(281, 270, text="Select a class:", font=("Georgia", 20, "bold"), fill="#918e89")

    classes = ["Sorceress", "Druid", "Amazon", "Paladin", "Barbarian", "Necromancer", "Assassin"]
    class_combobox = ttk.Combobox(random_build_screen_1, values=classes, state="readonly", font=("Georgia", 16), cursor="hand2")
    class_combobox.current(0)
    class_combobox.bind("<<ComboboxSelected>>", lambda event, c=class_combobox, i=image_label, : on_class_combobox_change(c, i))
    cv.create_window(501, 270, window=class_combobox, width=200)

    # Randomize class row
    button_image = Image.open("button.png")
    button_image = button_image.resize((220, 50), Image.Resampling.LANCZOS)
    button_photo = ImageTk.PhotoImage(button_image)

    cv.create_text(473, 403, text="If you want an absolutely random\nexperience,let the class to be\nrandomized as well", font=("Georgia", 16, "bold"), fill="black")
    cv.create_text(470, 400, text="If you want an absolutely random\nexperience,let the class to be\nrandomized as well.", font=("Georgia", 16, "bold"), fill="#b0b0b0")
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(random_build_screen_1, text="Randomize class", font=("Georgia", 16, "bold"), variable=checkbox_var, command=lambda: on_class_checkbox_change(checkbox_var, class_combobox), cursor="hand2", bg="#222222", fg="#b0b0b0")
    checkbox.image = button_photo
    # cv.create_window(497, 325, window=checkbox)
    cv.create_rectangle(49,378, 271, 422, fill="black")
    cv.create_window(160, 400, window=checkbox)
    
    # Create character button
    create_character_button = tk.Button(random_build_screen_1, image=button_photo, compound="center", fg="#cfc8b8", bg="#100605", text="Create character", font=("Georgia", 14, "bold"),  borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", cursor="hand2")
    create_character_button.image = button_photo
    cv.create_window(350, 500, window=create_character_button)
    
    cv.create_rectangle(60, 580, 633, 583, fill="black")
    
    cv.create_text(354, 624, text="Load character", font=("Georgia", 30, "bold"), fill="black")
    cv.create_text(350, 620, text="Load character", font=("Georgia", 30, "bold"), fill="#b0b0b0")

    # Enter character name row
    cv.create_text(263, 723, text="Character name:", font=("Georgia", 20, "bold"), fill="black")
    cv.create_text(260, 720, text="Character name:", font=("Georgia", 20, "bold"), fill="#918e89") #720
    text_entry = tk.Entry(random_build_screen_1, width=18, font=("Georgia", 16), bg="#222222", fg="#b0b0b0")
    cv.create_window(520, 720, window=text_entry)

    # Create character button
    create_character_button = tk.Button(random_build_screen_1, image=button_photo, compound="center", fg="#cfc8b8", bg="#100605", text="Load character", font=("Georgia", 14, "bold"),  borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", cursor="hand2")
    create_character_button.image = button_photo
    cv.create_window(350, 797, window=create_character_button)

    # cv.create_text(313, 403, text="If you want an absolutely random experience,\nlet the class to be randomized as well", font=("Georgia", 16, "bold"), fill="black")
    # cv.create_text(310, 400, text="If you want an absolutely random experience,\nlet the class to be randomized as well.", font=("Georgia", 16, "bold"), fill="#b0b0b0")
    # checkbox_var = tk.BooleanVar()
    # checkbox = tk.Checkbutton(random_build_screen_1, text="Randomize class", font=("Georgia", 16), variable=checkbox_var, command=lambda: on_class_checkbox_change(checkbox_var, class_combobox))
    # # cv.create_window(497, 325, window=checkbox)
    # cv.create_window(307, 460, window=checkbox)

    # label_background
    # # Class setup - Left
        # Class setup - Top Left
    # class_left_top_frame = tk.Frame(class_left_frame, bg="green")
    # class_left_top_frame.pack(side=tk.TOP, padx=20, pady=20)
    # content_frames.append(class_left_top_frame)

    # entry_label_image = Image.open("test.png")
    # # entry_label_image = entry_label_image.resize((239, 22), Image.Resampling.LANCZOS)
    # entry_label_photo = ImageTk.PhotoImage(entry_label_image)

    # entry_label_background = tk.Label(random_build_screen_1, image=entry_label_photo, text="Enter character name:", font=("Georgia", 16), bg="#0b0b09", highlightthickness=0)
    # cv.create_window(220, 220, window=entry_label_background)  # (x=200, y=150)
    # entry_label_background.image = entry_label_photo

    # entry_text = tk.Text(random_build_screen_1, text="Enter character name:", font=("Georgia", 16), fill="#cfc8b8")
    # cv.create_window(200, 400, window=entry_text)  # (x=200, y=150)
    # entry_label.pack(side=tk.LEFT, padx=20, pady=20)

    # entry_text = cv.create_text(220, 220, text="Enter character name:", font=("Georgia", 20, "bold"), fill="#cfc8b8")
    # text_entry.pack(side=tk.LEFT, padx=20, pady=20)

    #     # Class setup - Middle Left
    # class_left_middle_frame = tk.Frame(class_left_frame, bg="aqua")
    # class_left_middle_frame.pack(padx=20, pady=20)
    
    # entry_label = tk.Label(class_left_middle_frame, text="Choose a class:", width=20, height=2, font=("Georgia", 16))
    # entry_label.pack(side=tk.LEFT, padx=20, pady=20)

    # classes = ["Sorceress", "Druid", "Amazon", "Paladin", "Barbarian", "Necromancer", "Assassin"]
    # class_combobox = ttk.Combobox(class_left_middle_frame, values=classes, state="readonly", font=("Georgia", 16))
    # class_combobox.current(0)
    # class_combobox.pack(side=tk.LEFT, padx=20, pady=20)
    # class_combobox.bind("<<ComboboxSelected>>", lambda event, c=class_combobox, i=image_label, : on_class_combobox_change(c, i))

    #     # Class setup - Bottom Left
    # class_left_bottom_frame = tk.Frame(class_left_frame, bg="green")
    # class_left_bottom_frame.pack(side=tk.BOTTOM, padx=20, pady=20)

    # checkbox_var = tk.BooleanVar()
    # checkbox = tk.Checkbutton(class_left_bottom_frame, text="Randomize Class", font=("Georgia", 16), variable=checkbox_var, command=lambda: on_class_checkbox_change(checkbox_var, class_combobox))
    # checkbox.pack(padx=20, pady=20)

    # # Load character
    # load_character_frame = tk.Frame(random_build_screen_1, bg="blue")
    # load_character_frame.pack(side=tk.LEFT, padx=20, pady=20)
    # content_frames.append(load_character_frame)

    # load_character_button = tk.Button(load_character_frame, text="Load character", font=("Georgia", 14))
    # load_character_button.pack(padx=20, pady=20)

    # load_character_name_label = tk.Label(load_character_frame, text="Enter character name:", width=20, height=2, font=("Georgia", 16))
    # load_character_name_label.pack(side=tk.LEFT, padx=20, pady=20)

    # load_character_name_entry = tk.Entry(load_character_frame, width=18, font=("Georgia", 16))
    # load_character_name_entry.pack(side=tk.LEFT, padx=20, pady=20)

    # # Create character
    # create_character_frame = tk.Frame(random_build_screen_1, bg="blue")
    # create_character_frame.pack(side=tk.RIGHT, padx=20, pady=20)
    # content_frames.append(create_character_frame)

    # create_character_button = tk.Button(create_character_frame, text="Create character", font=("Georgia", 14))
    # create_character_button.pack(padx=20, pady=20)

    # error_text = tk.Text(create_character_frame, height=5, width=35, font=("Georgia", 14), fg="red")
    # error_text.insert(tk.END, "A character already exists with the name\n'Gabooor'")
    # error_text.pack(padx=20, pady=20)


    random_build_screen_1.pack(fill=tk.BOTH, expand=True)

def random_build(frames, top_subframe, bottom_subframe):
    # top_subframe.pack(fill=tk.BOTH, expand=True)

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
    # bottom_subframe.pack(fill=tk.X)

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
random_build_screen_1 = tk.Frame(root, bg="red")
content_frames.append(random_build_screen_1)
top_subframe = tk.Frame(root, bg="blue")
content_frames.append(top_subframe)
bottom_subframe = tk.Frame(root, bg="grey", height=350)
content_frames.append(bottom_subframe)

main_menu(content_frames, main_menu_frame)

# Add multiple buttons to the side panel
buttons = ["Main Menu", "Random Build"]
functions = [
    lambda: main_menu(content_frames, main_menu_frame), 
    lambda: random_build_load_screen(content_frames, random_build_screen_1)
]
button_image = tk.PhotoImage(file="button.png")
for i in range(len(buttons)):
    button = tk.Button(side_panel_frame, text=buttons[i], image=button_image, compound="center", fg="#cfc8b8", bg="#100605", font=("Georgia", 14, "bold"), borderwidth=0, highlightcolor="#100605", highlightbackground="#100605", relief="sunken", command=functions[i], cursor="hand2")
    button.pack(fill=tk.X, pady=1, padx=10)

# Run the Tkinter event loop
root.mainloop()