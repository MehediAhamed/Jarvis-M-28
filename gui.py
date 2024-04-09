
import tkinter as tk
from PIL import Image, ImageTk
import subprocess

proc = None  

def run_program():
    global proc
    proc = subprocess.Popen(['python', 'jarvis.py'])

def on_closing():
    global proc
    if proc:
        proc.terminate()
    app.destroy()

app = tk.Tk()
app.title("Jarvis-M 28 Desktop App")
app.geometry("800x600") 

gif_frames = []
gif = Image.open("./m.gif")
try:
    while True:
        gif_frames.append(ImageTk.PhotoImage(gif.copy()))
        gif.seek(len(gif_frames))  # Move to next frame
except EOFError:
    pass  

def animate_gif(frame_num=0):
    frame = gif_frames[frame_num]
    background_label.configure(image=frame)
    app.after(100, animate_gif, (frame_num + 1) % len(gif_frames))

# Create a label to display the GIF image as the background
background_label = tk.Label(app)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

animate_gif()

label = tk.Label(app, text="Click the button to run the program", padx=10, pady=10, font=("Helvetica", 18), fg="white", bg="black")
label.pack()

button = tk.Button(app, text="Start", command=run_program, font=("Helvetica", 14), bg="#6b0505", fg="white")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 

app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()
