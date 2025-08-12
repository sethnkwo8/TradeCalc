import customtkinter as ctk
from project import stop_loss, take_profit, reward_risk, accumulator_core, deriv_accumulator, deriv_output_format
from project import growth_rate_exceeds, bar_chart
from tkinter import messagebox
import csv
import os
import sys

ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")

def get_float(entry, field_name, required=True):
    """Validate and return float from entry, show error if invalid."""
    value = entry.get().strip()

    if not value:
        if required:
            messagebox.showerror("Invalid Input", f"{field_name} is required.")
            raise ValueError("Missing required field")
        else:
            return None  # Optional field left blank

    try:
        return float(value)
    except ValueError:
        messagebox.showerror("Invalid Input", f"{field_name} must be a number.")
        raise

def calculate(entry1,entry2,entry3,entry4,entry5,entry6, entry7):
    try:
        stake = get_float(entry1, "Stake ($)")
        profit_per_tick = get_float(entry2, "Take Profit Per Tick ($)")
        tick_duration = get_float(entry3, "Tick Duration (minutes)")
        trades_per_day = get_float(entry4, "No Of Trades (per day)")
        no_of_ticks = get_float(entry5, "No Of Ticks (per trade)", required=False) or 10
        growth_rate = get_float(entry6, "Growth Rate (%)", required=False)
        target_profit = get_float(entry7, "Target Profit ($)", required=False)

        return stake, profit_per_tick, tick_duration, trades_per_day, no_of_ticks, growth_rate, target_profit

    except ValueError:
        # Already handled in get_float(), so just stop execution
        return

# Root window
root = ctk.CTk()
root.title("TradeCalc")
root.geometry("800x900")

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

# ===== Top Frame (Fixed Mode Row) =====
top_frame = ctk.CTkFrame(root, fg_color="#ebebeb")
top_frame.pack(fill="both", pady=5)

mode_label = ctk.CTkLabel(top_frame, text="Select Mode:", font=("Calibri", 20))
mode_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

# Content frame (dynamic area)
content_frame = ctk.CTkFrame(root, fg_color="#ebebeb")
content_frame.pack(fill="both", expand=True, pady=0)

# ===== Layout Functions =====
def stop_loss_layout(frame):
    label1 = ctk.CTkLabel(frame, text="Entry Price ($):", font=("Calibri", 20))
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry1 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    label2 = ctk.CTkLabel(frame, text="Stop Loss (%):", font=("Calibri", 20))
    label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry2 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    label3 = ctk.CTkLabel(frame, text="Position Size ($):", font=("Calibri", 20))
    label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry3 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    label4 = ctk.CTkLabel(frame, text="Trade Direction:", font=("Calibri", 20))
    label4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry4 = ctk.CTkComboBox(frame, values=["Long", "Short"], font=("Calibri", 20))
    entry4.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    # ===== Helper Functions =====
    def lower_trade():
        direction = entry4.get().lower()
        return direction

    def results():
        try:
            val1 = float(entry1.get())
            val2 = float(entry2.get())
            val3 = float(entry3.get())
            val4 = lower_trade()

            stop_loss_price, risk_per_unit, potential_loss = stop_loss(val1, val2, val3, val4)
            
            output1_value.configure(text=f"${stop_loss_price}")
            output2_value.configure(text=f"${risk_per_unit}")
            output3_value.configure(text=f"${potential_loss}")
        except ValueError:
            output1_value.configure(text="Invalid")
            output2_value.configure(text="Invalid")
            output3_value.configure(text="Invalid")

    calc_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    calc_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=15)

    calc_button = ctk.CTkButton(calc_frame, 
                                text="Calculate",
                                font=("Calibri", 20),
                                fg_color="#ebebeb",
                                text_color="black",
                                border_color="black",
                                border_width=2,
                                hover_color="grey",
                                command=results)
    calc_button.grid(row=0, column=0, padx=10, pady=5)

    output = ctk.CTkFrame(frame,
                        width=600,
                        height=150,
                        fg_color="lightgrey",
                        border_color="black",
                        border_width=3
                        )
    output.grid(row=5, column=0, columnspan=2, padx=10, pady=15)
    output.grid_propagate(False)

    output1 = ctk.CTkLabel(output, text="Stop Loss Price:", font=("Calibri", 18))
    output1.grid(row=0, column=0, padx=30, pady=10, sticky="w")
    output1_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output1_value.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    output2 = ctk.CTkLabel(output, text="Risk Per Unit:", font=("Calibri", 18))
    output2.grid(row=1, column=0, padx=30, pady=10, sticky="w")
    output2_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output2_value.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    output3 = ctk.CTkLabel(output, text="Potential Loss:", font=("Calibri", 18))
    output3.grid(row=2, column=0, padx=30, pady=10, sticky="w")
    output3_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output3_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    frame.grid_columnconfigure(1, weight=1)  

