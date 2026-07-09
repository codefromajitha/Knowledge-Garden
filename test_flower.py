import tkinter as tk
from PIL import Image, ImageTk

# Create the window
window = tk.Tk()
window.title("Knowledge Garden")
window.geometry("400x400")

# Load the flower image
flower = "amethyst_rose"

image = Image.open(f"flower_images/{flower}.png")

# Resize it
image = image.resize((200, 200))

photo = ImageTk.PhotoImage(image)

# Put it on the window
label = tk.Label(window, image=photo)
label.image = photo
label.pack(expand=True)

window.mainloop()