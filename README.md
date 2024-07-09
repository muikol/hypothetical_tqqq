# Generierung Hypothetischer TQQQ-Daten ab 2004

Dieses Projekt generiert hypothetische historische Daten für den TQQQ-ETF ab dem Jahr 2004 basierend auf den tatsächlichen historischen Daten des QQQ-ETFs. Der TQQQ ist ein gehebelter ETF, der die dreifache tägliche Performance des QQQ nachbilden soll. Da der TQQQ erst später eingeführt wurde, sind historische Daten vor seiner Einführung nicht verfügbar. Dieses Skript nutzt die täglichen Renditen des QQQ, um diese Daten zu generieren.

## Anforderungen

- Python 3.x
- Pandas
- yfinance
- Matplotlib

Diese Bibliotheken können mit `pip` installiert werden:

```bash
pip install pandas yfinance matplotlib