def take_profit_layout(frame):
    label1 = ctk.CTkLabel(frame, text="Entry Price ($):", font=("Calibri", 20))
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry1 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    label2 = ctk.CTkLabel(frame, text="Take Profit (%):", font=("Calibri", 20))
    label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry2 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    label3 = ctk.CTkLabel(frame, text="Position Size ($):", font=("Calibri", 20))
    label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry3 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    label4 = ctk.CTkLabel(frame, text="Trade Direction:", font=("Calibri", 20))
    label4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry4 = ctk.CTkComboBox(frame, values=["Long", "Short"], font=("Calibri", 20))
    entry4.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    # ===== Helper Functions =====
    def lower_trade():
        direction = entry4.get().lower()
        return direction

    def results():
        try:
            val1 = float(entry1.get())
            val2 = float(entry2.get())
            val3 = float(entry3.get())
            val4 = lower_trade()

            take_profit_price, reward_per_unit, total_reward = take_profit(val1, val2, val3, val4)
            
            output1_value.configure(text=f"${take_profit_price}")
            output2_value.configure(text=f"${reward_per_unit}")
            output3_value.configure(text=f"${total_reward}")
        except ValueError:
            output1_value.configure(text="Invalid")
            output2_value.configure(text="Invalid")
            output3_value.configure(text="Invalid")

    calc_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    calc_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=15)

    calc_button = ctk.CTkButton(calc_frame, 
                                text="Calculate",
                                font=("Calibri", 20),
                                fg_color="#ebebeb",
                                text_color="black",
                                border_color="black",
                                border_width=2,
                                hover_color="grey",
                                command=results)
    calc_button.grid(row=0, column=0, padx=10, pady=15)

    output = ctk.CTkFrame(frame,
                        width=600,
                        height=150,
                        fg_color="lightgrey",
                        border_color="black",
                        border_width=3
                        )
    output.grid(row=5, column=0, columnspan=2, padx=10, pady=15)
    output.grid_propagate(False)

    output1 = ctk.CTkLabel(output, text="Take Profit Price:", font=("Calibri", 18))
    output1.grid(row=0, column=0, padx=30, pady=10, sticky="w")
    output1_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output1_value.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    output2 = ctk.CTkLabel(output, text="Reward Per Unit:", font=("Calibri", 18))
    output2.grid(row=1, column=0, padx=30, pady=10, sticky="w")
    output2_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output2_value.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    output3 = ctk.CTkLabel(output, text="Total Reward:", font=("Calibri", 18))
    output3.grid(row=2, column=0, padx=30, pady=10, sticky="w")
    output3_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output3_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    frame.grid_columnconfigure(1, weight=1)

