import tkinter as tk
import mouse

def on_key_press(event):
    if event.keysym == "F11":
        mouse.click()
        #print("Mouse clicked at ({}, {})".format(event.x, event.y))

root = tk.Tk()

# Bind the key press event to the on_key_press function
root.bind("<F11>", on_key_press)

def on_click(event):
  print("Button clicked!")

# Create a button
tk.Button(root, text="Click Me!",command=on_click).pack()


# Start the main loop
root.mainloop()
