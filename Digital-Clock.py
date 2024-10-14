import sys
from tkinter import *
import time

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, times)

# Initialize root window
root = Tk()
root.geometry('500x300')
root.title("Digital Clock")
root.configure(bg='#2C3E50')  # Dark background color

# Create clock title
digi = Label(root, text='Digital Clock', font=("Helvetica", 28, "bold"), bg='#2C3E50', fg='#E74C3C')
digi.pack(pady=10)  # Center the title and give space above

# Create clock display
clock = Label(root, font=("Helvetica", 50, "bold"), bg="#ECF0F1", fg="#2C3E50", padx=10, pady=10)
clock.pack(pady=20)  # Center the clock and space it evenly
times()

# Add label for hours, minutes, seconds
nota = Label(root, text='Hours    Minutes    Seconds', font=("Helvetica", 20), bg='#2C3E50', fg='#ECF0F1')
nota.pack(pady=10)  # Center the label and space it evenly

# Run the application
root.mainloop()
