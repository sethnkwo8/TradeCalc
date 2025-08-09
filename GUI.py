import customtkinter as ctk

# ---------- Helper Function ----------
def create_row(parent, label_text, widget,row):
    """Creates a label and widget in a horizontal row using grid."""
    label = ctk.CTkLabel(
        parent,
        text=label_text,
        font=("Times New Roman", 25)
    )
    label.grid(row=row, column=1, padx=60, pady=10, sticky="e")

    widget.grid(row=row, column=2, padx=10, pady=10, sticky="w")

def create_output(parent, label_text, row):
    label = ctk.CTkLabel(
        parent,
        text=label_text,
        font=("Times New Roman", 25)
    )
    label.grid(row=row, column=0, padx=60, pady=10, sticky="w")

# ---------- Main Window ----------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("TradeCalc")
root.geometry("800x600")  # Fullscreen-ish but resizable

# Top Logo Frame
top_logo = ctk.CTkFrame(root, width=600, height=100, fg_color="lightgrey", border_color="black", border_width=3)
top_logo.pack(pady=10)
top_logo.pack_propagate(False)

top_logo_label = ctk.CTkLabel(top_logo, 
                              text="TRADECALC",
                              font=("Circular", 75),
                              text_color="black",
                              )
top_logo_label.pack(expand = True)

main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=True, fill="both", pady=20)

# ---------- Widgets ----------
# Mode ComboBox
mode_combo = ctk.CTkComboBox(
    main_frame,
    width=400,
    font=("Times New Roman", 22),
    corner_radius=10,
    values=[
        "Stop-Loss Calculation", 
        "Take Profit Calculation",
        "Reward to Risk Calculation", 
        "Deriv Accumulator Calculation"
    ],
    state='readonly'
)
mode_combo.set("Stop-Loss Calculation")
create_row(main_frame, "Mode:", mode_combo, row=0)

# Entry Price
entry_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
create_row(main_frame, "Entry Price:", entry_price, row=1)

# Stop Loss %
stop_loss_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
create_row(main_frame, "Stop-Loss (%):", stop_loss_entry, row=2)

# Position Size
position_size_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
create_row(main_frame, "Position Size:", position_size_entry, row=3)

# Trade Direction ComboBox
trade_dir_combo = ctk.CTkComboBox(
    main_frame,
    width=400,
    font=("Times New Roman", 22),
    values=["Long", "Short"],
    state='readonly'
)
trade_dir_combo.set("Long")
create_row(main_frame, "Trade Direction:", trade_dir_combo, row=4)

# ---------- Calculate Button ----------
calc_button = ctk.CTkButton(
    main_frame,
    width=200,
    height=50,
    text="Calculate",
    fg_color="lightgrey",
    hover_color="grey",
    text_color="black",
    font=("Arial", 24),
    border_width=2,
    border_color="black"
)
calc_button.grid(row=5, column=1, columnspan=2, pady=30, padx=100)

# ---------- Output ----------
output = ctk.CTkFrame(main_frame,
                      width=600,
                      height=150,
                      fg_color="lightgrey",
                      border_color="black",
                      border_width=3
                      )
output.grid(row=6, column=1, columnspan=2, pady=10)
output.grid_propagate(False)

output1 = create_output(output, "Stop Loss Price:", row=0)
output2 = create_output(output, "Risk Per Unit:", row=1)
output3 = create_output(output, "Potential Loss:", row=2)



# ---------- Run ----------
root.mainloop()
