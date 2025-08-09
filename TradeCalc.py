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

def switch_mode(*args):
    for widget in main_frame.winfo_children():
        widget.destroy()

    if mode_var.get() == "Stop Loss Calculation":
        layout_mode_stoploss()
    elif mode_var.get() == "Take Profit Calculation":
        layout_mode_takeprofit()
    elif mode_var.get() == "Reward to Risk Calculation":
        layout_mode_rewardrisk()
    elif mode_var.get() == "Deriv Accumulator Calculation":
        layout_mode_derivaccum()

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

# ================= MODE ROW ================= #
mode_frame = ctk.CTkFrame(root)
mode_frame.pack(fill="x", pady=10)

ctk.CTkLabel(mode_frame, font=("Times New Roman", 25),text="Select Mode:").pack(side="left", padx=5)

mode_var = ctk.StringVar(value="Stop Loss Calculation")

# Mode Selector
mode_menu = ctk.CTkComboBox(mode_frame,
                            width=400,
                            font=("Times New Roman", 22),
                            corner_radius=10,
                            variable=mode_var,
                            values=["Stop Loss Calculation",
                                    "Take Profit Calculation",
                                    "Reward to Risk Calculation",
                                    "Deriv Accumulator Calculation"],
                            command= lambda _: switch_mode())
mode_menu.pack(side="left", padx=5)

# Main Frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=True, fill="both", pady=0)

# Layouts
def layout_mode_stoploss():
    # Entry Price
    entry_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Entry Price ($):", entry_price, row=1)

    # Stop Loss %
    stop_loss_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Stop-Loss (%):", stop_loss_entry, row=2)

    # Position Size
    position_size_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Position Size ($):", position_size_entry, row=3)

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

layout_mode_stoploss()

def layout_mode_takeprofit():
    # Entry Price
    entry_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Entry Price ($):", entry_price, row=1)

    # Take Profit Percent
    take_profit_percent = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Take Profit (%):", take_profit_percent, row=2)

    # Position Size
    position_size_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Position Size ($):", position_size_entry, row=3)

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

    output1 = create_output(output, "Take Profit Price:", row=0)
    output2 = create_output(output, "Reward Per Unit:", row=1)
    output3 = create_output(output, "Total Reward:", row=2)

def layout_mode_rewardrisk():
    # Entry Price
    entry_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Entry Price ($):", entry_price, row=1)

    # Take Profit Price
    take_profit_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Take Profit Price ($):", take_profit_price, row=2)

    # Stop Loss Price
    stop_loss_price = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Stop Loss Price ($):", stop_loss_price, row=3)

    # Position Size
    position_size_entry = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Position Size ($):", position_size_entry, row=4)

    # Trade Direction ComboBox
    trade_dir_combo = ctk.CTkComboBox(
        main_frame,
        width=400,
        font=("Times New Roman", 22),
        values=["Long", "Short"],
        state='readonly'
    )
    trade_dir_combo.set("Long")
    create_row(main_frame, "Trade Direction:", trade_dir_combo, row=5)

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
    calc_button.grid(row=6, column=1, columnspan=2, pady=30, padx=100)

    # ---------- Output ----------
    output = ctk.CTkFrame(main_frame,
                        width=600,
                        height=250,
                        fg_color="lightgrey",
                        border_color="black",
                        border_width=3
                        )
    output.grid(row=7, column=1, columnspan=2, pady=10)
    output.grid_propagate(False)

    output1 = create_output(output, "Reward Per Unit:", row=0)
    output2 = create_output(output, "Risk Per Unit:", row=1)
    output3 = create_output(output, "Total Reward:", row=2)
    output4 = create_output(output, "Total Risk:", row=3)
    output5 = create_output(output, "Reward-to-Risk Ratio:", row=4)

def layout_mode_derivaccum():
    # Stake
    stake = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Stake ($):", stake, row=1)

    # Take Profit per tick
    profit_per_tick = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Take Profit per tick ($):", profit_per_tick, row=2)

    # Tick Duration
    tick_duration = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Tick duration (minutes):", tick_duration, row=3)

    # Trades Per Day
    trades_per_day = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "No of trades (per day):", trades_per_day, row=4)

    # Ticks Per trade
    ticks_per_trade = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "No of ticks (per trade):", ticks_per_trade, row=5)

    # Growth Rate
    growth_rate = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Growth Rate (%):", growth_rate, row=6)

    # Target Profit
    target_profit = ctk.CTkEntry(main_frame, font=("Times New Roman", 22), width=400)
    create_row(main_frame, "Target Profit ($):", target_profit, row=7)

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
    calc_button.grid(row=8, column=1, columnspan=2, pady=20, padx=100)

    # ---------- Output ----------
    output = ctk.CTkFrame(main_frame,
                        width=600,
                        height=250,
                        fg_color="lightgrey",
                        border_color="black",
                        border_width=3
                        )
    output.grid(row=9, column=1, columnspan=2, pady=5)
    output.grid_propagate(False)

    output1 = create_output(output, "Reward Per Unit:", row=0)
    output2 = create_output(output, "Risk Per Unit:", row=1)
    output3 = create_output(output, "Total Reward:", row=2)
    output4 = create_output(output, "Total Risk:", row=3)
    output5 = create_output(output, "Reward-to-Risk Ratio:", row=4)

switch_mode()

# ---------- Run ----------
root.mainloop()
