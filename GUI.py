import customtkinter as ctk

ctk.set_appearance_mode("light")  # "dark" or "light"
ctk.set_default_color_theme("blue")  # or "green", "dark-blue", etc.

root = ctk.CTk()
root.title("TradeCalc")
root.geometry("800x800")

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

# Mode Row
mode_row = ctk.CTkFrame(root, fg_color="lightgrey")
mode_row.pack(pady=10)

mode_label = ctk.CTkLabel(mode_row,
                          text="Mode:",
                          font=("Times New Roman", 30),
                          width=200,  # In pixels
                          anchor="w",
                          text_color="black")
mode_label.pack(side="left", padx=5)

mode_combo_box = ctk.CTkComboBox(mode_row,
                             width=300,
                             font=("Times New Roman", 22),
                             corner_radius=10,
                             values=["Stop-Loss Calculation", "Take Profit Calculation", 
                                     "Reward to Risk Calculation", "Deriv Accumulator Calculation"],
                             state='readonly')
mode_combo_box.set("Stop-Loss Calculation")
mode_combo_box.pack(side="left", padx=5)

# Entry Price Row
entry_row = ctk.CTkFrame(root, fg_color="lightgrey")
entry_row.pack(pady=10)

entry_label = ctk.CTkLabel(entry_row,
                           text="Entry Price:",
                           font=("Times New Roman", 30),
                           width=200,
                           anchor="w",
                           text_color="black")
entry_label.pack(side="left", padx=5)

entry_price = ctk.CTkEntry(entry_row,
                           font=("Times New Roman", 20),
                           width=300)
entry_price.pack(side="left", padx=5)

# Stop Loss (%) Row 
stop_loss_row = ctk.CTkFrame(root, fg_color= "lightgrey")
stop_loss_row.pack(pady = 10)

stop_loss_label = ctk.CTkLabel(stop_loss_row,
                               text="Stop-Loss (%):",
                               font=("Times New Roman", 30),
                               width=200,
                               anchor="w",
                               text_color="black")
stop_loss_label.pack(side="left", padx=5)

stop_loss_entry = ctk.CTkEntry(stop_loss_row,
                               font=("Times New Roman", 20),
                               width=300)
stop_loss_entry.pack(side="left",padx= 5)

# Position Size Row
position_size_row = ctk.CTkFrame(root, fg_color= "lightgrey")
position_size_row.pack(pady = 10)

position_size_label = ctk.CTkLabel(position_size_row,
                               text="Position Size:",
                               font=("Times New Roman", 30),
                               width=200,
                               anchor="w",
                               text_color="black")
position_size_label.pack(side="left", padx=5)

position_size_entry = ctk.CTkEntry(position_size_row,
                               font=("Times New Roman", 20),
                               width=300)
position_size_entry.pack(side="left",padx= 5)

# Trade Direction Row
trade_direction_row = ctk.CTkFrame(root, fg_color="lightgrey")
trade_direction_row.pack(pady=10)

trade_direction_label = ctk.CTkLabel(trade_direction_row,
                          text="Trade Direction:",
                          font=("Times New Roman", 30),
                          width=200,  # In pixels
                          anchor="w",
                          text_color="black")
trade_direction_label.pack(side="left", padx=5)

trade_direction_combo_box = ctk.CTkComboBox(trade_direction_row,
                             width=300,
                             font=("Times New Roman", 20),
                             values=["Long", "Short",],
                             state='readonly')
trade_direction_combo_box.set("Long")
trade_direction_combo_box.pack(side="left", padx=5)

# Calculate Row
calculate_row = ctk.CTkFrame(root, fg_color="lightgrey")
calculate_row.pack(pady=10)

calculate_button = ctk.CTkButton(calculate_row,
                                 width=120,
                                 height=40,
                                 text="Calculate",
                                 fg_color=("lightgrey", "lightgrey"),
                                 hover_color="grey",
                                 text_color="Black",
                                 font=("Arial", 22),
                                 border_width=2,
                                 border_color="black")
calculate_button.pack()

output_frame = ctk.CTkFrame(root, width=700, height=300, fg_color="lightgrey", bg_color="lightgrey", border_color="black", border_width=3)
output_frame.pack(pady=10)
output_frame.pack_propagate(False)



root.mainloop()
