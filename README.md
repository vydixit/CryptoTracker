# 🚀 Crypto Price Tracker

A beautiful and interactive cryptocurrency price tracking application built with Streamlit and powered by the CoinGecko API.

## Features

- 🎨 **Beautiful Crypto-themed UI** with gradient backgrounds and glassmorphism effects
- 📊 **Real-time Price Data** from CoinGecko API
- 📈 **Interactive 52-week Price Charts** using Plotly
- 💰 **Current Price Metrics** including 24h change, market cap, and volume
- 🔍 **Dual Selection Mode**: Choose from popular coins or search all available cryptocurrencies
- 📱 **Responsive Design** that works on desktop and mobile
- ⚡ **Auto-refresh Option** for real-time updates
- 📊 **52-week Statistics** including highs, lows, and yearly change

## Installation

1. **Clone or download** this repository
2. **Navigate** to the project directory:
   ```bash
   cd CryptoTracker
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run app.py
   ```
2. **Open your browser** and go to `http://localhost:8501`
3. **Select a cryptocurrency** from the sidebar:
   - Choose "Popular Coins" for quick access to major cryptocurrencies
   - Choose "Search All Coins" to search through thousands of available coins
4. **View real-time data** including:
   - Current price and 24-hour change
   - Market capitalization and trading volume
   - Interactive 52-week price chart
   - 52-week high, low, and yearly performance
5. **Enable auto-refresh** for live updates every 60 seconds

## Supported Cryptocurrencies

The app includes quick access to popular cryptocurrencies:
- Bitcoin (BTC)
- Ethereum (ETH)
- Binance Coin (BNB)
- Cardano (ADA)
- Solana (SOL)
- XRP (XRP)
- Polkadot (DOT)
- Dogecoin (DOGE)
- And many more...

You can also search for any cryptocurrency available on CoinGecko (thousands of options).

## API Information

This application uses the **CoinGecko API** (free tier) which provides:
- Real-time cryptocurrency prices
- Historical price data
- Market statistics
- Coin information and metadata

No API key is required for the free tier, but there are rate limits:
- 10-30 calls/minute depending on the endpoint
- Data is cached in the app to minimize API calls

## Technical Details

### Built With
- **Streamlit** - Web app framework
- **Plotly** - Interactive charts
- **Pandas** - Data manipulation
- **Requests** - API calls
- **CoinGecko API** - Cryptocurrency data

### Key Features
- **Caching**: API responses are cached to improve performance and reduce API calls
- **Error Handling**: Robust error handling for API failures and network issues
- **Responsive Design**: Works well on different screen sizes
- **Real-time Updates**: Optional auto-refresh for live data

## Troubleshooting

### Common Issues

1. **"Error fetching data"**: 
   - Check your internet connection
   - The CoinGecko API might be temporarily unavailable
   - Try refreshing the page

2. **Slow loading**:
   - The free CoinGecko API has rate limits
   - Data is cached to improve performance on subsequent loads

3. **Missing chart data**:
   - Some newer or less popular coins might have limited historical data
   - Try selecting a more established cryptocurrency

### Dependencies Issues
If you encounter issues with dependencies, try:
```bash
pip install --upgrade pip
pip install -r requirements.txt --upgrade
```

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## Disclaimer

This application is for educational and informational purposes only. Cryptocurrency investments carry risk, and you should do your own research before making any investment decisions. The data provided is for informational purposes only and should not be considered as financial advice.