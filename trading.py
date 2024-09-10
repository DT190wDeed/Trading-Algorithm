import yfinance as yf
import pandas as pd
import time
import warnings

warnings.filterwarnings("ignore")

print("""

       .---.
       |---|
       |---|
       |---|
   .---^ - ^---.      _____            _ _           
   :___________:     |_   _| _ __ _ __| (_)_ _  __ _ 
      |  |//|          | || '_/ _` / _` | | ' \/ _` |
      |  |//|          |_||_| \__,_\__,_|_|_||_\__, |
      |  |//|                                  |___/ 
      |  |//|
      |  |//|          * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR     🎁
      |  |//|          * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
      |  |.-|          * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
      |.-'**|          * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
       \***/           * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
        \*/            * CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
         V
                                        Make by DT190.
        '
         ^'                            Telegram : DT190_R 
        (_)                            Discord : sqldtw

""")

def get_currency_data(symbol, period='1d', interval='1m'):
    ticker = f"{symbol}=X"
    data = yf.download(tickers=ticker, period=period, interval=interval, progress=False)
    return data

def calculate_ma(data, short_window=14, long_window=50):
    data['MA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['MA_Long'] = data['Close'].rolling(window=long_window).mean()
    return data

currency_pair = input("Choose a currency pair (EURUSD, USDCHF, GBPUSD): ")

first_iteration = True

while True:
    data = get_currency_data(currency_pair, period='5d', interval='1m')

    data = calculate_ma(data)

    latest_data = data.iloc[-1]
    ma_short = latest_data['MA_Short']
    ma_long = latest_data['MA_Long']

    if pd.notna(ma_short) and pd.notna(ma_long):
        if ma_short > ma_long:
            signal = f"Buy signal on {currency_pair} ↗️"
        elif ma_short < ma_long:
            signal = f"Sell signal on {currency_pair} ↘️"
        else:
            signal = f"No clear signal on {currency_pair}"
    else:
        signal = f"Insufficient data to generate signals for {currency_pair}"

    print(signal)

    if first_iteration:
        stop_signal = input("Press '*' to stop or Enter to continue: ")
        first_iteration = False
    else:
        stop_signal = input()

    if stop_signal == "*":
        print("Stopping the trading bot.")
        break

    time.sleep(10)  
