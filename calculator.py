import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def on_enter(e):
    e.widget["bg"] = "#d1d1d1"

def on_leave(e):
    e.widget["bg"] = "#f0f0f0"

root = tk.Tk()
root.title("Fancy Calculator")
root.geometry("320x450")
root.configure(bg="#ffffff")

# Entry
entry = tk.Entry(root, font="Helvetica 24", bd=5, relief=tk.FLAT, justify='right', bg="#eeeeee")
entry.pack(padx=20, pady=20, fill=tk.BOTH, ipady=10)

# Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

button_frame = tk.Frame(root, bg="#ffffff")
button_frame.pack(padx=10, pady=10)

for row in buttons:
    frame = tk.Frame(button_frame, bg="#ffffff")
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Helvetica 18", bg="#f0f0f0", fg="#333333",
                        relief="flat", activebackground="#d1d1d1", padx=10, pady=10)
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

root.mainloop()
