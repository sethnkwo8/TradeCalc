from functions import get_entry_price, get_position_size, get_stop_loss_percentage, get_trade_direction
from functions import get_take_profit_pct, get_take_profit_pce, get_stop_loss_pce, get_stake, get_take_profit_tick
from functions import get_growth_rate, get_target_profit, get_trades_per_day, get_tick_duration
import math

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
                print(f"""
🔻 Stop Loss Analysis

Trade Type      : {trade_direction.capitalize()}
Entry Price     : ${entry_price:.2f}
Stop Loss (%)   : ${stop_loss_price:.2f}
Position Size   : {position_size} units

-------------------------------

Stop Loss Price : ${stop_loss_price:.2f}
Risk per Unit   : ${risk_per_unit:.2f}
Total Risk      : ${potential_loss:.2f}
""")

            elif choice == "t":
                entry_price = get_entry_price()
                take_profit_pct = get_take_profit_pct()
                position_size = get_position_size()
                trade_direction = get_trade_direction()
                take_profit_price, reward_per_unit, total_reward = take_profit(entry_price, take_profit_pct, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"""
📈 Take Profit Analysis

Trade Type         : {trade_direction.capitalize()}
Entry Price        : ${entry_price:.2f}
Take Profit (%)    : ${take_profit_pct:.2f}
Position Size      : {position_size} units

-------------------------------
Take Profit price  : ${take_profit_price:,.2f}
Reward per Unit    : ${reward_per_unit:.2f}
Total Reward       : ${total_reward:.2f}
""")

            elif choice == "r":
                entry_price = get_entry_price()
                take_profit_pce = get_take_profit_pce()
                stop_loss_price = get_stop_loss_pce()
                position_size = get_position_size()
                trade_direction = get_trade_direction()
                ratio, reward_per_unit, risk_per_unit, total_reward, total_risk = reward_risk(entry_price, take_profit_pce, stop_loss_price, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"""
📊 Reward-to-Risk Analysis

Trade Type       : {trade_direction.capitalize()}
Entry Price      : ${entry_price:.2f}
Take-Profit Price: ${take_profit_pce:.2f}
Stop-Loss Price  : ${stop_loss_price:.2f}
Position Size    : {position_size} units

----------------------------------
Reward per Unit  : ${reward_per_unit:.2f}
Risk per Unit    : ${risk_per_unit:.2f}
Total Reward     : ${total_reward:.2f}
Total Risk       : ${total_risk:.2f}

✅ Reward-to-Risk Ratio: You gain ${ratio:.2f} per $1
"""
)
                
            elif choice == "d":
                stake = get_stake()
                growth_rate = get_growth_rate()
                target_profit = get_target_profit()
                take_profit_tick = get_take_profit_tick()
                tick_duration = get_tick_duration()
                trades_per_day = get_trades_per_day()
                results = deriv_accumulator(stake, take_profit_tick, tick_duration, trades_per_day, growth_rate, target_profit)
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

    return take_profit_price, reward_per_unit, total_reward

def reward_risk(entry_price, take_profit_pce, stop_loss_price, position_size, trade_direction):
    if trade_direction == "long":
        reward_per_unit = take_profit_pce - entry_price
    elif trade_direction == "short":
        reward_per_unit = entry_price - take_profit_pce
    else:
        raise ValueError("Trade direction must be 'long' or 'short'")
    
    if trade_direction == "long":
        risk_per_unit = entry_price - stop_loss_price
    elif trade_direction == "short":
        risk_per_unit = stop_loss_price - entry_price
    else:
        raise ValueError("Trade direction must be 'long' or 'short'")
    
    total_reward = reward_per_unit * position_size
    total_risk = risk_per_unit * position_size
    ratio =(abs(take_profit_pce - entry_price)) / (abs(entry_price - stop_loss_price))
    return ratio, reward_per_unit, risk_per_unit, total_reward, total_risk
    

def deriv_accumulator(stake, take_profit_tick, tick_duration, trades_per_day, growth_rate=None, target_profit=None):
    if target_profit is not None and growth_rate is not None:
        implied_growth_rate = (target_profit / stake) * 100

        if not math.isclose(implied_growth_rate, growth_rate, rel_tol=0.001):
            raise ValueError(
                f"Inconsistent inputs: Target profit of {target_profit} "
                f"implies {implied_growth_rate:.2f}% growth, but you entered {growth_rate:.2f}%."
            )

        growth_rate = implied_growth_rate  # Use target_profit to derive growth_rate

    elif target_profit is not None:
        growth_rate = (target_profit / stake) * 100

    elif growth_rate is not None:
        if growth_rate > 5:
            raise ValueError("Deriv Accumulator growth rate cannot exceed 5%")
        target_profit = (growth_rate / 100) * stake

    else:
        raise ValueError("Provide at least one: target profit or growth rate")

# Check if growth_rate exceeds 5%
# if growth_rate > 5:
    ...


if __name__ == "__main__":
    main()