def get_entry_price():
    while True:
        try:
            entry_price = float(input("Enter Entry price (in dollars): ").strip())
            if entry_price == 0:
                raise ValueError("Enter input above 0")
            return entry_price
        except ValueError:
            print("Invalid entry price. Please enter a number.")

def get_stop_loss_percentage():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss percent (%): ").strip())
            if stop_loss_percentage == 0:
                raise ValueError("Enter input above 0")
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss percent. Please enter a number.")

def get_stop_loss_pce():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss price (in dollars): ").strip())
            if stop_loss_percentage == 0:
                raise ValueError("Enter input above 0")
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss price. Please enter a number.")

def get_position_size():
    while True:
        try:
            position_size = float(input("Enter Position Size (units): ").strip())
            if position_size == 0:
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
            if take_profit == 0:
                raise ValueError("Enter input above 0")
            return take_profit
        except ValueError:
            print("Enter valid input")

def get_take_profit_pce():
    while True:
        try:
            take_profit = float(input("Enter your take profit price (in dollars): ").strip())
            if take_profit == 0:
                raise ValueError("Enter input above 0")
            return take_profit
        except ValueError:
            print("Enter valid input")