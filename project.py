from functions import get_entry_price, get_position_size, get_stop_loss_percentage, get_trade_direction, get_take_profit

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
            choice = input("").strip().lower()
            if choice not in ("s", "t", "r", "d"):
                raise ValueError("Enter a valid input 's', 't', 'r' or 'd'")
            if choice == "s":
                entry_price = get_entry_price()
                stop_loss_percentage= get_stop_loss_percentage()
                position_size = get_position_size()
                trade_direction = get_trade_direction()
                stop_loss_price, risk_per_unit, potential_loss = stop_loss(entry_price, stop_loss_percentage, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"Stop loss price: {stop_loss_price:,.2f}")
                print(f"Risk per unit: {risk_per_unit:,.2f}")
                print(f"Potential loss: ${potential_loss:,.2f}")

            elif choice == "t":
                entry_price = get_entry_price()
                take_profit_pct = get_take_profit()
                position_size = get_position_size()
                trade_direction = get_trade_direction()
                take_profit_price, reward_per_unit, units, total_reward= take_profit(entry_price, take_profit_pct, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"Take Profit price: {take_profit_price:,.2f}")
                print(f"Reward per unit: {reward_per_unit:,.2f}")
                print(f"Units: {units:,.2f}")
                print(f"Total reward: {total_reward:,.2f}")

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
        
def stop_loss(entry_price, stop_loss_percentage, position_size, trade_direction):
    risk_per_unit = (entry_price * stop_loss_percentage)/ 100
    if trade_direction == "long":
        stop_loss_price = entry_price - risk_per_unit
    elif trade_direction == "short":
        stop_loss_price = entry_price + risk_per_unit
    else:
        raise ValueError("Trade direction must be 'long' or 'short'")

    units = position_size / entry_price
    potential_loss = risk_per_unit * units

    return stop_loss_price, risk_per_unit, potential_loss


def take_profit(entry_price, take_profit_pct, position_size, trade_direction):
    if trade_direction == "long":
        take_profit_price = entry_price * (1 + take_profit_pct / 100)
    elif trade_direction == "short":
        take_profit_price = entry_price * (1 - take_profit_pct / 100)
    else:
        raise ValueError("Trade direction must be 'long' or 'short'")
    
    reward_per_unit = abs(take_profit_price - entry_price)
    units = position_size / entry_price
    total_reward = reward_per_unit * units

    return take_profit_price, reward_per_unit, units, total_reward

def reward_risk():
    ...

def deriv_accumulator():
    ...

if __name__ == "__main__":
    main()