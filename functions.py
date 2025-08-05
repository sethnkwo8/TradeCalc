import math
import matplotlib.pyplot as plt

def get_entry_price():
    while True:
        try:
            entry_price = float(input("Enter Entry price (in dollars): ").strip())
            if entry_price <= 0:
                print("Entry price must be a positive integer")
                continue
            return entry_price
        except ValueError:
            print("Invalid entry price. Please enter a number.")

def get_stop_loss_percentage():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss percent (%): ").strip())
            if stop_loss_percentage <= 0:
                print("Stop loss percent must be a positive integer")
                continue
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss percent. Please enter a number.")

def get_stop_loss_price():
    while True:
        try:
            stop_loss_price = float(input("Enter Stop-Loss price (in dollars): ").strip())
            if stop_loss_price <= 0:
                print("Stop loss price must be a positive integer")
                continue
            return stop_loss_price
        except ValueError:
            print("Invalid stop-loss price. Please enter a number.")

def get_position_size():
    while True:
        try:
            position_size = float(input("Enter Position Size (units): ").strip())
            if position_size <= 0:
                print("Position size must be a positive integer")
                continue
            return position_size
        except ValueError:
            print("Invalid position size. Please enter a number.")

def get_valid_trade_direction():
    while True:
        direction = input("Enter trade direction (long or short): ").strip().lower()
        if direction in ("long", "short"):
            return direction
        else:
            print("⚠️ Trade direction must be 'long' or 'short'. Please try again.")

def get_take_profit_pct():
    while True:
        try:
            take_profit = float(input("Enter your take profit percent (%): ").strip())
            if take_profit <= 0:
                print("Take profit percent must be a positive integer")
                continue
            return take_profit
        except ValueError:
            print("Invalid take profit percent. Please enter a number")

def get_take_profit_pce():
    while True:
        try:
            take_profit = float(input("Enter your take profit price (in dollars): ").strip())
            if take_profit <= 0:
                print("Take profit price must be a positive integer")
                continue
            return take_profit
        except ValueError:
            print("Invalid take profit percent. Please enter a number")

def get_stake():
    while True:
        try:
            stake = float(input("Enter your stake (in dollars): ").strip())
            if stake <= 0:
                print("Stake must be a positive integer")
                continue
            return stake
        except ValueError:
            print("Invalid stake. Please enter a number")

def get_take_profit_tick():
    while True:
        try:
            take_profit = float(input("Enter your take profit (profit per tick): ").strip())
            if take_profit <= 0:
                print("Take profit must be a positive integer")
                continue
            return take_profit
        except ValueError:
            print("Invalid take profit. Enter an integer ")

def get_growth_rate():
    while True:
        growth_input = input("Enter growth rate (% profit goal), or press Enter to skip: ").strip()
        if growth_input == "":
            return None
        try:
            growth_rate = float(growth_input)
            if float(growth_input) <= 0:
                print("Growth rate must be a positive integer")
                continue
            if float(growth_input) > 5:
                print("Deriv Accumulator growth rate cannot exceed 5%")
                continue
            return growth_rate
        except ValueError:
            print("Invalid growth rate. Please enter a valid growth rate")

def get_target_profit():
    while True:
        target_input = input("Enter target profit (desired $ profit), or press Enter to skip: ").strip()
        if target_input == "":
            return None
        else:
            try:
                target_profit = float(target_input)
                if float(target_input) <= 0:
                    print("Target profit must be a positive integer")
                    continue
                return target_profit
            except ValueError:
                print("Invalid target profit. Please enter a number")

def get_trades_per_day():
    while True:
        tpd_input = input("Enter trades per day (trades planned per day/session), or press Enter to skip: ").strip()
        if tpd_input == "":
            return None
        else:
            try:
                tpd = float(tpd_input)
                if float(tpd_input) <= 0:
                    print("Trades per day must be a positive integer")
                    continue
                return tpd
            except ValueError:
                print("Invalid input. Please enter an integer.")

