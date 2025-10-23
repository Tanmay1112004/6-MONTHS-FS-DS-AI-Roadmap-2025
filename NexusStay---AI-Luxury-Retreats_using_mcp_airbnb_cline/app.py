import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import re
import random

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="NexusStay - AI Luxury Retreats",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DARK THEME CSS ---
st.markdown("""
<style>
    /* Dark Theme Variables */
    :root {
        --primary: #FF385C;
        --secondary: #00D4AA;
        --accent: #FFB800;
        --dark: #0A0A0A;
        --darker: #050505;
        --card-dark: #1A1A1A;
        --card-darker: #151515;
        --text-primary: #FFFFFF;
        --text-secondary: #B0B0B0;
        --text-muted: #666666;
        --border: #333333;
    }
    
    /* Global Dark Theme */
    .stApp {
        background: linear-gradient(135deg, var(--darker) 0%, var(--dark) 50%, #1a1a2e 100%);
        color: var(--text-primary);
    }
    
    .main {
        background: transparent !important;
    }
    
    /* Premium Dark Cards */
    .premium-dark-card {
        background: linear-gradient(145deg, var(--card-dark) 0%, var(--card-darker) 100%);
        border-radius: 20px;
        padding: 0;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid var(--border);
        overflow: hidden;
        position: relative;
    }
    
    .premium-dark-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(255, 56, 92, 0.2);
        border-color: var(--primary);
    }
    
    .card-image {
        width: 100%;
        height: 240px;
        object-fit: cover;
        border-radius: 0;
        transition: transform 0.3s ease;
    }
    
    .premium-dark-card:hover .card-image {
        transform: scale(1.05);
    }
    
    /* Chatbot Styles */
    .chat-container {
        background: linear-gradient(145deg, var(--card-dark) 0%, var(--card-darker) 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid var(--border);
        max-height: 400px;
        overflow-y: auto;
    }
    
    .chat-message {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 15px;
        max-width: 80%;
        animation: fadeIn 0.3s ease-in;
    }
    
    .user-message {
        background: linear-gradient(135deg, var(--primary) 0%, #FF6B81 100%);
        color: white;
        margin-left: auto;
        text-align: right;
    }
    
    .bot-message {
        background: rgba(255,255,255,0.1);
        color: var(--text-primary);
        border: 1px solid var(--border);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .typing-indicator {
        display: inline-block;
        padding: 0.5rem 1rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        color: var(--text-secondary);
        font-style: italic;
    }
    
    .typing-dots {
        display: inline-block;
    }
    
    .typing-dots::after {
        content: '...';
        animation: typing 1.5s infinite;
    }
    
    @keyframes typing {
        0%, 20% { content: '.'; }
        40% { content: '..'; }
        60%, 100% { content: '...'; }
    }
    
    /* Stats Cards Dark */
    .stats-card-dark {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .stats-number {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Badge Styles */
    .superhost-badge {
        background: linear-gradient(135deg, var(--accent) 0%, #FFD700 100%);
        color: var(--dark);
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.7rem;
        font-weight: 700;
        display: inline-block;
        margin-left: 0.5rem;
        box-shadow: 0 2px 8px rgba(255, 184, 0, 0.3);
    }
    
    .amenity-item-dark {
        display: inline-flex;
        align-items: center;
        background: rgba(255,255,255,0.1);
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.8rem;
        color: var(--text-secondary);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .progress-bar {
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        height: 8px;
        margin: 0.5rem 0;
        overflow: hidden;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--primary), var(--secondary));
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- AI CHATBOT CLASS (No NLTK Required) ---
class NexusStayChatbot:
    def __init__(self):
        self.patterns = {
            'greeting': [
                (r'hello|hi|hey|hola', ['Hello! Welcome to NexusStay Luxury Retreats! 🏰', 
                                       'Hi there! Ready to find your perfect luxury stay?',
                                       'Hey! How can I help you discover elite properties today?']),
                (r'how are you|how do you do', ['I\'m fantastic! Ready to help you find luxury accommodations!',
                                              'Doing great! Excited to help you plan your luxury getaway!']),
            ],
            'help': [
                (r'help|support|assistance', ['I can help you with:\n• Finding luxury properties\n• Booking information\n• Price inquiries\n• Amenity details\n• Location recommendations\n\nWhat would you like to know?']),
            ],
            'properties': [
                (r'properties|listings|stays|accommodations', ['We have over 1,200 luxury properties worldwide! 🏰\n\n• Luxury Apartments\n• Private Villas\n• Beach Houses\n• Mountain Cabins\n• Historic Castles\n\nWhat type of property interests you?']),
            ],
            'pricing': [
                (r'price|cost|expensive|cheap|budget', ['Our luxury properties range from $200 to $2,000 per night 💎\n\n• Budget Luxury: $200-400/night\n• Premium: $400-800/night\n• Elite: $800-2,000/night\n\nWhat\'s your preferred budget range?']),
            ],
            'amenities': [
                (r'amenities|facilities|features|what included', ['Our properties include premium amenities:\n\n• High-speed WiFi\n• Luxury Kitchens\n• Private Pools\n• Hot Tubs\n• Gym Access\n• Concierge Service\n• Private Beach Access\n\nAny specific amenity you\'re looking for?']),
            ],
            'booking': [
                (r'book|reserve|make reservation|how to book', ['Booking is easy! 🚀\n\n1. Search for properties\n2. Select your dates\n3. Choose guests\n4. Click "Book Now"\n5. Get instant confirmation!\n\nWould you like me to help you find a property?']),
            ],
            'location': [
                (r'location|where|place|destination', ['We have luxury properties in 50+ countries! 🌍\n\n• New York City\n• Malibu Beach\n• Paris\n• Tokyo\n• Bali\n• Aspen\n• Edinburgh\n\nWhere would you like to stay?']),
            ],
            'cancellation': [
                (r'cancel|cancellation|refund|policy', ['Our cancellation policy:\n\n• Free cancellation within 48 hours\n• 50% refund up to 7 days before\n• Flexible dates available\n• Travel insurance recommended\n\nNeed specific cancellation details?']),
            ],
            'thanks': [
                (r'thank you|thanks|appreciate', ['You\'re welcome! 😊\nHappy to help with your luxury travel plans!',
                                                'My pleasure! Let me know if you need anything else!']),
            ],
            'search': [
                (r'search|find|look for', ['I can help you search for properties! 🔍\n\nTry using our search bar above or tell me:\n• Your destination\n• Budget range\n• Number of guests\n• Preferred amenities']),
            ],
            'recommendation': [
                (r'recommend|suggest|best|top', ['Based on popular choices, I recommend:\n\n🏙️ **City Luxury**: Skyline penthouses in New York\n🏖️ **Beach Getaway**: Private villas in Malibu\n🏔️ **Mountain Escape**: Cozy cabins in Aspen\n🏰 **Unique Stays**: Historic castles in Edinburgh\n\nWhich type interests you?']),
            ],
            'default': [
                (r'.*', ["I'm here to help you find the perfect luxury stay! 🏰\n\nTry asking about:\n• Available properties\n• Pricing\n• Locations\n• Amenities\n• Booking process",
                        "I specialize in luxury accommodations! 💎\n\nHow can I assist with:\n• Property search\n• Price ranges\n• Location advice\n• Booking help"]),
            ]
        }
    
    def preprocess_text(self, text):
        """Basic text preprocessing without NLTK"""
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def get_response(self, user_input):
        """Get chatbot response based on user input"""
        user_input = self.preprocess_text(user_input)
        
        for category, patterns in self.patterns.items():
            for pattern, responses in patterns:
                if re.search(pattern, user_input):
                    return random.choice(responses)
        
        return random.choice(self.patterns['default'][0][1])

# --- ENHANCED SAMPLE DATA ---
properties = [
    {
        "id": 1,
        "title": "Skyline Penthouse Infinity Views",
        "location": "Manhattan, New York",
        "price": 450,
        "original_price": 520,
        "type": "Luxury Apartment",
        "rating": 4.95,
        "reviews": 128,
        "superhost": True,
        "instant_book": True,
        "image": "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?q=80&w=2187&auto=format&fit=crop",
        "amenities": ["WiFi", "Kitchen", "AC", "Hot Tub", "Gym", "Pool", "Parking"],
        "bedrooms": 3,
        "bathrooms": 2,
        "guests": 6,
        "description": "Stunning penthouse with panoramic city views, modern amenities, and premium finishes throughout.",
        "popular": True,
        "featured": True,
        "discount": 15
    },
    {
        "id": 2,
        "title": "Oceanfront Villa Private Beach",
        "location": "Malibu, California",
        "price": 890,
        "original_price": 950,
        "type": "Luxury Villa",
        "rating": 4.98,
        "reviews": 76,
        "superhost": True,
        "instant_book": True,
        "image": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?q=80&w=2070&auto=format&fit=crop",
        "amenities": ["WiFi", "Kitchen", "Pool", "Beachfront", "Hot Tub", "BBQ", "Parking"],
        "bedrooms": 4,
        "bathrooms": 3,
        "guests": 8,
        "description": "Exclusive beachfront property with direct beach access and breathtaking ocean views.",
        "popular": True,
        "featured": True,
        "discount": 8
    },
    {
        "id": 3,
        "title": "Alpine Retreat Mountain Spa",
        "location": "Aspen, Colorado",
        "price": 320,
        "original_price": 380,
        "type": "Mountain Cabin",
        "rating": 4.89,
        "reviews": 94,
        "superhost": True,
        "instant_book": False,
        "image": "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?q=80&w=2070&auto=format&fit=crop",
        "amenities": ["WiFi", "Kitchen", "Hot Tub", "Fireplace", "Mountain View", "Hiking", "Spa"],
        "bedrooms": 2,
        "bathrooms": 2,
        "guests": 4,
        "description": "Cozy mountain cabin perfect for ski trips and summer getaways with modern comforts.",
        "popular": False,
        "featured": False,
        "discount": 18
    },
    {
        "id": 4,
        "title": "Designer Loft Arts District",
        "location": "Chicago, Illinois",
        "price": 280,
        "original_price": 320,
        "type": "Designer Loft",
        "rating": 4.92,
        "reviews": 156,
        "superhost": False,
        "instant_book": True,
        "image": "https://images.unsplash.com/photo-1536376072261-38c75010e6c9?q=80&w=2071&auto=format&fit=crop",
        "amenities": ["WiFi", "Kitchen", "AC", "Workspace", "Balcony", "City View", "Art Studio"],
        "bedrooms": 1,
        "bathrooms": 1,
        "guests": 2,
        "description": "Beautifully designed loft in the heart of the arts district with high ceilings and natural light.",
        "popular": True,
        "featured": False,
        "discount": 14
    },
    {
        "id": 5,
        "title": "Tropical Paradise Private Island",
        "location": "Miami, Florida",
        "price": 620,
        "original_price": 690,
        "type": "Beach House",
        "rating": 4.96,
        "reviews": 203,
        "superhost": True,
        "instant_book": True,
        "image": "https://q-xx.bstatic.com/xdata/images/hotel/max1024x768/450518775.jpg?k=31a259c55a2326c5e08569d8d56c8ad3d436c6780b5f5b71dd5fab3b1ba9764b&o=&s=1024x",
        "amenities": ["WiFi", "Kitchen", "Pool", "Beachfront", "BBQ", "Garden", "Parking", "Private Beach"],
        "bedrooms": 3,
        "bathrooms": 2,
        "guests": 6,
        "description": "Private tropical oasis with direct beach access and lush garden surroundings.",
        "popular": True,
        "featured": True,
        "discount": 12
    },
    {
        "id": 6,
        "title": "Historic Castle Medieval Experience",
        "location": "Edinburgh, Scotland",
        "price": 1200,
        "original_price": 1500,
        "type": "Historic Castle",
        "rating": 4.99,
        "reviews": 45,
        "superhost": True,
        "instant_book": False,
        "image": "https://images.unsplash.com/photo-1589656384667-54f1c6bd9066?q=80&w=2069&auto=format&fit=crop",
        "amenities": ["WiFi", "Kitchen", "Fireplace", "Historic", "Gardens", "Library", "Wine Cellar"],
        "bedrooms": 8,
        "bathrooms": 6,
        "guests": 16,
        "description": "Authentic medieval castle with modern amenities and historic charm.",
        "popular": False,
        "featured": True,
        "discount": 25
    }
]

df = pd.DataFrame(properties)

# --- INITIALIZE CHATBOT ---
chatbot = NexusStayChatbot()

# --- SESSION STATE INITIALIZATION ---
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = []
if 'bookings' not in st.session_state:
    st.session_state.bookings = []
if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "bot", "content": "Hello! I'm your NexusStay AI Assistant! 🏰\nHow can I help you find the perfect luxury accommodation today?"}
    ]
if 'show_chatbot' not in st.session_state:
    st.session_state.show_chatbot = False

# --- HEADER SECTION ---
col1, col2, col3, col4 = st.columns([2, 3, 2, 1])
with col1:
    st.markdown("<h1 style='color: #FF385C; font-size: 2.8rem; margin-bottom: 0; text-shadow: 0 2px 10px rgba(255,56,92,0.5);'>🏰 NexusStay</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #00D4AA; margin-top: 0; font-size: 1.1rem;'>AI Luxury Retreats</p>", unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h2 style='color: #FFFFFF; margin-bottom: 0.5rem; text-shadow: 0 2px 8px rgba(0,0,0,0.5);'>Discover Elite Stays</h2>
        <p style='color: #B0B0B0;'>AI-Powered Luxury Property Search</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    col3a, col3b, col3c = st.columns(3)
    with col3a:
        st.metric("Wishlist", f"{len(st.session_state.wishlist)}", "❤️")
    with col3b:
        st.metric("Bookings", f"{len(st.session_state.bookings)}", "📅")
    with col3c:
        st.metric("AI Online", "✅", "🤖")
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
    if st.button("🤖 AI Assistant", key="chatbot_toggle"):
        st.session_state.show_chatbot = not st.session_state.show_chatbot
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- AI CHATBOT SECTION ---
if st.session_state.show_chatbot:
    st.markdown("### 🤖 NexusStay AI Assistant")
    
    with st.container():
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        for message in st.session_state.chat_messages:
            if message["role"] == "user":
                st.markdown(f'<div class="chat-message user-message">{message["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message bot-message">{message["content"]}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Chat input
    col_input, col_send = st.columns([4, 1])
    with col_input:
        user_input = st.text_input("Type your message...", key="chat_input", placeholder="Ask about properties, prices, or amenities...")
    with col_send:
        send_button = st.button("Send", key="send_message")
    
    if send_button and user_input:
        # Add user message
        st.session_state.chat_messages.append({"role": "user", "content": user_input})
        
        # Get bot response
        with st.spinner("AI is thinking..."):
            bot_response = chatbot.get_response(user_input)
            st.session_state.chat_messages.append({"role": "bot", "content": bot_response})
        
        st.rerun()

# --- ENHANCED SEARCH BAR ---
st.markdown("""
<div style='background: linear-gradient(145deg, var(--card-dark) 0%, var(--card-darker) 100%); 
            padding: 2rem; border-radius: 20px; margin-bottom: 2rem; border: 1px solid var(--border);'>
    <div style='display: grid; grid-template-columns: 2fr 1fr 1fr 1fr auto; gap: 1rem; align-items: end;'>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])

