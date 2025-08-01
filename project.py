class Account():
    def __init__(self, name):
        if not name.isalpha():
            raise ValueError("Please enter a Valid Name")
        self.name = name
    
    def __str__(self):
        return f"\nOk {self.name} this is TradeCalc where we make trading easier by giving you ideal calculations to guide your trade. What would you like to do?\nStop-Loss Calculation   -s\nTake Profit Calculation   -t\nReward:Risk Ratio Calculation   -r\nDeriv Accumulator Calculation   -d"
    

def main():
    name = input("Welcome, what's your name? ")
    account = Account(name)
    print(account)

    while True:
        try: 
            choice = input("").strip()
            if choice not in ("s", "t", "r", "d"):
                raise ValueError("Enter a valid input 's', 't', 'r' or 'd'")
            if choice == "s":
                stop_loss()
            elif choice == "t":
                take_profit()
            elif choice == "r":
                reward_risk()
            elif choice == "d":
                deriv_accumulator()
            break  # Exit loop after successful function call
        except ValueError:
            print("Enter a valid input 's', 't', 'r' or 'd'")
        except TypeError:
            print("Invalid input")
    

def stop_loss():
    ...

def take_profit():
    ...

def reward_risk():
    ...

def deriv_accumulator():
    ...

if __name__ == "__main__":
    main()