def reward_risk_layout(frame):
    label1 = ctk.CTkLabel(frame, text="Entry Price ($):", font=("Calibri", 20))
    label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entry1 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    label2 = ctk.CTkLabel(frame, text="Take Profit Price ($):", font=("Calibri", 20))
    label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entry2 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    label3= ctk.CTkLabel(frame, text="Stop Loss Price ($):", font=("Calibri", 20))
    label3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entry3 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    label4= ctk.CTkLabel(frame, text="Position Size ($):", font=("Calibri", 20))
    label4.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    entry4 = ctk.CTkEntry(frame, font=("Calibri", 20))
    entry4.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    label5 = ctk.CTkLabel(frame, text="Trade Direction:", font=("Calibri", 20))
    label5.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entry5 = ctk.CTkComboBox(frame, values=["Long", "Short"], font=("Calibri", 20))
    entry5.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    # ===== Helper Functions =====
    def lower_trade():
        direction = entry5.get().lower()
        return direction

    def results():
        try:
            val1 = float(entry1.get())
            val2 = float(entry2.get())
            val3 = float(entry3.get())
            val4 = float(entry4.get())
            val5 = lower_trade()

            reward_per_unit, risk_per_unit, total_reward, total_risk, reward_risk_ratio = reward_risk(val1, val2, val3, val4, val5)
            
            output1_value.configure(text=f"${reward_per_unit}")
            output2_value.configure(text=f"${risk_per_unit}")
            output3_value.configure(text=f"${total_reward}")
            output4_value.configure(text=f"${total_risk}")
            output5_value.configure(text=f" You gain ${reward_risk_ratio} per $1")
        except ValueError:
            output1_value.configure(text="Invalid")
            output2_value.configure(text="Invalid")
            output3_value.configure(text="Invalid")
            output4_value.configure(text="Invalid")
            output5_value.configure(text="Invalid")

    calc_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    calc_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=15)

    calc_button = ctk.CTkButton(calc_frame, 
                                text="Calculate",
                                font=("Calibri", 20),
                                fg_color="#ebebeb",
                                text_color="black",
                                border_color="black",
                                border_width=2,
                                hover_color="grey",
                                command=results)
    calc_button.grid(row=0, column=0, padx=10, pady=15)

    output = ctk.CTkFrame(frame,
                        width=600,
                        height=250,
                        fg_color="lightgrey",
                        border_color="black",
                        border_width=3
                        )
    output.grid(row=6, column=0, columnspan=2, padx=10, pady=15)
    output.grid_propagate(False)

    output1 = ctk.CTkLabel(output, text="Reward Per Unit:", font=("Calibri", 18))
    output1.grid(row=0, column=0, padx=30, pady=10, sticky="w")
    output1_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output1_value.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    output2 = ctk.CTkLabel(output, text="Risk Per Unit:", font=("Calibri", 18))
    output2.grid(row=1, column=0, padx=30, pady=10, sticky="w")
    output2_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output2_value.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    output3 = ctk.CTkLabel(output, text="Total Reward:", font=("Calibri", 18))
    output3.grid(row=2, column=0, padx=30, pady=10, sticky="w")
    output3_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output3_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    output4 = ctk.CTkLabel(output, text="Total Risk:", font=("Calibri", 18))
    output4.grid(row=3, column=0, padx=30, pady=10, sticky="w")
    output4_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output4_value.grid(row=3, column=1, padx=10, pady=10, sticky="w")

    output5 = ctk.CTkLabel(output, text="Reward-to-Risk Ratio:", font=("Calibri", 18))
    output5.grid(row=4, column=0, padx=30, pady=10, sticky="w")
    output5_value = ctk.CTkLabel(output, text="", font=("Calibri", 18))
    output5_value.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    frame.grid_columnconfigure(1, weight=1)

