from tkinter import messagebox
import ttkbootstrap as ttk
from backend.utils import BOOKS_FILE, MEMBERS_FILE, BOOK_SHELF_FILE, DESHELVED_BOOKS_FILE, save_data
from ui.login_screen import login_screen
from backend.books import Books
from backend.members import Members
from backend.shelfing import BookShelf, DeshelvedBooks

def on_close():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        print("App is closing. Saving data...")
        save_data(Books, BOOKS_FILE)
        save_data(Members, MEMBERS_FILE)
        save_data(BookShelf, BOOK_SHELF_FILE)
        save_data(DeshelvedBooks, DESHELVED_BOOKS_FILE)
        app.destroy()

app = ttk.Window(themename="darkly")
app.geometry("1200x800") 
app.state('zoomed')
app.title("LibPro | Library Management App")

app.protocol("WM_DELETE_WINDOW", on_close)

style = ttk.Style()
style.configure("crimson.TButton",
                background="#dc143c", 
                foreground="white",  
                borderwidth=0,
                focusthickness=0)

login_screen(app)
app.mainloop()