import tkinter as tk
from tkinter import messagebox

class MathGame:
    def __init__(mathsgame, screen):
       #starting the main game window
        mathsgame.screen = screen
        mathsgame.screen.title("Sum-thing")  #setting window name
        mathsgame.screen.geometry("600x600")  #size
        mathsgame.screen.configure(bg="light blue")  #background color
        
        
        mathsgame.username = ""  #storing the username
        
        #displaying the welcome screen
        mathsgame.show_welcome_screen()
    
    def clear_screen(mathsgame):
        """Remove all widgets from the window"""
        for widget in mathsgame.screen.winfo_children():
            widget.destroy()
    
    def show_welcome_screen(mathsgame):
        """Display username entry screen"""
        mathsgame.clear_screen()
        
        # Welcome label
        tk.Label(mathsgame.screen, 
                text="Welcome to Sum-thing!",
                font=("Arial", 24),
                bg="#f0f0f0").pack(pady=30)
        
        # Username entry
        tk.Label(mathsgame.screen, 
                text="Enter username:",
                font=("Arial", 12),
                bg="#f0f0f0").pack()
        
        mathsgame.username_entry = tk.Entry(mathsgame.screen, font=("Arial", 12))
        mathsgame.username_entry.pack(pady=10)
        
        # Start button
        tk.Button(mathsgame.screen,
                text="Start",
                command=mathsgame.save_username,
                font=("Arial", 14),
                bg="#4CAF50",  
                fg="white").pack(pady=20)
    
    def save_username(mathsgame):
        """Validate and save username"""
        mathsgame.username = mathsgame.username_entry.get()
        if not mathsgame.username:
            messagebox.showwarning("Oops", "Please enter a username!")
        else:
            print(f"Username saved: {mathsgame.username}")  

if __name__ == "__main__":
    root = tk.Tk()
    game = MathGame(root)
    root.mainloop()
