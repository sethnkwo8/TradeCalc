# 📊 TradeCalc — Trading Calculator

#### 🎥 Video Demo: [https://youtu.be/oBtbOppqQcg](https://youtu.be/oBtbOppqQcg)

---

## 📌 Description
**TradeCalc** is a Python-based trading calculator designed for quick and accurate trade planning.  
It supports multiple calculation modes to suit different trading strategies:

### 📈 Profit Calculation Modes
- **Standard Mode** — Calculate profits using fixed stake and profit per tick.
- **Compound Mode** — Automatically reinvest profits to accelerate growth.
- **Target Profit Mode** — Work backward from your target profit to determine required trades.
- **Growth Rate Mode** — Calculate profits based on a daily growth percentage.
- **Tick Duration Mode** — Estimate total trading time based on tick duration.
- **Hybrid Mode** — Combine compounding with set trade limits for flexible planning.

### 🛡 Risk Management Modes
- **Stop Loss Calculation Mode** — Determine the maximum loss allowed per trade or session.
- **Take Profit Mode** — Set profit targets and calculate the required trade conditions.
- **Reward-to-Risk Ratio Mode** — Compare potential rewards to potential losses for informed decision-making.

### 📊 Extra Features
- Input validation to prevent incorrect calculations.
- Save all trade results to a **CSV file** for tracking.
- Generate **visual profit charts**.
- Simple, clean **CustomTkinter GUI**.
- Adaptable for both **fixed stake** and **compounding strategies**.

---

## 🖥 Technologies Used
- **Python 3.8+**
- **CustomTkinter** — Modern UI framework for Tkinter.
- **Matplotlib** — For chart plotting.
- **CSV Module** — To store trade history.
- **OS Module** — File management.

---

## 🚀 Features
- Calculate profits across different trading strategies.
- Switch between **profit-focused** and **risk management** modes.
- View daily profit growth in a bar chart.
- Store trade history automatically.
- Clean, user-friendly interface.

---

## 📂 Project Structure
TradeCalc/
│
├── TradeCalc.py            # Main program entry point
├── project.py              # Core calculation functions
├── functions.py            # Helper functions
│
├── requirements.txt         # Python dependencies (pip-installable)
├── README.md                # Project description, usage, and setup instructions
├── Trades History.csv       # (Optional) Generated CSV history file

---

## ⚙ How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/TradeCalc.git
cd TradeCalc

2. **Install Dependencies**
pip install -r requirements.txt

3. **Run the Program**
python TradeCalc.py