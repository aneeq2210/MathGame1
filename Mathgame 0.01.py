import tkinter as tk

class MathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sum-thing")#Window Title
        self.root.geometry("600x500") #window size
        self.root.configure(bg="#89d8e8") #background colour
        
        #Welcome banner
        tk.Label(root, text="Welcome to Sum-thing!", 
                font=("Comic Sans MS", 25), bg="#ccf5fc").pack(pady=100)

if __name__ == "__main__":
    root = tk.Tk()
    mathgame = MathGame(root)
    root.mainloop()
