import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Laden Sie die QQQ- und TQQQ-Daten herunter
qqq = yf.download('QQQ', start='2004-01-01')
tqqq = yf.download('TQQQ')

# Berechnen Sie die täglichen Renditen des QQQ
qqq['Daily Return'] = qqq['Adj Close'].pct_change()

# Berechnen Sie die hypothetischen TQQQ-Daten ab 2004
tqqq_start_date = tqqq.index[0]

# Initialisieren des DataFrame für die hypothetischen TQQQ-Daten
hypothetical_tqqq = qqq[qqq.index < tqqq_start_date].copy()

# Setzen Sie die Startwerte für Open, High, Low, Close basierend auf dem ersten TQQQ-Wert
initial_ohlc = tqqq.loc[tqqq_start_date, ['Open', 'High', 'Low', 'Close']]
hypothetical_tqqq[['Open', 'High', 'Low', 'Close']] = initial_ohlc.values

# Iterieren über die täglichen Renditen und berechnen die hypothetischen TQQQ-OHLC-Daten
for i in range(1, len(hypothetical_tqqq)):
    prev_close = hypothetical_tqqq.iloc[i - 1]['Close']
    daily_return = 3 * hypothetical_tqqq.iloc[i]['Daily Return']
    
    # Berechnen Sie die hypothetischen OHLC-Werte
    open_price = prev_close * (1 + daily_return)
    close_price = open_price  # Angenommen, Open und Close sind gleich für die Berechnung
    high_price = max(open_price, close_price)
    low_price = min(open_price, close_price)
    
    hypothetical_tqqq.iloc[i, hypothetical_tqqq.columns.get_loc('Open')] = open_price
    hypothetical_tqqq.iloc[i, hypothetical_tqqq.columns.get_loc('High')] = high_price
    hypothetical_tqqq.iloc[i, hypothetical_tqqq.columns.get_loc('Low')] = low_price
    hypothetical_tqqq.iloc[i, hypothetical_tqqq.columns.get_loc('Close')] = close_price

# Kombinieren der hypothetischen und realen TQQQ-Daten
combined_tqqq = pd.concat([hypothetical_tqqq[['Open', 'High', 'Low', 'Close']], tqqq[['Open', 'High', 'Low', 'Close']]], axis=0)

# Plotten der kombinierten Daten mit QQQ in einem separaten Pane darunter
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(14, 10))

ax1.plot(combined_tqqq['Close'], label='TQQQ')
ax1.set_title('Hypothetische und reale TQQQ-Daten ab 2004')
ax1.legend()

ax2.plot(qqq['Close'], label='QQQ', color='orange')
ax2.set_title('QQQ-Daten ab 2004')
ax2.legend()

plt.show()

# Plotten der Daten von 2004 bis ein Jahr nach dem Startdatum der realen TQQQ-Daten
end_date = tqqq_start_date + pd.DateOffset(years=1)
fig, (ax3, ax4) = plt.subplots(2, 1, sharex=True, figsize=(14, 10))

ax3.plot(combined_tqqq.loc['2004-01-01':end_date, 'Close'], label='TQQQ')
ax3.set_title('Hypothetische TQQQ-Daten von 2004 bis ein Jahr nach Startdatum der realen Daten')
ax3.legend()

ax4.plot(qqq.loc['2004-01-01':end_date, 'Close'], label='QQQ', color='orange')
ax4.set_title('QQQ-Daten von 2004 bis ein Jahr nach Startdatum der realen TQQQ-Daten')
ax4.legend()

plt.show()
