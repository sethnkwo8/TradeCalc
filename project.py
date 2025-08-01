class Account():
    def __init__(self, name):
        if not name.isalpha():
            raise ValueError("Please enter a Valid Name")
        self.name = name
    
    def __str__(self):
        return f"\nOk {self.name} this is TradeCalc where we make trading easier by giving you ideal calculations to guide your trade. What would you like to do?\nStop-Loss Calculation   -s\nTake Profit Calculation   -t\nReward:Risk Ratio Calculation   -r\nDeriv Accumulator Calculation   -d"
    

def main():
    while True:
        try:
            name = input("Welcome, what's your name? ")
            account = Account(name)
            break
        except ValueError:
            print("Please enter a Valid Name")
    print(account)

    while True:
        try: 
            choice = input("").strip()
            if choice not in ("s", "t", "r", "d"):
                raise ValueError("Enter a valid input 's', 't', 'r' or 'd'")
            if choice == "s":
                stop_loss_price, risk_per_unit, potential_loss = stop_loss()
                print("\n--- CALCULATION RESULTS ---")
                print(f"Stop loss price: {stop_loss_price:.2f}")
                print(f"Risk per unit: {risk_per_unit:.2f}")
                print(f"Potential loss: ${potential_loss:.2f}")
            elif choice == "t":
                results = take_profit()
                print(results)
            elif choice == "r":
                results = reward_risk()
                print(results)
            elif choice == "d":
                results = deriv_accumulator()
                print(results)
            break  # Exit loop after successful function call
        except ValueError:
            print("Enter a valid input 's', 't', 'r' or 'd'")
        except TypeError:
            print("Invalid input")
    

def stop_loss():
    while True:
        try:
            entry_price = float(input("Enter Entry price (in dollars): "))
            break
        except ValueError:
            print("Invalid entry price. Please enter a number.")

    while True:
        try:
            stop_loss_percentage = float(input("Enter Stop-Loss percent (%): "))
            break
        except ValueError:
            print("Invalid stop-loss percent. Please enter a number.")

    while True:
        try:
            position_size = float(input("Enter Position Size (in dollars): "))
            break
        except ValueError:
            print("Invalid position size. Please enter a number.")

    while True:
        trade_direction = input("Are you going long or short? ").lower()
        if trade_direction in ("long", "short"):
            break
        else:
            print("Enter a valid input 'long' or 'short'")

    risk_per_unit = (entry_price * stop_loss_percentage) * 100
    if trade_direction == "long":
        stop_loss_price = entry_price - risk_per_unit
    elif trade_direction == "short":
        stop_loss_price = entry_price + risk_per_unit

    units = position_size / entry_price
    potential_loss = risk_per_unit * units

    return stop_loss_price, risk_per_unit, potential_loss



def take_profit():
    ...

def reward_risk():
    ...

def deriv_accumulator():
    ...

if __name__ == "__main__":
    main()