import tkinter as tk
from PIL import Image, ImageTk
import os

class DesktopPet:
    def __init__(self, gif_file):
        self.gif_file = gif_file
        self.window = tk.Tk()
        self.window.title("Desktop Pet")
        self.window.geometry("250x300")

        # Load the GIF image
        self.load_gif()

        # Create a canvas and display the GIF image in it
        self.canvas = tk.Canvas(self.window, width=self.gif_width, height=self.gif_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.gif_frames[0])

        # Add mouse and keyboard controls to move and interact with the pet
        self.pet_x = 0
        self.pet_y = 0
        self.canvas.bind('<Up>', lambda event: self.move_pet(0, -10))
        self.canvas.bind('<Down>', lambda event: self.move_pet(0, 10))
        self.canvas.bind('<Left>', lambda event: self.move_pet(-10, 0))
        self.canvas.bind('<Right>', lambda event: self.move_pet(10, 0))
        self.canvas.bind('<space>', lambda event: self.interact_with_pet())

        # Set up the animation loop
        self.current_frame = 0
        self.animating = True
        self.animate()

    def load_gif(self):
        """Load the GIF file and extract its frames."""
        self.gif_image = Image.open(self.gif_file)
        self.gif_width, self.gif_height = self.gif_image.size
        self.gif_frames = []
        try:
            while True:
                self.gif_frames.append(ImageTk.PhotoImage(self.gif_image))
                self.gif_image.seek(len(self.gif_frames))
        except EOFError:
            pass

    def animate(self):
        """Animate the GIF frames."""
        if self.animating:
            self.canvas.itemconfig(1, image=self.gif_frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
            self.window.after(50, self.animate)

    def move_pet(self, x, y):
        """Move the pet to a new position."""
        self.pet_x += x
        self.pet_y += y
        self.canvas.move(1, x, y)

    def interact_with_pet(self):
        """Interact with the pet."""
        print("You clicked the pet!")

    def run(self):
        """Run the tkinter event loop."""
        self.window.mainloop()

if __name__ == '__main__':
    # Set the path to your GIF file
    gif_path = "ki233308.gif"

    # Check if the GIF file exists
    if os.path.exists(gif_path):
        # Create a DesktopPet object and run it
        pet = DesktopPet(gif_path)
        pet.run()
    else:
        print(f"Error: The file '{gif_path}' does not exist.")