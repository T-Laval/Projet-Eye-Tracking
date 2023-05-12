import tkinter as tk

# Create a window
root = tk.Tk()

# Create a text widget
text = tk.Text(root)

# Create a list of words
words = ["apple", "banana", "cherry", "durian", "eggplant"]

# Create a function to display word suggestions
def show_suggestions(event):
    # Get the current word
    current_word = text.get("1.0", "end-1c")

    # Get the suggestions for the current word
    suggestions = [word for word in words if word.startswith(current_word)]

    # Clear the suggestions listbox
    suggestions_listbox.delete(0, tk.END)

    # Add the suggestions to the suggestions listbox
    for suggestion in suggestions:
        suggestions_listbox.insert(tk.END, suggestion)

# Bind the show_suggestions function to the <KeyRelease> event
text.bind("<KeyRelease>", show_suggestions)

# Create a listbox for the suggestions
suggestions_listbox = tk.Listbox(root)

# Pack the text widget and the listbox
text.pack()
suggestions_listbox.pack()

# Start the mainloop
root.mainloop()