def get_tick_duration():
    while True:
        tick_duration_input = input("Enter tick duration (in minutes per tick/contract), or press Enter to skip: ").strip()
        
        if tick_duration_input == "":
            return None
        else:
            try:
                tick_duration = float(tick_duration_input)
                if float(tick_duration_input) <= 0:
                    print("Tick duration must be a positive integer")
                    continue
                return tick_duration
            except ValueError:
                print("Invalid input. Please enter an integer")

def growth_rate_exceeds(stake, target_profit):
        total_target = stake + target_profit
        compound_trades_no = round((math.log(total_target / stake) / math.log(1.05)))
        targets = [round(stake * ((1.05) ** i), 2) for i in range(1, compound_trades_no + 1) ]
        implied_growth_rate = (target_profit / stake) * 100
        final_account = round(stake * (1.05) ** compound_trades_no, 2)
        actual_profit = final_account - stake
        return targets, total_target, compound_trades_no, actual_profit

def get_ticks_per_trade():
    while True:
        ticks_input = input("Enter number of ticks per trade (press Enter for default 10): ").strip()

        if ticks_input == "":
            return 10
        else:
            try:
                ticks_per_trade = int(ticks_input)
                if ticks_per_trade <= 0:
                    print("Ticks per trade must be a positive integer.")
                    continue
                return ticks_per_trade
            except ValueError:
                print("Please enter a valid number of ticks (e.g., 10, 20).")

def deriv_output_format(
    stake, growth_rate, target_profit, take_profit_tick,
    trades_per_day, tick_duration, compound_mode=False,
    no_trades=None, targets=None, actual_profit=None
):
    output = []

    output.append("📊 Deriv Accumulator Summary")
    output.append("-" * 40)
    output.append(f"Initial Stake: ${stake:.2f}")
    output.append(f"Target Growth Rate: {growth_rate:.2f}%")
    output.append(f"Target Profit: ${target_profit:.2f}")
    output.append(f"Take Profit per Tick: ${take_profit_tick:.2f}")
    output.append(f"Trades per Day: {trades_per_day}")
    output.append(f"Tick Duration: {tick_duration} minutes")

    if compound_mode:
        output.append("\n🔁 Since the growth rate exceeds 5%, compounding is applied.")
        output.append(f"Total Compound Trades Needed: {no_trades}")
        output.append(f"Profit After Compounding: ${actual_profit:.2f}")
        output.append("\nCompound Trade Targets:")
        for i, target in enumerate(targets[1:], 1):  # skip initial stake
            output.append(f"  Trade {i}: ${target:.2f}\n")
    else:
        ticks_needed = target_profit / take_profit_tick
        estimated_time = ticks_needed * tick_duration
        daily_sessions_target = take_profit_tick * trades_per_day

        output.append(f"Ticks Needed to Hit Profit: {int(ticks_needed)}")
        output.append(f"Estimated Time to Target: {estimated_time:.1f} minutes")
        output.append(f"Daily Profit at Current Settings: ${daily_sessions_target:.2f}/day\n")

    return "\n".join(output)

def bar_chart(stake, profit_per_tick, trades_per_day, compound_mode, targets, days=7 ):
    if compound_mode and targets:
        x_axis = [f"Day {i+1}" for i in range(len(targets))]
        y_axis = [f"${(target * profit_per_tick * trades_per_day):.2f}" for target in targets]
    else:
        daily_profit = stake * profit_per_tick * trades_per_day
        x_axis = [f"Day {i+1}" for i in range(days)]
        y_axis = [f"${daily_profit * (i+1):.2f}" for i in range(days) ]
    
    plt.bar(x_axis,y_axis)
    plt.title("Profit per day")
    plt.xlabel("Days")
    plt.ylabel("Profit")
    plt.show()

def get_chart():
    while True:
            outcome = input("Will you like to see a diagram representation of your profit per day (yes or no)? ").lower().strip()
            if outcome in ["yes", "no"]:
                return outcome
            else:
                print("Enter 'yes' or 'no'")
