import os

# App Configuration
APP_TITLE = "Crypto Price Tracker"
APP_ICON = "₿"

# API Configuration
COINGECKO_BASE_URL = "https://api.coingecko.com/api/v3"
API_TIMEOUT = 10  # seconds
CACHE_TTL_CURRENT_DATA = 60  # seconds
CACHE_TTL_HISTORICAL_DATA = 3600  # seconds (1 hour)
CACHE_TTL_COIN_LIST = 300  # seconds (5 minutes)

# Chart Configuration
CHART_HEIGHT = 500
CHART_COLOR = "#00D4AA"
CHART_FILL_COLOR = "rgba(0, 212, 170, 0.1)"

# Popular Coins (can be customized)
POPULAR_COINS = {
    'bitcoin': 'Bitcoin (BTC)',
    'ethereum': 'Ethereum (ETH)',
    'binancecoin': 'Binance Coin (BNB)',
    'cardano': 'Cardano (ADA)',
    'solana': 'Solana (SOL)',
    'xrp': 'XRP (XRP)',
    'polkadot': 'Polkadot (DOT)',
    'dogecoin': 'Dogecoin (DOGE)',
    'avalanche-2': 'Avalanche (AVAX)',
    'chainlink': 'Chainlink (LINK)',
    'polygon': 'Polygon (MATIC)',
    'litecoin': 'Litecoin (LTC)',
    'uniswap': 'Uniswap (UNI)',
    'cosmos': 'Cosmos (ATOM)',
    'algorand': 'Algorand (ALGO)',
    'stellar': 'Stellar (XLM)',
    'vechain': 'VeChain (VET)',
    'filecoin': 'Filecoin (FIL)',
    'tron': 'TRON (TRX)',
    'monero': 'Monero (XMR)'
}

# UI Configuration
AUTO_REFRESH_INTERVAL = 60  # seconds
DEFAULT_DAYS_HISTORY = 365  # 52 weeks
DESCRIPTION_MAX_LENGTH = 500

# Styling
GRADIENT_COLORS = {
    'primary': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    'secondary': 'linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)',
    'card_background': 'rgba(255, 255, 255, 0.1)',
    'text_color': 'white'
}