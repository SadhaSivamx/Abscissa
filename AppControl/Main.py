import customtkinter as ctk
from PIL import Image, ImageTk
import warnings

# Cancelling warnings
warnings.filterwarnings('ignore')

# Main application
root = ctk.CTk()
ctk.set_appearance_mode("light")
root.title("Abscissa")
root.iconbitmap("Dino.ico")
root.resizable(width=False,height=False)
root.geometry("600x400")

def load_image(file_path):
    image = Image.open(file_path)

    # Resize image to fill the entire space allocated to it
    new_width = int(root.winfo_height() * 1.0)  # Half of the window width
    new_height = int(root.winfo_height() * 0.95)  # 95% of the height
    image = image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    return photo

def print_values():
    # Gather slider values and toggle value
    slider_values = [slider.get() for slider in sliders]
    toggle_value = toggle_button.get()

    # Print values
    print("Slider Values:", slider_values)
    print("Toggle Value:", toggle_value)

# Load and display the image
ImgLabel = ctk.CTkLabel(root, image=load_image("Arm.png"), corner_radius=10,text=None)
ImgLabel.grid(row=0, column=0, padx=5, pady=10, sticky="nw")

# Create a frame for sliders and toggle button
slider_frame = ctk.CTkFrame(root)
slider_frame.grid(row=0, column=1, padx=5, pady=10, sticky="ns")

# List to hold slider references
sliders = []

# Create and place sliders with labels
for i in range(1, 5):
    label = ctk.CTkLabel(slider_frame, text=f"Motor {i}")
    label.pack(pady=(10, 0))

    slider = ctk.CTkSlider(slider_frame)
    slider.pack(fill="x", padx=10, pady=(0, 10))  # Fill width
    sliders.append(slider)  # Add slider to the list

# Add a toggle button
toggle_button = ctk.CTkSwitch(slider_frame, text="Toggle Gripper")
toggle_button.pack(pady=10)

# Add a button to print values
print_button = ctk.CTkButton(slider_frame, text="Set Arm 🚀", command=print_values)
print_button.pack(pady=20)

# Set the column weights to allow the layout to adjust
root.grid_columnconfigure(0, weight=1)  # Image column
root.grid_columnconfigure(1, weight=0)  # Sliders column

# Update the image on window resize
def update_image(event):
    ImgLabel.configure(image=load_image("Arm.png"))

root.bind("<Configure>", update_image)

# Main application UI
root.mainloop()
