from tkinter import *
from tkinter import ttk

# def get_input():
#     user_input = entry_widget.get()  # Retrieve the text from the Entry widget
#     print(f"User entered: {user_input}")

root = Tk()
root.title("TradeCalc")
root.geometry("800x600")
root.config(bg="lightgrey")

frame1 = Frame(root,
               borderwidth=3,
               width=600,
               height=100,
               relief=RAISED,
               bg="lightgrey",
               highlightbackground="black",
               highlightcolor="black",
               highlightthickness=3)
frame1.pack(pady=20)

label = Label(frame1, 
              text="TRADECALC", 
              anchor=CENTER,
              bg="lightgrey",
              height=1,
              width=13,
              font=("Circular", 75),
              fg="black")     
label.pack()

combo_box = ttk.Combobox(root, values=["Stop-Loss Calculation", "Take Profit Calculation", "Reward:Risk Calculation", "Deriv Accumulator Calculation"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("Stop-Loss Calculation")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>")

root.mainloop()
