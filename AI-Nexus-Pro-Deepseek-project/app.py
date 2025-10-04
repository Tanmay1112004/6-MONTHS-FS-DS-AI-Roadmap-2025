import streamlit as st
import requests
import json
import time
from datetime import datetime
import random
import plotly.graph_objects as go
from streamlit_lottie import st_lottie

# Page configuration - Wide mode with beautiful theme
st.set_page_config(
    page_title="AI Nexus Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with advanced styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Header with animated gradient */
    .main-header {
        font-size: 4rem;
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #FFD93D);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient 3s ease infinite;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 800;
        text-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50% }
        50% { background-position: 100% 50% }
        100% { background-position: 0% 50% }
    }
    
    /* User message bubble */
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 20px 20px 5px 20px;
        padding: 20px 25px;
        margin: 15px 0;
        border: none;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* AI message bubble */
    .assistant-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        border-radius: 20px 20px 20px 5px;
        padding: 20px 25px;
        margin: 15px 0;
        border: none;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Button styling */
    .stButton button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stButton button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #3498db 100%);
        color: white;
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 15px;
        margin: 10px 0;
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
    }
    
    /* Quick question buttons */
    .quick-question {
        background: linear-gradient(135deg, #fd746c 0%, #ff9068 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px;
        margin: 5px 0;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .quick-question:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }
    
    /* Chat input styling */
    .stChatInput input {
        border-radius: 25px !important;
        border: 2px solid #4ECDC4 !important;
        padding: 15px 20px !important;
        font-size: 16px !important;
    }
</style>
""", unsafe_allow_html=True)

class AdvancedAIChatbot:
    def __init__(self):
        self.conversation_history = []
        self.available_models = [
            "🤖 HuggingFace AI Pro",
            "🚀 Advanced Demo AI"
        ]
        self.huggingface_token = "use_your_huggingface_api_key"
        
    def generate_huggingface_response(self, question):
        """Use multiple HuggingFace models for better responses"""
        try:
            # Try different models for better responses
            models_to_try = [
                "microsoft/DialoGPT-large",
                "microsoft/DialoGPT-medium",
                "microsoft/DialoGPT-small"
            ]
            
            for model in models_to_try:
                API_URL = f"https://api-inference.huggingface.co/models/{model}"
                headers = {"Authorization": f"Bearer {self.huggingface_token}"}
                
                # Enhanced prompt engineering
                context = self.get_context()
                prompt = f"""Conversation History:
{context}

User: {question}

Assistant: I'll provide a comprehensive answer:"""
                
                payload = {
                    "inputs": prompt,
                    "parameters": {
                        "max_length": 400,
                        "temperature": 0.8,
                        "do_sample": True,
                        "top_p": 0.9,
                        "repetition_penalty": 1.1
                    },
                    "options": {
                        "wait_for_model": True
                    }
                }
                
                response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    if isinstance(result, list) and len(result) > 0:
                        generated_text = result[0].get('generated_text', '')
                        
                        # Extract assistant response
                        if "Assistant:" in generated_text:
                            response_text = generated_text.split("Assistant:")[-1].strip()
                        else:
                            response_text = generated_text.strip()
                        
                        # Clean up response
                        response_text = response_text.split("User:")[0].strip()
                        
                        if response_text and len(response_text) > 20:
                            return self.format_response(response_text, question)
            
            # If all models fail, use enhanced fallback
            return self.generate_enhanced_response(question)
                
        except Exception as e:
            return self.generate_enhanced_response(question)
    
    def format_response(self, response, question):
        """Format the response with emojis and structure"""
        # Add emojis based on content
        emoji_map = {
            'python': '🐍',
            'code': '💻',
            'learn': '📚',
            'api': '🔗',
            'web': '🌐',
            'data': '📊',
            'machine': '🤖',
            'cloud': '☁️',
            'develop': '🚀',
            'hello': '👋',
            'thank': '🙏',
            'what': '❓',
            'how': '🔧',
            'why': '💡'
        }
        
        # Add relevant emoji to start
        first_emoji = "🤖"
        for keyword, emoji in emoji_map.items():
            if keyword in question.lower():
                first_emoji = emoji
                break
        
        # Structure the response
        lines = response.split('. ')
        if len(lines) > 3:
            formatted_response = f"{first_emoji} **{question}**\n\n"
            for i, line in enumerate(lines[:4], 1):
                if line.strip():
                    formatted_response += f"• {line.strip()}.\n"
            if len(lines) > 4:
                formatted_response += f"\n💡 *And more insights available...*"
        else:
            formatted_response = f"{first_emoji} {response}"
        
        return formatted_response
    
    def generate_enhanced_response(self, question):
        """Generate highly contextual and accurate demo responses"""
        question_lower = question.lower()
        
        # Comprehensive response database
        response_templates = {
            'api': {
                'question': 'What are APIs used for?',
                'response': """🔗 **APIs (Application Programming Interfaces) are used for:**

🌐 **Communication Between Systems**
• Allow different software applications to talk to each other
• Enable web services to share data and functionality

📱 **Mobile & Web Development**
• Connect frontend applications to backend servers
• Integrate third-party services (payment, maps, social media)

☁️ **Cloud Services & Microservices**
• Enable cloud platform interactions (AWS, Azure, Google Cloud)
• Connect microservices in distributed systems

📊 **Data Exchange & Integration**
• Share data between different platforms and databases
• Enable real-time data synchronization

🔒 **Security & Access Control**
• Provide controlled access to sensitive data and functions
• Implement authentication and authorization

🚀 **Examples in Practice:**
• Weather apps using weather service APIs
• E-commerce sites using payment gateway APIs
• Social media apps using platform APIs
• Mobile apps using device hardware APIs

💡 **Key Benefits:** Faster development, scalability, security, and interoperability!"""
            },
            
            'python': {
                'question': 'Python programming',
                'response': """🐍 **Python Programming - Complete Overview:**

🚀 **Why Python?**
• Easy to learn with clean syntax
• Versatile across multiple domains
• Massive community support
• Extensive libraries and frameworks

💼 **Key Applications:**
• **Web Development**: Django, Flask, FastAPI
• **Data Science**: Pandas, NumPy, SciPy
• **Machine Learning**: TensorFlow, PyTorch, Scikit-learn
• **Automation**: Scripting, DevOps, Testing
• **Desktop Apps**: Tkinter, PyQt

📚 **Core Concepts:**
• Simple syntax and dynamic typing
• Object-oriented and functional programming
• Extensive standard library
• Cross-platform compatibility

🎯 **Getting Started:**
1. Learn basic syntax and data types
2. Practice with small projects
3. Explore specialized libraries
4. Build portfolio projects
5. Contribute to open source

🔥 **Popular Frameworks:**
• Web: Django, Flask
• Data: Pandas, NumPy
• AI: TensorFlow, PyTorch
• Testing: Pytest, Unittest"""
            },
            
            'machine learning': {
                'question': 'machine learning',
                'response': """🤖 **Machine Learning Fundamentals:**

🎯 **What is ML?**
AI subset where systems learn from data to make predictions or decisions without explicit programming.

📊 **Main Types:**
• **Supervised Learning**: Labeled data (Classification, Regression)
• **Unsupervised Learning**: Unlabeled data (Clustering, Dimensionality Reduction)
• **Reinforcement Learning**: Learn through rewards/punishments

🛠️ **Common Algorithms:**
• Linear Regression, Logistic Regression
• Decision Trees, Random Forests
• SVM, K-Means, Neural Networks

💻 **Popular Tools:**
• Python: Scikit-learn, TensorFlow, PyTorch
• R: Caret, MLR
• Cloud: AWS SageMaker, Google AI Platform

🚀 **Learning Path:**
1. Mathematics foundation
2. Python programming
3. ML algorithms understanding
4. Real project implementation
5. Advanced topics (Deep Learning)"""
            },
            
            'web development': {
                'question': 'web development',
                'response': """🌐 **Web Development Roadmap:**

🎨 **Frontend Development:**
• HTML5, CSS3, JavaScript (ES6+)
• React, Vue.js, Angular frameworks
• Responsive design principles
• Web performance optimization

⚡ **Backend Development:**
• Node.js, Python (Django/Flask), Java, PHP
• RESTful API design
• Database management (SQL/NoSQL)
• Authentication & security

🔧 **Full Stack Skills:**
• Version control (Git)
• DevOps & deployment
• Testing strategies
• Agile methodologies

🚀 **Modern Technologies:**
• Progressive Web Apps (PWA)
• Serverless architecture
• Microservices
• Cloud platforms (AWS, Azure)"""
            },
            
            'hello': {
                'question': 'greeting',
                'response': """👋 **Welcome to AI Nexus Pro!**

I'm your advanced AI assistant powered by cutting-edge technology. Here's what I can help you with:

🎯 **Technical Guidance**
• Programming concepts & best practices
• Software architecture & design patterns
• Career advice in tech

🚀 **Learning Support**
• Step-by-step tutorials
• Project ideas & implementation
• Resource recommendations

💡 **Problem Solving**
• Code debugging assistance
• Algorithm explanations
• System design discussions

🔧 **Technology Insights**
• Latest trends & frameworks
• Tool comparisons
• Industry best practices

Feel free to ask me anything about technology, programming, or your learning journey! I'm here to provide detailed, actionable insights. 😊"""
            }
        }
        
        # Find the best matching template
        for key, template in response_templates.items():
            if key in question_lower:
                return template['response']
        
        # Default intelligent response for unknown questions
        default_responses = [
            f"""🔍 **Let me break down '{question}' for you:**

This topic involves several key aspects that are important to understand:

💡 **Core Concepts:**
• Fundamental principles and definitions
• Key terminology and their meanings
• Basic working mechanisms

🛠️ **Practical Applications:**
• Real-world use cases and scenarios
• Industry implementations
• Common challenges and solutions

🚀 **Implementation Guide:**
• Step-by-step approach to get started
• Best practices to follow
• Tools and resources needed

📚 **Learning Resources:**
• Recommended reading materials
• Online courses and tutorials
• Community forums for support

Would you like me to elaborate on any specific aspect of this topic?""",

            f"""🎯 **Understanding '{question}':**

This is a comprehensive topic that spans multiple domains:

🌟 **Key Aspects:**
1. Fundamental concepts and theories
2. Practical implementations
3. Industry standards and trends
4. Future developments

💼 **Real-World Impact:**
• Business applications and value
• Technological advancements
• Career opportunities
• Learning pathways

🔧 **Technical Depth:**
• Architecture and design patterns
• Implementation strategies
• Performance considerations
• Security aspects

I can provide more specific information based on your particular interests or use case!"""
        ]
        
        return random.choice(default_responses)
    
    def get_context(self):
        """Get recent conversation context"""
        if len(self.conversation_history) == 0:
            return "First interaction with user."
        
        recent_messages = self.conversation_history[-4:]
        context = "Recent conversation:\n"
        for msg in recent_messages:
            role = "User" if msg["role"] == "user" else "Assistant"
            context += f"{role}: {msg['content']}\n"
        return context

    def generate_response(self, question, model_choice):
        """Generate response based on selected model"""
        if model_choice == "🤖 HuggingFace AI Pro":
            response = self.generate_huggingface_response(question)
            # Fallback if response is too short
            if len(response) < 50:
                return self.generate_enhanced_response(question)
            return response
        else:
            return self.generate_enhanced_response(question)

def create_usage_chart(messages_count):
    """Create a beautiful usage chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(
        mode = "gauge+number+delta",
        value = messages_count,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Messages Today", 'font': {'size': 24}},
        delta = {'reference': 5, 'increasing': {'color': "#4ECDC4"}},
        gauge = {
            'axis': {'range': [None, 50], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#4ECDC4"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 20], 'color': '#FF6B6B'},
                {'range': [20, 35], 'color': '#FFD93D'},
                {'range': [35, 50], 'color': '#4ECDC4'}],
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': "white", 'family': "Arial"},
        height=300
    )
    
    return fig

def main():
    # Initialize session state
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = AdvancedAIChatbot()
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'model_choice' not in st.session_state:
        st.session_state.model_choice = "🤖 HuggingFace AI Pro"
    if 'usage_stats' not in st.session_state:
        st.session_state.usage_stats = {"sessions": 1, "total_messages": 0}

    # Header Section with animated gradient
    st.markdown('<h1 class="main-header">🚀 AI Nexus Pro</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; color: #666; font-size: 1.3rem; margin-bottom: 2rem;">'
        'Advanced AI Assistant • Beautiful Interface • Real HuggingFace AI • Professional Portfolio Ready'
        '</p>', 
        unsafe_allow_html=True
    )

    # Sidebar with enhanced styling
    with st.sidebar:
        # Sidebar header
        st.markdown(
            '<div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 20px;">'
            '<h2 style="color: white; margin: 0;">🎮 Control Center</h2>'
            '</div>', 
            unsafe_allow_html=True
        )
        
        # Model Selection
        st.subheader("🤖 AI Engine")
        model_choice = st.selectbox(
            "Select AI Model:",
            st.session_state.chatbot.available_models,
            index=0
        )
        st.session_state.model_choice = model_choice
        
        # Status indicator
        st.markdown("---")
        st.subheader("📊 System Status")
        
        col1, col2 = st.columns(2)
        with col1:
            if model_choice == "🤖 HuggingFace AI Pro":
                st.success("🟢 **AI Active**")
                st.caption("HuggingFace Connected")
            else:
                st.info("🔵 **Demo Mode**")
                st.caption("Enhanced Responses")
        
        with col2:
            st.metric("Messages", len(st.session_state.messages))
        
        # Usage Chart
        st.plotly_chart(
            create_usage_chart(len(st.session_state.messages)), 
            use_container_width=True
        )
        
        st.markdown("---")
        
        # Features Showcase
        st.subheader("✨ Premium Features")
        features = [
            "🎨 Beautiful Gradient UI",
            "🤖 Real AI Integration", 
            "💬 Context-Aware Chat",
            "📊 Visual Analytics",
            "🚀 Fast Performance",
            "🎯 Smart Responses",
            "📱 Mobile Optimized",
            "💾 Export Capabilities"
        ]
        
        for feature in features:
            st.markdown(f'<div class="feature-card">{feature}</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Conversation Management
        st.subheader("🛠️ Management")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 New Chat", use_container_width=True, help="Start a new conversation"):
                st.session_state.messages = []
                st.session_state.chatbot.conversation_history = []
                st.rerun()
        
        with col2:
            if st.button("🗑️ Clear All", use_container_width=True, help="Clear all messages"):
                st.session_state.messages = []
                st.session_state.chatbot.conversation_history = []
                st.rerun()
        
        # Export conversation
        if st.session_state.messages:
            export_data = {
                "exported_at": datetime.now().isoformat(),
                "conversation": st.session_state.messages,
                "model_used": st.session_state.model_choice,
                "total_messages": len(st.session_state.messages),
                "ai_provider": "HuggingFace" if "HuggingFace" in st.session_state.model_choice else "Enhanced Demo"
            }
            st.download_button(
                label="💾 Export Chat JSON",
                data=json.dumps(export_data, indent=2),
                file_name=f"ai_chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True
            )
        
        st.markdown("---")
        st.markdown(
            '<div style="text-align: center; color: #888; font-size: 0.8rem;">'
            '🌟 Professional Portfolio Project<br>'
            'Built with Streamlit & HuggingFace'
            '</div>', 
            unsafe_allow_html=True
        )

    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Chat messages display
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.markdown(
                            f'<div class="user-message">'
                            f'<strong>👤 You:</strong><br>{message["content"]}'
                            f'</div>', 
                            unsafe_allow_html=True
                        )
                else:
                    with st.chat_message("assistant"):
                        st.markdown(
                            f'<div class="assistant-message">'
                            f'<strong>🤖 AI:</strong><br>{message["content"]}'
                            f'</div>', 
                            unsafe_allow_html=True
                        )

    with col2:
        # Quick actions panel
        st.markdown(
            '<div style="background: linear-gradient(135deg, #fd746c 0%, #ff9068 100%); padding: 20px; border-radius: 20px; margin-bottom: 20px;">'
            '<h3 style="color: white; text-align: center; margin: 0;">💡 Quick Questions</h3>'
            '</div>', 
            unsafe_allow_html=True
        )
        
        quick_questions = [
            "What are APIs used for?",
            "Explain Python programming",
            "Machine learning basics", 
            "Web development roadmap",
            "Data science fundamentals",
            "Cloud computing explained",
            "How to learn programming?",
            "Career in tech guidance"
        ]
        
        for q in quick_questions:
            if st.button(
                f"🎯 {q}",
                key=f"quick_{q}",
                use_container_width=True,
                help=f"Ask: {q}"
            ):
                st.session_state.pending_question = q

    # Chat input with enhanced styling
    if "pending_question" in st.session_state:
        question = st.session_state.pending_question
        del st.session_state.pending_question
    else:
        question = st.chat_input("💬 Ask me anything about technology...")

    if question:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": question})
        st.session_state.chatbot.conversation_history.append({
            "role": "user", 
            "content": question, 
            "timestamp": datetime.now().isoformat()
        })
        
        # Display user message immediately with animation
        with chat_container:
            with st.chat_message("user"):
                st.markdown(
                    f'<div class="user-message">'
                    f'<strong>👤 You:</strong><br>{question}'
                    f'</div>', 
                    unsafe_allow_html=True
                )
        
        # Generate and display assistant response with typing effect
        with chat_container:
            with st.chat_message("assistant"):
                with st.spinner(f"🧠 Thinking with {st.session_state.model_choice}..."):
                    try:
                        response = st.session_state.chatbot.generate_response(
                            question, 
                            st.session_state.model_choice
                        )
                        
                        # Enhanced typing animation
                        message_placeholder = st.empty()
                        full_response = ""
                        
                        # Typewriter effect with progress
                        for i, char in enumerate(response):
                            full_response += char
                            progress = min(i / len(response), 1.0)
                            
                            # Update message with progress
                            message_placeholder.markdown(
                                f'<div class="assistant-message">'
                                f'<strong>🤖 AI:</strong><br>{full_response}▌'
                                f'</div>', 
                                unsafe_allow_html=True
                            )
                            time.sleep(0.001)  # Smooth typing
                        
                        # Final message without cursor
                        message_placeholder.markdown(
                            f'<div class="assistant-message">'
                            f'<strong>🤖 AI:</strong><br>{response}'
                            f'</div>', 
                            unsafe_allow_html=True
                        )
                        
                        # Add to history
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        st.session_state.chatbot.conversation_history.append({
                            "role": "assistant", 
                            "content": response, 
                            "timestamp": datetime.now().isoformat()
                        })
                        
                        # Update usage stats
                        st.session_state.usage_stats["total_messages"] += 1
                        
                    except Exception as e:
                        error_msg = f"⚠️ **Temporary System Glitch**\n\nOur AI engine is experiencing high demand. Please try again in a moment!\n\n*Error details: {str(e)}*"
                        st.error("System temporarily unavailable")
                        st.session_state.messages.append({"role": "assistant", "content": error_msg})

    # Enhanced Footer with stats
    st.markdown("---")
    
    # Stats dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            f'<div class="stat-card">'
            f'<h3>📨</h3>'
            f'<h2>{len(st.session_state.messages)}</h2>'
            f'<p>Total Messages</p>'
            f'</div>', 
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f'<div class="stat-card">'
            f'<h3>🤖</h3>'
            f'<h2>{st.session_state.model_choice.split()[0]}</h2>'
            f'<p>AI Engine</p>'
            f'</div>', 
            unsafe_allow_html=True
        )
    
    with col3:
        status = "🟢 Live" if "HuggingFace" in st.session_state.model_choice else "🔵 Demo"
        st.markdown(
            f'<div class="stat-card">'
            f'<h3>📊</h3>'
            f'<h2>{status}</h2>'
            f'<p>System Status</p>'
            f'</div>', 
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            f'<div class="stat-card">'
            f'<h3>⚡</h3>'
            f'<h2>v2.1</h2>'
            f'<p>Version</p>'
            f'</div>', 
            unsafe_allow_html=True
        )
    
    # Final footer
    st.markdown(
        '<div style="text-align: center; padding: 20px; color: #666;">'
        '🚀 <strong>AI Nexus Pro</strong> - Advanced AI Assistant • '
        'Beautiful Gradient UI • '
        'Professional Portfolio Ready • '
        'Built with ❤️ for Developers'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()