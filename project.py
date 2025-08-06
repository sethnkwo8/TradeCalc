from functions import get_entry_price, get_position_size, get_stop_loss_percentage, get_valid_trade_direction
from functions import get_take_profit_pct, get_take_profit_pce, get_stop_loss_price, get_stake, get_take_profit_tick
from functions import get_growth_rate, get_target_profit, get_trades_per_day, get_tick_duration, get_ticks_per_trade
from functions import growth_rate_exceeds, deriv_output_format, bar_chart, get_chart
import math
import csv
import os
import sys

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
                trade_direction = input("Enter trade direction (long or short): ").strip().lower()
                trade_direction = get_valid_trade_direction
                stop_loss_price, risk_per_unit, potential_loss = stop_loss(entry_price, stop_loss_percentage, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"""
🔻 Stop Loss Analysis

Trade Type      : {"Long" if trade_direction == "long" else "Short"}
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
                trade_direction = get_valid_trade_direction
                take_profit_price, reward_per_unit, total_reward = take_profit(entry_price, take_profit_pct, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"""
📈 Take Profit Analysis

Trade Type         : {"Long" if trade_direction == "long" else "Short"}
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
                trade_direction = get_valid_trade_direction
                ratio, reward_per_unit, risk_per_unit, total_reward, total_risk = reward_risk(entry_price, take_profit_pce, stop_loss_price, position_size, trade_direction)
                print("\n--- CALCULATION RESULTS ---")
                print(f"""
📊 Reward-to-Risk Analysis

Trade Type       : {"Long" if trade_direction == "long" else "Short"}
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
                formatted_output = deriv_output_format(**results)
                print("\n", formatted_output)
                fields = ["stake",
                           "growth rate",
                           "target profit",
                           "profit per tick",
                           "tick duration",
                           "trades per day",
                        #    "ticks per trade",
                           "compound mode",
                           "no of trades",
                           "actual profit",
                           "targets"
                           ]
                
                csv_results = {
    "stake": f'${results["stake"]} ',
    "growth rate": f'{results["growth_rate"]}% ',
    "target profit": f'${results["target_profit"]} ',
    "profit per tick": f'${results["take_profit_tick"]} ',
    "tick duration": f'{results["tick_duration"]} mins ',
    "trades per day": f'{results["trades_per_day"]} trades per day ',
    "compound mode": f'{results["compound_mode"]} ' ,
    "no of trades": f'{results.get("no_trades") }' or "N/A ",
    "actual profit": f'${results.get("actual_profit", "N/A")} ',
    "targets": ", ".join([f"{t:.2f}" for t in results["targets"]]) if results["targets"] else "N/A "
}

                file_exists = os.path.exists("Trades History.csv")
                with open("Trades History.csv", "a") as file:
                    writer = csv.DictWriter(file, fieldnames=fields)

                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(csv_results)

                if get_chart() == "yes":
                    bar_chart(stake, take_profit_tick, trades_per_day, results["compound_mode"], results["targets"])
                elif get_chart() == "no":
                    sys.exit()
                break  # Exit loop after successful function call

            else:
                print("Enter a valid input 's', 't', 'r' or 'd'")
                continue

        except Exception as e:
            print(f"⚠️ Invalid input: {e}")
            continue
        
def stop_loss(entry_price, stop_loss_percentage, position_size, trade_direction):
    if trade_direction not in ("long", "short"):
        raise ValueError("Trade direction must be 'long' or 'short'")
    
    risk_per_unit = (entry_price * stop_loss_percentage) / 100
    stop_loss_price = entry_price - risk_per_unit if trade_direction == "long" else entry_price + risk_per_unit
    units = position_size / entry_price
    potential_loss = risk_per_unit * units
    return stop_loss_price, risk_per_unit, potential_loss



def take_profit(entry_price, take_profit_pct, position_size, trade_direction):
    if trade_direction not in ("long", "short"):
        raise ValueError("Trade direction must be 'long' or 'short'")
    
    take_profit_price = entry_price * (1 + take_profit_pct / 100) if trade_direction == "long" else entry_price * (1 - take_profit_pct / 100)
    reward_per_unit = abs(take_profit_price - entry_price)
    units = position_size / entry_price
    total_reward = reward_per_unit * units
    return take_profit_price, reward_per_unit, total_reward


def reward_risk(entry_price, take_profit_price, stop_loss_price, position_size, trade_direction):
    if trade_direction not in ("long", "short"):
        raise ValueError("Trade direction must be 'long' or 'short'")

    reward_per_unit = take_profit_price - entry_price if trade_direction == "long" else entry_price - take_profit_price
    risk_per_unit = entry_price - stop_loss_price if trade_direction == "long" else stop_loss_price - entry_price
    total_reward = reward_per_unit * position_size
    total_risk = risk_per_unit * position_size
    ratio = abs(reward_per_unit / risk_per_unit)
    return ratio, reward_per_unit, risk_per_unit, total_reward, total_risk

        
def deriv_accumulator(stake, take_profit_tick, tick_duration, trades_per_day, ticks_per_trade):
    try:
        growth_rate = get_growth_rate() or None
        target_profit = get_target_profit() or None

        result = accumulator_core(
            stake,
            take_profit_tick,
            tick_duration,
            trades_per_day,
            ticks_per_trade,
            growth_rate=growth_rate,
            target_profit=target_profit
        )
        return result

    except ValueError as e:
        return f"⚠️ Accumulator Error: {e}"

    except Exception as e:
        return f"⚠️ Unexpected Error: {e}"


def accumulator_core(
    stake,
    take_profit_tick,
    tick_duration,
    trades_per_day,
    ticks_per_trade,
    growth_rate=None,
    target_profit=None
    ):
        if target_profit is not None and growth_rate is not None:
            implied_growth_rate = (target_profit / stake) * 100
            if not math.isclose(implied_growth_rate, growth_rate, rel_tol=0.001):
                raise ValueError(
                    f"Inconsistent inputs: Target profit of ${target_profit:.2f} "
                    f"implies {implied_growth_rate:.2f}% growth, but got {growth_rate:.2f}%."
                )
            growth_rate = implied_growth_rate
        
        if growth_rate is None and target_profit is None:
            raise ValueError("You must enter either a growth rate or target profit.")

        elif target_profit is not None:
            growth_rate = (target_profit / stake) * 100

        elif growth_rate is not None:
            target_profit = (growth_rate / 100) * stake

        else:
            raise ValueError("Provide at least one: target profit or growth rate")

        compound_mode = False
        no_trades = None
        targets = None
        actual_profit = None

        if growth_rate > 5:
            compound_mode = True
            targets, total_target, no_trades, actual_profit = growth_rate_exceeds(stake, target_profit)

        ticks_needed = target_profit / take_profit_tick if take_profit_tick else None
        estimated_time = tick_duration * ticks_needed if ticks_needed and tick_duration else None
        daily_sessions_target = take_profit_tick * trades_per_day if take_profit_tick and trades_per_day else None

        return {
        "stake": stake,
        "growth_rate": round(growth_rate, 2),
        "target_profit": round(target_profit, 2),
        "take_profit_tick": take_profit_tick,
        "tick_duration": tick_duration,
        "trades_per_day": trades_per_day,
        "compound_mode": compound_mode,
        "no_trades": no_trades,
        "actual_profit": actual_profit,
        "targets": targets
    }

        
if __name__ == "__main__":
    main()