with col1:
    search_query = st.text_input(
        "🔍 AI-Powered Search", 
        placeholder="Search by location, amenities, or property type...",
        key="search_input"
    )

with col2:
    check_in = st.date_input("📅 Check-in", datetime.now(), key="check_in")

with col3:
    check_out = st.date_input("📅 Check-out", datetime.now() + timedelta(days=7), key="check_out")

with col4:
    guests = st.selectbox("👥 Guests", [1, 2, 3, 4, 5, 6, 7, 8, "8+"], key="guests")

with col5:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 AI Search", key="search_main", use_container_width=True):
        st.session_state.search_performed = True
        st.session_state.search_query = search_query
        st.rerun()

st.markdown("</div></div>", unsafe_allow_html=True)

# --- PREMIUM STATISTICS SECTION ---
st.markdown("### 📊 AI Analytics Dashboard")
stats_col1, stats_col2, stats_col3, stats_col4, stats_col5 = st.columns(5)

with stats_col1:
    st.markdown("""
    <div class='stats-card-dark'>
        <div class='stats-number'>1.2K+</div>
        <div class='stats-label'>AI-Matched Properties</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col2:
    st.markdown("""
    <div class='stats-card-dark'>
        <div class='stats-number'>4.9⭐</div>
        <div class='stats-label'>AI Verified Rating</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col3:
    st.markdown("""
    <div class='stats-card-dark'>
        <div class='stats-number'>50+</div>
        <div class='stats-label'>AI Optimized Locations</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col4:
    st.markdown("""
    <div class='stats-card-dark'>
        <div class='stats-number'>24/7</div>
        <div class='stats-label'>AI Concierge</div>
    </div>
    """, unsafe_allow_html=True)

with stats_col5:
    st.markdown("""
    <div class='stats-card-dark'>
        <div class='stats-number'>98%</div>
        <div class='stats-label'>AI Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

# --- ENHANCED SIDEBAR FILTERS ---
st.sidebar.markdown("## ⚡ AI Smart Filters")

# AI Recommendations
st.sidebar.markdown("### 🧠 AI Suggestions")
ai_recommend = st.sidebar.checkbox("Show AI Recommended", True)
trending = st.sidebar.checkbox("Trending Properties", False)

# Price Range
st.sidebar.markdown("### 💎 Smart Price Range")
min_price, max_price = st.sidebar.slider(
    "AI Optimized Pricing",
    min_value=0,
    max_value=2000,
    value=(200, 800),
    key="price_slider"
)

# Property Type with AI Icons
st.sidebar.markdown("### 🏰 AI-Categorized Types")
property_types = df['type'].unique()
selected_types = []
for ptype in property_types:
    if st.sidebar.checkbox(f"🤖 {ptype}", True, key=f"type_{ptype}"):
        selected_types.append(ptype)

# AI Features
st.sidebar.markdown("### ⭐ AI Verified Features")
superhost_only = st.sidebar.checkbox("AI Verified Superhost", True)
instant_book = st.sidebar.checkbox("AI Instant Book", True)
high_rating = st.sidebar.checkbox("AI Top Rated 4.9+", False)

# Smart Rating Filter
st.sidebar.markdown("### 🌟 AI Rating Intelligence")
min_rating = st.sidebar.slider("AI Recommended Minimum", 4.0, 5.0, 4.7, 0.1)

# --- ENHANCED FILTERING LOGIC WITH AI SEARCH ---
filtered_df = df[
    (df['price'] >= min_price) & 
    (df['price'] <= max_price) &
    (df['type'].isin(selected_types)) &
    (df['rating'] >= min_rating)
]

# AI-Powered Search
if st.session_state.search_query:
    search_lower = st.session_state.search_query.lower()
    filtered_df = filtered_df[
        filtered_df['title'].str.lower().str.contains(search_lower) |
        filtered_df['location'].str.lower().str.contains(search_lower) |
        filtered_df['amenities'].apply(lambda x: any(search_lower in amenity.lower() for amenity in x)) |
        filtered_df['type'].str.lower().str.contains(search_lower)
    ]

# AI Recommendations
if ai_recommend:
    filtered_df = filtered_df[filtered_df['featured'] == True]

if trending:
    filtered_df = filtered_df[filtered_df['popular'] == True]

if superhost_only:
    filtered_df = filtered_df[filtered_df['superhost'] == True]

if instant_book:
    filtered_df = filtered_df[filtered_df['instant_book'] == True]

if high_rating:
    filtered_df = filtered_df[filtered_df['rating'] >= 4.9]

# --- PROPERTY LISTINGS WITH AI ENHANCEMENTS ---
st.markdown(f"## 🏰 AI-Curated Collection ({len(filtered_df)} smart matches)")

if filtered_df.empty:
    st.warning("🤖 No AI-matched properties found. Try adjusting your search or ask the AI assistant for help!")
    if st.button("🎯 Get AI Recommendations"):
        st.session_state.chat_messages.append({
            "role": "user", 
            "content": "Can you recommend some luxury properties?"
        })
        st.session_state.chat_messages.append({
            "role": "bot",
            "content": "Based on popular choices, I recommend:\n\n• Luxury apartments in New York\n• Beach villas in Malibu\n• Mountain cabins in Aspen\n• Historic castles in Edinburgh\n\nTry searching for these or ask me more specific questions!"
        })
        st.session_state.show_chatbot = True
        st.rerun()
else:
    # Display AI-enhanced properties
    cols = st.columns(3)
    for i, property in enumerate(filtered_df.to_dict('records')):
        with cols[i % 3]:
            discount = property.get('discount')
            
            # AI Enhanced Property Card
            with st.container():
                st.markdown(f"""
                <div class='premium-dark-card'>
                    <div style='position: relative;'>
                        <img src="{property['image']}" class='card-image' alt="{property['title']}">
                        {f"<div style='position: absolute; top: 10px; right: 10px; background: linear-gradient(135deg, #FF385C, #FF6B81); color: white; padding: 0.5rem 1rem; border-radius: 20px; font-weight: bold; font-size: 0.8rem; box-shadow: 0 4px 12px rgba(255,56,92,0.5);'>🔥 AI DEAL {discount}% OFF</div>" if discount else ''}
                        {('<div style="position: absolute; top: 10px; left: 10px; background: rgba(0,0,0,0.7); color: #FFB800; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.7rem; font-weight: bold;">🤖 AI PICK</div>' if property['featured'] else '')}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # AI Enhanced Content
                col_title, col_rating = st.columns([3, 1])
                with col_title:
                    st.markdown(f"**{property['title']}**")
                with col_rating:
                    st.markdown(f"<div style='background: linear-gradient(135deg, #FFB800, #FFD700); color: black; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8rem; font-weight: bold; text-align: center;'>🤖 {property['rating']}</div>", unsafe_allow_html=True)
                
                # AI Verified Badges
                location_text = f"📍 {property['location']}"
                if property['superhost']:
                    location_text += " <span class='superhost-badge'>AI VERIFIED</span>"
                if property['instant_book']:
                    location_text += " <span class='superhost-badge' style='background:linear-gradient(135deg, #00D4AA, #00E5C4)'>INSTANT</span>"
                
                st.markdown(location_text, unsafe_allow_html=True)
                
                # Smart Amenities
                amenities_text = " ".join([f"<span class='amenity-item-dark'>{amenity}</span>" for amenity in property['amenities'][:4]])
                st.markdown(amenities_text, unsafe_allow_html=True)
                
                # AI Pricing
                col_price, col_details = st.columns([1, 1])
                with col_price:
                    st.markdown(f"<div style='font-size: 1.3rem; font-weight: bold; color: #FF385C;'>${property['price']}/night</div>", unsafe_allow_html=True)
                    if discount:
                        st.markdown(f"<div style='color: #B0B0B0; text-decoration: line-through; font-size: 0.9rem;'>${property['original_price']}</div>", unsafe_allow_html=True)
                
                with col_details:
                    st.markdown(f"<div style='color: #B0B0B0; font-size: 0.9rem; text-align: right;'>🛏️ {property['bedrooms']} • 🛁 {property['bathrooms']} • 👥 {property['guests']}</div>", unsafe_allow_html=True)
                
                # AI Confidence Score
                st.markdown(f"""
                <div class='progress-bar'>
                    <div class='progress-fill' style='width: {(property['rating'] - 4.0) * 100}%'></div>
                </div>
                <div style='color: #B0B0B0; font-size: 0.8rem; text-align: center;'>AI Match: {int((property['rating'] - 4.0) * 100)}%</div>
                """, unsafe_allow_html=True)
                
                # AI Action Buttons
                col_book, col_wish, col_ai = st.columns([2, 1, 1])
                with col_book:
                    if st.button("🚀 Book Now", key=f"book_{property['id']}", use_container_width=True):
                        st.session_state.bookings.append(property)
                        st.success(f"🎉 AI confirmed booking for '{property['title']}'!")
                        st.balloons()
                with col_wish:
                    is_in_wishlist = property['id'] in [p['id'] for p in st.session_state.wishlist]
                    button_text = "💝" if is_in_wishlist else "🤍"
                    if st.button(button_text, key=f"wish_{property['id']}", use_container_width=True):
                        if is_in_wishlist:
                            st.session_state.wishlist = [p for p in st.session_state.wishlist if p['id'] != property['id']]
                            st.info("💔 AI removed from wishlist")
                        else:
                            st.session_state.wishlist.append(property)
                            st.success("💝 AI added to smart wishlist!")
                with col_ai:
                    if st.button("🤖", key=f"ai_{property['id']}", use_container_width=True):
                        st.session_state.chat_messages.append({
                            "role": "user", 
                            "content": f"Tell me more about {property['title']} in {property['location']}"
                        })
                        st.session_state.chat_messages.append({
                            "role": "bot",
                            "content": f"🤖 **AI Analysis for {property['title']}:**\n\n⭐ Rating: {property['rating']}/5.0\n💰 Price: ${property['price']}/night\n🏠 Type: {property['type']}\n🎯 Best for: {property['guests']} guests\n\nKey features: {', '.join(property['amenities'][:3])}\n\nThis property is {'AI RECOMMENDED' if property['featured'] else 'available'}!"
                        })
                        st.session_state.show_chatbot = True
                        st.rerun()

# --- AI DESTINATIONS ---
st.markdown("## 🌍 AI Smart Destinations")

dest_col1, dest_col2, dest_col3, dest_col4 = st.columns(4)

destinations = [
    {"name": "New York", "image": "https://images.unsplash.com/photo-1485738422979-f5c462d49f74?q=80&w=2099&auto=format&fit=crop", "properties": "1,200+", "rating": "4.8", "ai_tip": "Trending: Luxury apartments"},
    {"name": "Paris", "image": "https://images.unsplash.com/photo-1546436836-07a91091f160?q=80&w=2074&auto=format&fit=crop", "properties": "800+", "rating": "4.9", "ai_tip": "Romantic getaways"},
    {"name": "Tokyo", "image": "https://img.traveltriangle.com/blog/wp-content/uploads/2019/12/Places-To-Visit-In-Tokyo-6_dec.jpg", "properties": "950+", "rating": "4.7", "ai_tip": "Modern luxury"},
    {"name": "Bali", "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=2070&auto=format&fit=crop", "properties": "1,500+", "rating": "4.9", "ai_tip": "Beach villas"}
]

for i, dest in enumerate(destinations):
    with [dest_col1, dest_col2, dest_col3, dest_col4][i]:
        st.markdown(f"""
        <div style='background: linear-gradient(145deg, var(--card-dark) 0%, var(--card-darker) 100%); 
                    border-radius: 15px; padding: 0; overflow: hidden; border: 1px solid var(--border);'>
            <img src='{dest['image']}' style='width: 100%; height: 120px; object-fit: cover;'>
            <div style='padding: 1rem;'>
                <h4 style='color: var(--text-primary); margin: 0;'>{dest['name']}</h4>
                <p style='color: var(--text-secondary); margin: 0.5rem 0; font-size: 0.9rem;'>
                    <strong>{dest['properties']}</strong> AI-optimized
                </p>
                <div style='color: #FFB800; font-size: 0.8rem;'>🤖 {dest['rating']} rating</div>
                <div style='color: #00D4AA; font-size: 0.7rem; margin-top: 0.5rem;'>💡 {dest['ai_tip']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- ENHANCED FOOTER ---
st.markdown("---")
footer_col1, footer_col2, footer_col3, footer_col4, footer_col5 = st.columns(5)

with footer_col1:
    st.markdown("**🏰 NexusStay AI**")
    st.markdown("Smart Search")
    st.markdown("AI Matching")
    st.markdown("Predictive Analytics")

with footer_col2:
    st.markdown("**🛡️ AI Support**")
    st.markdown("24/7 AI Concierge")
    st.markdown("Smart Safety")
    st.markdown("AI Verification")

with footer_col3:
    st.markdown("**🌟 AI Hosting**")
    st.markdown("Become AI Host")
    st.markdown("Smart Pricing")
    st.markdown("AI Community")

with footer_col4:
    st.markdown("**📱 AI Experience**")
    st.markdown("AI Mobile App")
    st.markdown("Virtual AI Tours")
    st.markdown("Smart Loyalty")

with footer_col5:
    st.markdown("**🔗 AI Connect**")
    st.markdown("AI Blog")
    st.markdown("Smart Updates")
    st.markdown("AI Research")

st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem; background: var(--card-darker); border-radius: 15px; margin-top: 2rem; border: 1px solid var(--border);'>
    <p style='margin: 0;'>© NexusStay AI Elite. Powered by Artificial Intelligence by Tanmay.</p>
    <p style='margin: 0.5rem 0 0 0; color: var(--text-secondary);'>AI Privacy · Smart Terms · Neural Sitemap · ML Standards</p>
</div>
""", unsafe_allow_html=True)

# --- AI WISHLIST SIDEBAR ---
if st.session_state.wishlist:
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"### 💝 AI Wishlist ({len(st.session_state.wishlist)})")
    for i, item in enumerate(st.session_state.wishlist[:3]):
        st.sidebar.markdown(f"**{i+1}. {item['title']}**")
        st.sidebar.markdown(f"🤖 ${item['price']}/night ⭐ {item['rating']}")
    
    if len(st.session_state.wishlist) > 3:
        st.sidebar.markdown(f"🤖 ... and {len(st.session_state.wishlist) - 3} more AI picks")

# --- QUICK AI TIPS ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 AI Quick Tips")
st.sidebar.info("""
**Try asking our AI:**
- "Find beach properties"
- "Budget under $500"  
- "Family-friendly stays"
- "Luxury amenities"
- "Best locations for couples"
- "Recommend top properties"
- "How to book"
- "Cancellation policy"
""")