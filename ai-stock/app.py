from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import requests
from bs4 import BeautifulSoup
import datetime

app = Flask(__name__)

def get_stock_data(symbol):
    # Taiwan stocks in yfinance usually end with .TW or .TWO
    # We try .TW first, then .TWO if not found
    ticker_symbol = f"{symbol}.TW"
    ticker = yf.Ticker(ticker_symbol)
    
    if ticker.history(period="1d").empty:
        ticker_symbol = f"{symbol}.TWO"
        ticker = yf.Ticker(ticker_symbol)
        if ticker.history(period="1d").empty:
            return None, None

    # Price data
    hist = ticker.history(period="1y")
    
    # Financials
    info = ticker.info
    financials = ticker.financials
    balance_sheet = ticker.balance_sheet
    
    return ticker, hist

def get_cnyes_news(symbol):
    url = f"https://m.cnyes.com/news?keyword={symbol}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # This is a simplified scraping logic; actual selectors may vary
        news_list = []
        # Look for news items (this is an example, cnyes might change structure)
        articles = soup.find_all('div', class_='news-item') or soup.find_all('a')
        for art in articles[:5]:
            title = art.text.strip()
            link = art.get('href') if art.name == 'a' else ""
            if symbol in title:
                news_list.append({'title': title, 'link': link})
        return news_list
    except Exception as e:
        print(f"News error: {e}")
        return []

def generate_chart(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Close Price', line=dict(color='blue')))
    
    # SMA 20
    df['SMA20'] = df['Close'].rolling(window=20).mean()
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA20'], name='SMA 20', line=dict(color='orange')))
    
    # SMA 50
    df['SMA50'] = df['Close'].rolling(window=50).mean()
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA50'], name='SMA 50', line=dict(color='red')))
    
    fig.update_layout(
        title=f"Stock Price Trend: {symbol}",
        xaxis_title="Date",
        yaxis_title="Price (TWD)",
        template="plotly_white"
    )
    return pio.to_html(fig, full_html=False)

def perform_analysis(ticker, hist):
    info = ticker.info
    # Basic Technical indicators
    current_price = hist['Close'].iloc[-1]
    sma20 = hist['Close'].rolling(window=20).mean().iloc[-1]
    sma50 = hist['Close'].rolling(window=50).mean().iloc[-1]
    
    trend = "看漲 (Bullish)" if current_price > sma20 > sma50 else "看跌 (Bearish)" if current_price < sma20 < sma50 else "盤整 (Sideways)"
    
    # Financial health
    pe = info.get('trailingPE', 'N/A')
    pb = info.get('priceToBook', 'N/A')
    dividend_yield = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 'N/A'
    
    report = f"""
    ### 專業分析報告
    **目前股價**: {current_price:.2f} TWD
    **趨勢判定**: {trend}
    
    **技術面分析**:
    - 股價目前處於 {trend} 狀態。
    - 20日均線 ({sma20:.2f}) 與 50日均線 ({sma50:.2f}) 的關係顯示市場目前 { '多頭排列' if sma20 > sma50 else '空頭排列' }。
    
    **基本面分析**:
    - P/E Ratio: {pe} 
    - P/B Ratio: {pb}
    - 殖利率: {dividend_yield:.2f}% (若可用)
    
    **綜合建議**:
    根據目前的技術面與基本面指標，該股票呈現 {trend} 走勢。建議投資者關注 { '關鍵壓力位' if trend == '看漲 (Bullish)' else '關鍵支撐位' } 並參考近期新聞面資訊。
    """
    return report

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form.get('symbol')
    if not symbol:
        return "Please enter a stock code", 400
    
    ticker, hist = get_stock_data(symbol)
    if ticker is None:
        return "Stock not found", 404
    
    chart_html = generate_chart(hist, symbol)
    news = get_cnyes_news(symbol)
    report = perform_analysis(ticker, hist)
    
    return render_template('index.html', 
                           symbol=symbol, 
                           chart_html=chart_html, 
                           news=news, 
                           report=report)

if __name__ == '__main__':
    app.run(debug=True)
