import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Set page configuration
st.set_page_config(
    page_title="Crypto Price Tracker",
    page_icon="₿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for crypto-themed background
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-attachment: fixed;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    
    .crypto-header {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
        text-align: center;
        color: white;
    }
    
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        backdrop-filter: blur(10px);
        margin: 10px 0;
        color: white;
    }
    
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
</style>
""", unsafe_allow_html=True)

class CryptoTracker:
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
        self.popular_coins = {
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
            'algorand': 'Algorand (ALGO)'
        }
    
    @st.cache_data(ttl=300)  # Cache for 5 minutes
    def get_coin_list(_self):
        """Get list of all available coins"""
        try:
            response = requests.get(f"{_self.base_url}/coins/list", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching coin list: {e}")
            return []
    
    @st.cache_data(ttl=60)  # Cache for 1 minute
    def get_current_price(_self, coin_id):
        """Get current price and basic info for a coin"""
        try:
            response = requests.get(
                f"{_self.base_url}/coins/{coin_id}",
                params={
                    'localization': 'false',
                    'tickers': 'false',
                    'market_data': 'true',
                    'community_data': 'false',
                    'developer_data': 'false',
                    'sparkline': 'false'
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching current price: {e}")
            return None
    
    @st.cache_data(ttl=3600)  # Cache for 1 hour
    def get_price_history(_self, coin_id, days=365):
        """Get price history for the specified number of days"""
        try:
            response = requests.get(
                f"{_self.base_url}/coins/{coin_id}/market_chart",
                params={
                    'vs_currency': 'usd',
                    'days': days,
                    'interval': 'daily'
                },
                timeout=15
            )
            response.raise_for_status()
            data = response.json()
            
            # Convert to DataFrame
            prices = data['prices']
            df = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df.drop('timestamp', axis=1)
            df = df.set_index('date')
            
            return df
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching price history: {e}")
            return pd.DataFrame()

def format_number(num):
    """Format numbers with appropriate suffixes"""
    if num >= 1e12:
        return f"${num/1e12:.2f}T"
    elif num >= 1e9:
        return f"${num/1e9:.2f}B"
    elif num >= 1e6:
        return f"${num/1e6:.2f}M"
    elif num >= 1e3:
        return f"${num/1e3:.2f}K"
    else:
        return f"${num:.2f}"

def format_percentage(pct):
    """Format percentage with color"""
    if pct > 0:
        return f"🟢 +{pct:.2f}%"
    else:
        return f"🔴 {pct:.2f}%"

def create_price_chart(df, coin_name):
    """Create an interactive price chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['price'],
        mode='lines',
        name=f'{coin_name} Price',
        line=dict(color='#00D4AA', width=2),
        fill='tonexty',
        fillcolor='rgba(0, 212, 170, 0.1)'
    ))
    
    fig.update_layout(
        title=f'{coin_name} - 52 Week Price Chart',
        title_font_size=20,
        title_font_color='white',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        height=500,
        hovermode='x unified'
    )
    
    fig.update_xaxis(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxis(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.1)')
    
    return fig

def main():
    # Initialize the tracker
    tracker = CryptoTracker()
    
    # Header
    st.markdown("""
    <div class="crypto-header">
        <h1>₿ Crypto Price Tracker</h1>
        <p>Real-time cryptocurrency prices and 52-week charts powered by CoinGecko API</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for coin selection
    st.sidebar.title("🪙 Select Cryptocurrency")
    
    # Option to choose from popular coins or search all
    selection_type = st.sidebar.radio(
        "Selection Method:",
        ["Popular Coins", "Search All Coins"]
    )
    
    selected_coin_id = None
    
    if selection_type == "Popular Coins":
        # Popular coins dropdown
        coin_options = list(tracker.popular_coins.keys())
        coin_labels = list(tracker.popular_coins.values())
        
        selected_index = st.sidebar.selectbox(
            "Choose a cryptocurrency:",
            range(len(coin_options)),
            format_func=lambda x: coin_labels[x],
            index=0
        )
        selected_coin_id = coin_options[selected_index]
        selected_coin_name = coin_labels[selected_index]
        
    else:
        # Search all coins
        with st.sidebar:
            with st.spinner("Loading coin list..."):
                all_coins = tracker.get_coin_list()
            
            if all_coins:
                coin_names = [f"{coin['name']} ({coin['symbol'].upper()})" for coin in all_coins]
                coin_ids = [coin['id'] for coin in all_coins]
                
                search_term = st.text_input("Search for a cryptocurrency:", "bitcoin")
                
                # Filter coins based on search term
                if search_term:
                    filtered_indices = [i for i, name in enumerate(coin_names) 
                                      if search_term.lower() in name.lower()]
                    filtered_names = [coin_names[i] for i in filtered_indices]
                    filtered_ids = [coin_ids[i] for i in filtered_indices]
                    
                    if filtered_names:
                        selected_index = st.selectbox(
                            "Select from search results:",
                            range(len(filtered_names)),
                            format_func=lambda x: filtered_names[x]
                        )
                        selected_coin_id = filtered_ids[selected_index]
                        selected_coin_name = filtered_names[selected_index]
    
    # Main content area
    if selected_coin_id:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Get current price data
            with st.spinner("Fetching current price data..."):
                current_data = tracker.get_current_price(selected_coin_id)
            
            if current_data:
                # Display current price and metrics
                market_data = current_data.get('market_data', {})
                current_price = market_data.get('current_price', {}).get('usd', 0)
                price_change_24h = market_data.get('price_change_percentage_24h', 0)
                price_change_7d = market_data.get('price_change_percentage_7d', 0)
                market_cap = market_data.get('market_cap', {}).get('usd', 0)
                volume_24h = market_data.get('total_volume', {}).get('usd', 0)
                
                # Price metrics row
                metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                
                with metric_col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>Current Price</h3>
                        <h2>${current_price:,.2f}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>24h Change</h3>
                        <h2>{format_percentage(price_change_24h)}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col3:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>Market Cap</h3>
                        <h2>{format_number(market_cap)}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col4:
                    st.markdown(f"""
                    <div class="metric-card">
                        <h3>24h Volume</h3>
                        <h2>{format_number(volume_24h)}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Get and display price chart
                with st.spinner("Loading 52-week price chart..."):
                    price_history = tracker.get_price_history(selected_coin_id, days=365)
                
                if not price_history.empty:
                    fig = create_price_chart(price_history, current_data['name'])
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Additional statistics
                    st.subheader("📊 52-Week Statistics")
                    
                    week_52_high = price_history['price'].max()
                    week_52_low = price_history['price'].min()
                    week_52_change = ((current_price - price_history['price'].iloc[0]) / price_history['price'].iloc[0]) * 100
                    
                    stat_col1, stat_col2, stat_col3 = st.columns(3)
                    
                    with stat_col1:
                        st.metric("52W High", f"${week_52_high:,.2f}")
                    
                    with stat_col2:
                        st.metric("52W Low", f"${week_52_low:,.2f}")
                    
                    with stat_col3:
                        st.metric("52W Change", f"{week_52_change:.2f}%")
                else:
                    st.error("Unable to load price history data.")
            else:
                st.error("Unable to load cryptocurrency data.")
        
        with col2:
            # Additional coin information
            if current_data:
                st.subheader("ℹ️ Coin Information")
                
                # Coin image
                if 'image' in current_data and 'large' in current_data['image']:
                    st.image(current_data['image']['large'], width=100)
                
                st.write(f"**Name:** {current_data.get('name', 'N/A')}")
                st.write(f"**Symbol:** {current_data.get('symbol', 'N/A').upper()}")
                st.write(f"**Rank:** #{current_data.get('market_cap_rank', 'N/A')}")
                
                if 'description' in current_data and 'en' in current_data['description']:
                    description = current_data['description']['en']
                    if description:
                        # Truncate description
                        short_desc = description[:500] + "..." if len(description) > 500 else description
                        st.write(f"**Description:** {short_desc}")
                
                # Links
                links = current_data.get('links', {})
                if links.get('homepage') and links['homepage'][0]:
                    st.write(f"**Website:** [Link]({links['homepage'][0]})")
    
    # Auto-refresh option
    st.sidebar.markdown("---")
    auto_refresh = st.sidebar.checkbox("Auto-refresh every 60 seconds")
    
    if auto_refresh:
        time.sleep(60)
        st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("*Data provided by CoinGecko API*")

if __name__ == "__main__":
    main()