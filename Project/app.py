import matplotlib.pyplot as plt

# --- Algorithms ---
def SMA(prices, window):
    sma_values = []
    for i in range(len(prices) - window + 1):
        avg = sum(prices[i:i+window]) / window
        sma_values.append(avg)
    return [None]*(window-1) + sma_values

def EMA(prices, window):
    ema_values = []
    k = 2 / (window + 1)
    ema = prices[0]
    ema_values.append(ema)
    for price in prices[1:]:
        ema = (price * k) + (ema * (1 - k))
        ema_values.append(ema)
    return ema_values

def LinearRegression(prices):
    n = len(prices)
    x = list(range(n))
    sum_x = sum(x)
    sum_y = sum(prices)
    sum_xy = sum(x[i]*prices[i] for i in range(n))
    sum_x2 = sum(i*i for i in x)
    m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    b = (sum_y - m*sum_x) / n
    return [m*i + b for i in x]

# --- Timeframe selection ---
timeframe = input("Enter timeframe (H/D/M/Y): ").strip().upper()

if timeframe == "H":
    options = ["1h", "4h", "6h", "12h"]
elif timeframe == "D":
    options = ["1d", "3d", "5d"]
elif timeframe == "M":
    options = ["1m", "3m", "6m"]
elif timeframe == "Y":
    options = ["1y", "3y", "5y"]
else:
    print("Invalid timeframe, defaulting to Daily 1d")
    timeframe = "D"
    options = ["1d"]

print("Available options:", ", ".join(options))
period = input("Choose period: ").strip().lower()

# --- Number of data points ---
n_points = int(input("How many consecutive periods do you want to enter? "))

# --- User input for prices ---
print(f"Enter {n_points} prices for {timeframe}-{period}:")
prices = []
for i in range(n_points):
    price = float(input(f"Price {i+1}: "))
    prices.append(price)

# --- Run algorithms ---
sma = SMA(prices, 3)
ema = EMA(prices, 3)
lr = LinearRegression(prices)

# --- Plot ---
plt.figure(figsize=(10,6))
plt.plot(prices, label=f"Prices ({timeframe}-{period})", marker='o')
plt.plot(sma, label="SMA (3)", linestyle="--")
plt.plot(ema, label="EMA (3)", linestyle="-.")
plt.plot(lr, label="Linear Regression", linestyle=":")

plt.title("Financial Market Analysis Algorithms")
plt.xlabel(f"Time ({n_points} periods)")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()