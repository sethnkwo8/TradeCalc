def get_entry_price():
    while True:
        try:
            entry_price = float(input("Enter Entry price (in dollars): ").strip())
            if entry_price <= 0:
                raise ValueError("Enter input above 0")
            return entry_price
        except ValueError:
            print("Invalid entry price. Please enter a number.")

def get_stop_loss_percentage():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss percent (%): ").strip())
            if stop_loss_percentage <= 0:
                raise ValueError("Enter input above 0")
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss percent. Please enter a number.")

def get_stop_loss_pce():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss price (in dollars): ").strip())
            if stop_loss_percentage <= 0:
                raise ValueError("Enter input above 0")
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss price. Please enter a number.")

def get_position_size():
    while True:
        try:
            position_size = float(input("Enter Position Size (units): ").strip())
            if position_size <= 0:
                raise ValueError("Enter input above 0")
            return position_size
        except ValueError:
            print("Invalid position size. Please enter a number.")

def get_trade_direction():
    while True:
        trade_direction = input("Are you going long or short? ").strip().lower()
        if trade_direction in ("long", "short"):
            return trade_direction
        else:
            print("Enter a valid input 'long' or 'short'")

def get_take_profit_pct():
    while True:
        try:
            take_profit = float(input("Enter your take profit percent (%): ").strip())
            if take_profit <= 0:
                raise ValueError("Enter input above 0")
            return take_profit
        except ValueError:
            print("Enter valid input")

def get_take_profit_pce():
    while True:
        try:
            take_profit = float(input("Enter your take profit price (in dollars): ").strip())
            if take_profit <= 0:
                raise ValueError("Enter input above 0")
            return take_profit
        except ValueError:
            print("Enter valid input")

def get_stake():
    while True:
        try:
            stake = float(input("Enter your stake (in dollars): ").strip())
            if stake <= 0:
                raise ValueError("Enter input above 0")
            return stake
        except ValueError:
            print("Enter valid input")

def get_take_profit_tick():
    while True:
        try:
            take_profit = float(input("Enter your take profit (profit per tick): ").strip())
            if take_profit <= 0:
                raise ValueError("Enter input above 0")
            return take_profit
        except ValueError:
            print("Enter valid input")

def get_growth_rate():
    while True:
        try:
            growth_input = input("Enter growth rate (% profit goal), or press Enter to skip: ").strip()
            if growth_input == "":
                growth_rate = None
            elif float(growth_input) <= 0:
                raise ValueError("Enter input above 0")
            else:
                growth_rate = float(growth_input)
            return growth_rate
        except ValueError:
            print("Enter valid input")

def get_target_profit():
    while True:
        try:
            target_input = input("Enter target profit (desired $ profit), or press Enter to skip: ").strip()
            if target_input == "":
                target_profit = None
            elif float(target_input) <= 0:
                raise ValueError("Enter input above 0")
            else:
                target_profit = float(target_input)
            return target_profit
        except ValueError:
            print("Enter valid input")

def get_trades_per_day():
    while True:
        try:
            tpd_input = input("Enter trades per day (number of trades planned for day/session), or press Enter to skip: ").strip()
            if tpd_input == "":
                tpd = None
            elif float(tpd_input) <= 0:
                raise ValueError("Enter input above 0")
            else:
                tpd = float(tpd_input)
            return tpd
        except ValueError:
            print("Enter valid input")

def get_tick_duration():
    while True:
        try:
            tick_duration_input = input("Enter tick duration (time in minutes each tick/contract takes), or press Enter to skip: ").strip()
            if tick_duration_input == "":
                tick_duration = None
            elif float(tick_duration_input) <= 0:
                raise ValueError("Enter input above 0")
            else:
                tick_duration = float(tick_duration_input)
            return tick_duration
        except ValueError:
            print("Enter valid input")