def deriv_accum_layout(frame):
    last_results = {}

    def get_float(entry, field_name):
        val = entry.get().strip()
        if not val:
            raise ValueError(f"{field_name} cannot be empty")
        try:
            return float(val)
        except ValueError:
            raise ValueError(f"{field_name} must be a number")

    # Calculate button action
    def calculate():
        nonlocal last_results
        try:
            stake = get_float(stake_entry, "Stake")
            take_profit_tick = get_float(take_profit_entry, "Take Profit/Tick")
            tick_duration = get_float(tick_duration_entry, "Tick Duration (min)")
            trades_per_day = get_float(trades_per_day_entry, "Trades per Day")
            ticks_per_trade = get_float(ticks_per_trade_entry, "Ticks per Trade")

            growth_rate_val = growth_rate_entry.get().strip()
            target_profit_val = target_profit_entry.get().strip()

            growth_rate = float(growth_rate_val) if growth_rate_val else None
            target_profit = float(target_profit_val) if target_profit_val else None

            results = accumulator_core(
                stake, take_profit_tick, tick_duration, trades_per_day, ticks_per_trade,
                growth_rate=growth_rate, target_profit=target_profit
            )

            last_results = results

            formatted_output = deriv_output_format(**results)
            output_text.configure(text="")
            output_text.configure(text=formatted_output)

            save_to_csv(results)

        except Exception as e:
            messagebox.showerror("Invalid Input", str(e))

    # Save results to CSV
    def save_to_csv(results):
        fields = ["Stake","Growth Rate","Target Profit","Profit per Tick","Tick Duration",
                "Trades per Day","Ticks Needed","Daily Session Targets","Estimated Time Needed",
                "Compound Mode","No of Trades","Actual Profit","Targets"]

        csv_results = {
            "Stake": f' ${results["stake"]} ',
            "Growth Rate": f' {results["growth_rate"]}% ',
            "Target Profit": f' ${results["target_profit"]} ',
            "Profit per Tick": f' ${results["profit_per_tick"]} ',
            "Tick Duration": f' {results["tick_duration"]} mins ',
            "Trades per Day": f' {results["trades_per_day"]} trades per day ',
            "Ticks Needed": f' {results["ticks_needed"]:.0f} ticks needed ' if results["ticks_needed"] else " N/A ",
            "Daily Session Targets": f' ${results["daily_sessions_target"]:.2f}/day ' if results["daily_sessions_target"] else " N/A ",
            "Estimated Time Needed": f' {results["estimated_time"]:.0f} minutes ' if results["estimated_time"] else " N/A ",
            "Compound Mode": f' {results["compound_mode"]} ',
            "No of Trades": f' {results["no_trades"]} ' if results["no_trades"] else " N/A ",
            "Actual Profit": f' ${results["actual_profit"]} ' if results["actual_profit"] else " N/A ",
            "Targets": " , ".join([f"{t:.2f}" for t in results["targets"]]) if results["targets"] else " N/A "
        }

        file_exists = os.path.exists("Trades History.csv")
        with open("Trades History.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            if not file_exists:
                writer.writeheader()
            writer.writerow(csv_results)

    def add_entry(frame, label_text, row):
        lbl = ctk.CTkLabel(frame, text=label_text, font=("Calibri", 18))
        lbl.grid(row=row, column=0, padx=10, pady=5, sticky="w")
        
        entry = ctk.CTkEntry(frame, width=1800, font=("Calibri", 18))
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="w")
    
        return entry

    stake_entry = add_entry(frame, "Stake ($):", 0)
    take_profit_entry = add_entry(frame, "Take Profit per Tick ($):", 1)
    tick_duration_entry = add_entry(frame, "Tick Duration (minutes):", 2)
    trades_per_day_entry = add_entry(frame, "Trades per Day:", 3)
    ticks_per_trade_entry = add_entry(frame, "Ticks per Trade:", 4)
    growth_rate_entry = add_entry(frame, "Growth Rate (%) [optional]:", 5)
    target_profit_entry = add_entry(frame, "Target Profit ($) [optional]:", 6)

    calc_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    calc_frame.grid(row=7, column=0, columnspan=2, padx=10, pady=2)

    calc_btn = ctk.CTkButton(calc_frame,
                             text="Calculate",
                             font=("Calibri", 20),
                             fg_color="#ebebeb",
                             text_color="black",
                             border_color="black",
                             border_width=2,
                             hover_color="grey",
                             command=calculate)
    calc_btn.grid(row=0, column=0, padx=10, pady=15)

    # Output frame
    output_frame = ctk.CTkFrame(
    frame,
    width=600,
    height=350,
    fg_color="#ebebeb", 
    border_color="black",
    border_width=3
    )
    output_frame.grid(row=8, column=0, columnspan=2, padx=10, pady=2)
    output_frame.grid_propagate(False)

    output_text = ctk.CTkLabel(
        output_frame,
        text="Results will appear here...",
        width=580,
        justify="left",
        anchor="w",
        font=("Calibri", 19)
    )
    output_text.pack(expand=True, fill="both", padx=3, pady=3)

    buttons_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    buttons_frame.grid(row=9, column=0, columnspan=2, padx=10, pady=1)

    def on_generate_chart():
        if not last_results:
            messagebox.showerror("Error", "Please run Calculate first.")
            return
        
        bar_chart(
            last_results["stake"],
            last_results["profit_per_tick"],
            last_results["trades_per_day"],
            last_results["compound_mode"],
            last_results["targets"],
            days=7
        )

    buttons_frame = ctk.CTkFrame(frame, fg_color="#ebebeb")
    buttons_frame.grid(row=9, column=0, columnspan=2, padx=10, pady=1)

    chart = ctk.CTkButton(
        buttons_frame,
        text="Generate Profit Chart",
        font=("Calibri", 20),
        fg_color="#ebebeb",
        text_color="black",
        border_color="black",
        border_width=2,
        corner_radius=8,
        hover_color="grey",
        command=on_generate_chart
    )
    chart.grid(row=0, column=0, padx=10, pady=15)
    frame.grid_columnconfigure(1, weight=1)

# ===== Mode Switch Logic =====
def switch_mode(choice):
    # Clear only content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Populate based on mode
    if choice == "Stop Loss Calculation":
        stop_loss_layout(content_frame)
    elif choice == "Take Profit Calculation":
        take_profit_layout(content_frame)
    elif choice == "Reward to Risk Calculation":
        reward_risk_layout(content_frame)
    else:
        deriv_accum_layout(content_frame)

# Mode dropdown
mode_dropdown = ctk.CTkComboBox(top_frame,
                                width=400,
                                values=["Stop Loss Calculation",
                                        "Take Profit Calculation",
                                        "Reward to Risk Calculation",
                                        "Deriv Accumulator Calculation"],
                                command=switch_mode,
                                font=("Calibri", 20))
mode_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Start with Basic mode
switch_mode("Stop Loss Calculation")

root.mainloop()
