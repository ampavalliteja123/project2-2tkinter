import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def get_date():
    selected_date = cal.get_date()
    date_label.config(text="Selected Date: " + selected_date)

# Step 2: Create the Tkinter window and configure its properties
root = tk.Tk()
root.title("calendar")
root.geometry("600x600")

# Step 3: Create the Calendar widget
cal = Calendar(root, selectmode="day", date_pattern="dd/MM/yyyy")
cal.pack(pady=20)

# Step 5: Create a button to trigger date selection and link it to the get_date() function
select_button = ttk.Button(root, text="get_date", command=get_date)
select_button.pack(pady=20)

# Step 6: Create a label to display the selected date
date_label = ttk.Label(root, text="Selected Date: ")
date_label.pack(pady=20)

# Step 7: Run the Tkinter event loop
root.mainloop()
