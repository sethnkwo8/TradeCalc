def get_entry_price():
    while True:
        try:
            entry_price = float(input("Enter Entry price (in dollars): "))
            return entry_price
        except ValueError:
            print("Invalid entry price. Please enter a number.")

def get_stop_loss_percentage():
    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss percent (%): "))
            return stop_loss_percentage
        except ValueError:
            print("Invalid stop-loss percent. Please enter a number.")

def get_position_size():
    while True:
        try:
            position_size = float(input("Enter Position Size (in dollars): "))
            return position_size
        except ValueError:
            print("Invalid position size. Please enter a number.")

def get_trade_direction():
    while True:
        trade_direction = input("Are you going long or short? ").lower()
        if trade_direction in ("long", "short"):
            return trade_direction
        else:
            print("Enter a valid input 'long' or 'short'")