from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

class WatermarkApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Image Watermark App")
        
        # Create the canvas for displaying the image
        self.canvas = Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        
        # Create the menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        file_menu = Menu(menubar)
        file_menu.add_command(label="Open Image", command=self.open_image)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Create the watermark text input
        self.watermark_entry = Entry(self.master)
        self.watermark_entry.pack()
        
        # Create the watermark button
        self.watermark_button = Button(self.master, text="Add Watermark", command=self.add_watermark)
        self.watermark_button.pack()
        
        # Set the initial values of the image and watermark text
        self.image = None
        self.watermark_text = ""
        # Create a "Save Image" button
        self.save_button = Button(self.master, text="Save Image", command=self.save_image)
        self.save_button.pack()
        
        

    def open_image(self):
        # Open a file dialog to select an image file
        filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
        
        # Load the selected image and display it on the canvas
        self.image = Image.open(filepath)
        self.image = self.image.resize((400, 400))
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)
    
    def add_watermark(self):
        # Get the watermark text from the entry widget
        self.watermark_text = self.watermark_entry.get()
        
        # Check if an image and watermark text have been selected
        if self.image is None or self.watermark_text == "":
            return
        
        # Add the watermark to the image
        font = ImageFont.truetype("arial.ttf", 36)
        draw = ImageDraw.Draw(self.image)
        draw.text((10, 10), self.watermark_text, font=font)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)

    def save_image(self):
        # Open a file dialog to select a file name and location for the edited image
        filepath = filedialog.asksaveasfilename(defaultextension=".png")
    
        # Save the edited image
        self.image.save(filepath)

    
root = Tk()
app = WatermarkApp(root)
root.mainloop()
