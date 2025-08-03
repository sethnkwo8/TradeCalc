from functions import get_entry_price, get_position_size, get_stop_loss_percentage, get_trade_direction
from functions import get_take_profit_pct, get_take_profit_pce, get_stop_loss_price, get_stake, get_take_profit_tick
from functions import get_growth_rate, get_target_profit, get_trades_per_day, get_tick_duration, get_ticks_per_trade
from functions import growth_rate_exceeds, deriv_output_format
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
            choice = input("Enter your choice (s, t, r, d): ").strip().lower()

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
                break

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
                break

            elif choice == "r":
                entry_price = get_entry_price()
                take_profit_pce = get_take_profit_pce()
                stop_loss_price = get_stop_loss_price()
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
                break
                
            elif choice == "d":
                stake = get_stake()
                take_profit_tick = get_take_profit_tick()
                tick_duration = get_tick_duration()
                trades_per_day = get_trades_per_day()
                ticks_per_trade = get_ticks_per_trade()
                results = deriv_accumulator(stake, take_profit_tick, tick_duration, trades_per_day, ticks_per_trade)
                print("\n")
                print(results)
                break  # Exit loop after successful function call

            else:
                print("Enter a valid input 's', 't', 'r' or 'd'")
                continue
        except TypeError:
            print("Invalid input")
        
def stop_loss(entry_price, stop_loss_percentage, position_size, trade_direction):
    while True:
        try:
            risk_per_unit = (entry_price * stop_loss_percentage)/ 100
            if trade_direction == "long":
                stop_loss_price = entry_price - risk_per_unit
            elif trade_direction == "short":
                stop_loss_price = entry_price + risk_per_unit
            else:
                print("Trade direction must be 'long' or 'short'")
                continue

            units = position_size / entry_price
            potential_loss = risk_per_unit * units

            return stop_loss_price, risk_per_unit, potential_loss
        
        except ValueError:
            print("Invalid input. Please try again.")


def take_profit(entry_price, take_profit_pct, position_size, trade_direction):
    while True:
        try:
            if trade_direction == "long":
                take_profit_price = entry_price * (1 + take_profit_pct / 100)
            elif trade_direction == "short":
                take_profit_price = entry_price * (1 - take_profit_pct / 100)
            else:
                print("Trade direction must be 'long' or 'short'")
                continue
        
            reward_per_unit = abs(take_profit_price - entry_price)
            units = position_size / entry_price
            total_reward = reward_per_unit * units

            return take_profit_price, reward_per_unit, total_reward
        
        except ValueError:
            print("Invalid input. Please try again.")

def reward_risk(entry_price, take_profit_pce, stop_loss_price, position_size, trade_direction):
    while True:
        try:
            if trade_direction == "long":
                reward_per_unit = take_profit_pce - entry_price
            elif trade_direction == "short":
                reward_per_unit = entry_price - take_profit_pce
            else:
                print("Trade direction must be 'long' or 'short'")
                continue
            
            if trade_direction == "long":
                risk_per_unit = entry_price - stop_loss_price
            elif trade_direction == "short":
                risk_per_unit = stop_loss_price - entry_price
            else:
                print("Trade direction must be 'long' or 'short'")
                continue
            
            total_reward = reward_per_unit * position_size
            total_risk = risk_per_unit * position_size
            ratio =(abs(take_profit_pce - entry_price)) / (abs(entry_price - stop_loss_price))
            return ratio, reward_per_unit, risk_per_unit, total_reward, total_risk
        
        except ValueError:
            print("Invalid input. Please try again.")
        

def deriv_accumulator(stake, take_profit_tick, tick_duration, trades_per_day, ticks_per_trade):
    while True:
        try:
            growth_rate = get_growth_rate()
            target_profit = get_target_profit()

            if target_profit is not None and growth_rate is not None:
                implied_growth_rate = (target_profit / stake) * 100
                if not math.isclose(implied_growth_rate, growth_rate, rel_tol=0.001):
                    print(
                        f"Inconsistent inputs: Target profit of ${target_profit:.2f} "
                        f"implies {implied_growth_rate:.2f}% growth, but you entered {growth_rate:.2f}%."
                    )
                    continue
                growth_rate = implied_growth_rate

            elif target_profit is not None:
                growth_rate = (target_profit / stake) * 100

            elif growth_rate is not None:
                target_profit = (growth_rate / 100) * stake

            else:
                print("Provide at least one: target profit or growth rate")
                continue  # re-prompt

            # Initialize optional outputs
            compound_mode = False
            no_trades = None
            targets = None
            actual_profit = None

            if growth_rate > 5:
                compound_mode = True
                targets, total_target, no_trades, actual_profit = growth_rate_exceeds(stake, target_profit)

            # Ticks logic
            ticks_needed = target_profit / take_profit_tick if take_profit_tick else None
            estimated_time = tick_duration * ticks_needed if ticks_needed and tick_duration else None
            daily_sessions_target = take_profit_tick * trades_per_day if take_profit_tick and trades_per_day else None

            final = deriv_output_format(
                stake,
                growth_rate,
                target_profit,
                take_profit_tick,
                trades_per_day,
                tick_duration,
                compound_mode,
                no_trades,
                targets,
                actual_profit
            )

            return final

        except ValueError:
            print("Invalid input. Please try again.")


    

        
if __name__ == "__main__":
    main()